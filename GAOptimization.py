# Import libraries
import numpy as np
from PIL import Image
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys, random, ast, time
from pathlib import Path
import re

# Import Qiskit
from qiskit import Aer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram
from qiskit.providers.aer import QasmSimulator
from qiskit.providers.aer.noise.errors import thermal_relaxation_error, pauli_error
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer import noise

# Import other necessary Python files
import simRunQW


def singleQubitErrorRates(data):
    '''Returns as a dictionary the single qubit error rates, as they appear on ibmq_16_melbourne. NOTE: the 
    values deviate every time the machine gets callibrated.'''
    qubits = data.Qubit.tolist()
    del qubits[0]
    rates = data.SQError.tolist()
    del rates[0]
    sqRates = dict(zip(qubits, rates))
    
    return sqRates

def twoQubitErrorRates(data):
    '''Returns as a dictionary the two qubit error rates, as they appear on ibmq_16_melbourne. NOTE: the values 
    deviate every time the machine gets callibrated.'''
    tqer = data.TQError.tolist()
    del tqer[0]

    qpairs = []
    qvals = []
    for i in range(0, len(tqer)):
        tqer[i] = tqer[i].replace("cx", "Q")

        s = tqer[i].split(",")
        for j in range(0, len(s)):
            t = s[j].split(":")
            qpairs.append(t[0].replace(" ", ""))
            qvals.append(float(t[1].replace(" ", "")))

    tqRates = dict(zip(qpairs, qvals))
    
    return tqRates

def measureErrorRates(data):
    '''Returns as a dictionary the measurement error rates, as they appear on ibmq_16_melbourne. NOTE: the values
    deviate every time the machine gets callibrated'''
    qubits = data.Qubit.tolist()
    del qubits[0]
    rates = data.ReadoutError.tolist()
    del rates[0]
    measRates = dict(zip(qubits, rates))
    
    return measRates

def getDecoherenceTimes(data):
    '''Returns the thermal relaxation time T1 and the qubit dephasing time T2, as given by IBMQ.'''
    t1er = data.T1.tolist()
    del t1er[0]
    t2er = data.T2.tolist()
    del t2er[0]

    for i in range(0, len(t1er)):
        t1er[i] = float(t1er[i] + "e3")
        t2er[i] = float(t2er[i] + "e3")

    T1s = np.array(t1er)
    T2s = np.array(t2er)
    
    # Check for error in IBMQ's measurements (i.e it must always be T2 <= 2T1)
    c = 0
    for i in range(0,len(T1s)):
        if (T2s[i] > 2*T1s[i]):
            c = 1
            print("ERROR: incompatible decay rates - Qubit Q", i, ", T2 =", T2s[i], "and T1 =", T1s[i])
    if (c == 0):
        print(r'Checking decoherence times: all ok')

    return T1s,T2s

def noisyGate(line):
    '''Simulates a bit-flip channel. With a randomely generated probability p an X gate is chosen,
    whereas with (1-p) the Identity is chosen. The probability of error is chosen according to the
    qubit selected each time.'''
    sqRates = singleQubitErrorRates() # Dictionary containing the single qubit error rates
    tqRates = twoQubitErrorRates() # Dictionary containing the two qubit error rates
    
    # Generate the operation according to single- or two-qubit error rates
    if (("u1" in line) or ("u2" in line) or ("u3" in line) or (".x" in line)):
        s = line.split('[')
        s = s[1].split(']')
        qubit = ("Q" + s[0])
        op = list(np.random.choice(["X", "I"], 1, p=[sqRates[qubit], 1-sqRates[qubit]]))
    elif ("cx" in line):
        s = line.split('(')
        s = s[1].split(',')
        s0 = s[0].split('[')
        s0 = s0[1].split(']')
        q1 = s0[0]
        s0 = s[1].split('[')
        s0 = s0[1].split(']')
        q2 = s0[0]
        qubits = ("Q" + q1 + "_" + q2)
        op = list(np.random.choice(["X", "I"], 1, p=[tqRates[qubits], 1-tqRates[qubits]]))
    
    return op

def noisyMeasure(line):
    '''Simulates the noisey measurement. The probability is chosen according to the qubit being measured. The
    argument `line` is a string containing the line of code that this  '''
    measRates = measureErrorRates() # Dictionary containing the measurement error rates per qubit
    
    # Find out which qubit is being measured
    s = line.split('q')
    s = s[1].split('[')
    s = s[1].split(']')
    qubit = ("Q" + s[0])
    
    op = list(np.random.choice(["X", "I"], 1, p=[measRates[qubit], 1-measRates[qubit]]))
    
    return op

def qwQASM(path):
    '''Runs the formatted python file from the path and returns the circuit.'''
    
    %run -i path
        
    return circ

def noiseFreeqwQASM(path):
    '''Runs the formatted, noise-free python file from the path and returns the circuit.'''
    
    %run -i path
    
    return circ

def machineData(path):
    '''Imports the error rates of the machine as the downloaded csv file. path - the path to the csv file, including
    the name of the csv file and ".csv".'''
    
    colnames = ["Qubit", "T1", "T2", "Frequency", "ReadoutError", "SQError", "TQError", "Date"]
    
    data = pandas.read_csv(path, names=colnames)
    
    return data

def getQState(qwalk):
    '''Method to get the quantum state before the measurement. This is in particular
    for a N=8 cycle.'''
    sv_simulator = Aer.get_backend('statevector_simulator')

    # Execute and get counts
    result = execute(qwalk, sv_simulator).result()
    statevector = result.get_statevector(qwalk)

    # Create the statevector
    b = []
    for k in range(0,len(statevector)):
        b.append(k)

    i = iter(statevector)
    j = iter(b)
    dct = dict(zip(j, i))

    # Create the dictionary without all the    
    qstate = {}
    for i in range(0,len(dct)):
        qstate[format(i, '#05b')[2:]] = dct[i]
                        
    return qstate

def getQStateList(dct):
    '''Method that returns the states and the probabilities of the entire experiment (dictionary)
    as a list containing tuples [(x1,p1),...,(xB,pB)]'''
    lst = list(dct.items())
    for i in range(0,len(lst)):
        t = list(lst[i])
        lst[i] = tuple(t)
    
    return lst

def getNonZeros(dct):
    '''Method that returns the positions of the state space that have non-zero amplitudes in
    the form of a dictionary.'''
    non_zeros = dict()

    for key in dct.keys():
        if (dct[key] != (0+0j)):
            non_zeros[key] = dct[key]
            
    return non_zeros

def getStateVectorProbabilities(qw_circ):
    '''Methods that calculates the probabilities of each position of the state space from
    the amplitudes of the quantum state. Returns a dictionary that contains the states with
    removed the ancilla and coin qubits.'''
    qstate = getQState(ideal_circ)
    dct = getNonZeros(qstate)
    probs = dict()
    dct1 = dict()
    dct2 = dict()
    newdct = dict()

    for key in dct.keys():
        s = re.findall(r'.{,0}''.',key)
        newkey = s[1]+s[2]+s[0]
        newdct[newkey] = dct[key]

    newdct = dict(OrderedDict(sorted(newdct.items())))

    for key in newdct.keys():
        if (key[0] == '0'):
            dct1[key] = newdct[key]
        elif (key[0] == '1'):
            dct2[key] = newdct[key]

    # The two states with the same last 2 qubits (state space) will have their amplitudes squared
    # and sumed to give the probability for the state.
    for key_1 in dct1.keys():
        probs[key_1[1:len(key_1)]] = dct1[key_1]**2
        probs[key_1[1:len(key_1)]] = abs(round(probs[key_1[1:len(key_1)]].real, 4))
        for key_2 in dct2.keys():
            if (key_1[1:len(key_1)] == key_2[1:len(key_2)]):
                probs[key_1[1:len(key_1)]] = dct1[key_1]**2 + dct2[key_2]**2
                probs[key_1[1:len(key_1)]] = abs(round(probs[key_1[1:len(key_1)]].real, 4))
            else:
                if key_2[1:len(key_2)] not in probs:
                    probs[key_2[1:len(key_2)]] = dct2[key_2]**2
                    probs[key_2[1:len(key_2)]] = abs(round(probs[key_2[1:len(key_2)]].real, 4))

    return probs

def runExperiments(trials, circ, iterations, device, path):
    '''Method to run the experiments on the real machine.'''
    # Create and open the file for the experiments
    simCount = 0
    myfile = open(path + ".txt", mode='wt', encoding='utf-8')
    
    # Horizontal architecture
    for i in range(0, trials):
        # Run the experiments
        print("Experiment count: " + str(simCount+1))
        job_device = execute(circ, device, shots = iterations)
        job_monitor(job_device)
        counts = job_device.result().get_counts(0)
        counts = dict(OrderedDict(sorted(counts.items())))
        simCount = simCount + 1

        # Write the results
        line = str(counts)
        myfile.write("%s\n" % line)
        myfile.flush()

            
    # Finalize and close the file for the results
    myfile.close()
    
    return None

def getData(exFilename, prob):
    '''Returns the data as list of dictionaries. prob - True if we want the data to be returned as probability
    distributions instead of counts. NOTE: careful with the name of the datafiles.'''
    with open(path + exFilename) as f:
        content = f.readlines()
    experimentData = [ast.literal_eval(x.strip('\n')) for x in content]
    f.close()

    # Format the lists with probabilities instead of counts of positions
    if (prob==True):
        for i in range(0,len(experimentData)):
            dct = ast.literal_eval(experimentData[i])
            keys = list(dct.keys())
            values = list(dct.values())
            for j in range(0,len(values)):
                values[j] = values[j]/1000
            dct = dict(zip(keys, values))
            experimentData[i] = (str(dct))
        
    return experimentData

def getAvgData(data):
    '''Returns the average distribution of all the data collected from the trials on the quantum computer.'''
    avg_dct = dict()
    
    for key in data[0].keys():
        sm = 0
        for i in range(0,len(data)):
            sm = sm + data[i][key]
            
        avg_dct[key] = sm/len(data)
    
    return avg_dct

def getSQGateExecutionTime(gate, backend):
    '''Returns the average execution time of the single-qubit type gates we are interested in.'''
    # Single qubit gates
    s = [0]*15
    for i in range(0,15):
        s[i] = backend.properties().gate_length(gate, [i])

    return (np.mean(s)*(10**9))

def getTQGateExecutionTime(gate, backend):
    '''Returns the average execution time of the two-qubit type gates in the circuit.'''
    # Two qubit gates
    graph = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [7,8], [8,9], [9,10], [10,11], [11,12], [12,13], [13,14],
            [0,14], [1,13], [2,12], [3,11], [4,10], [5,9], [6,8]]

    t = [0]*len(graph)
    for i in range(0,len(graph)):
        t[i] = backend.properties().gate_length('cx', graph[i])

    return (np.mean(t)*(10**9))

def thermalRelaxationChannel(backend):
    '''Method that returns the thermal relaxation error quantum channel.'''
    # T1 and T2
    T1s,T2s = getDecoherenceTimes()

    # Instruction times (in nanoseconds)
    time_u1 = 10 # virtual gate
    time_u2 = getSQGateExecutionTime('u2', backend) # Average of all u2 times
    time_u3 = getSQGateExecutionTime('u3', backend) # Average of all u3 times
    time_cx = getTQGateExecutionTime('cx', backend) # Average of all cx times
    time_reset = 1000  # 1 microsecond
    time_measure = 1000 # 1 microsecond

    # QuantumError objects
    errors_reset = [thermal_relaxation_error(t1, t2, time_reset)
                    for t1, t2 in zip(T1s, T2s)]
    errors_measure = [thermal_relaxation_error(t1, t2, time_measure)
                      for t1, t2 in zip(T1s, T2s)]
    errors_u1  = [thermal_relaxation_error(t1, t2, time_u1)
                  for t1, t2 in zip(T1s, T2s)]
    errors_u2  = [thermal_relaxation_error(t1, t2, time_u2)
                  for t1, t2 in zip(T1s, T2s)]
    errors_u3  = [thermal_relaxation_error(t1, t2, time_u3)
                  for t1, t2 in zip(T1s, T2s)]
    errors_cx = [[thermal_relaxation_error(t1a, t2a, time_cx).expand(
                 thermal_relaxation_error(t1b, t2b, time_cx))
                  for t1a, t2a in zip(T1s, T2s)]
                   for t1b, t2b in zip(T1s, T2s)]

    # Add errors to noise model
    noise_thermal = NoiseModel()
    for j in range(len(T1s)):
        noise_thermal.add_quantum_error(errors_reset[j], "reset", [j])
        noise_thermal.add_quantum_error(errors_measure[j], "measure", [j])
        noise_thermal.add_quantum_error(errors_u1[j], "u1", [j])
        noise_thermal.add_quantum_error(errors_u2[j], "u2", [j])
        noise_thermal.add_quantum_error(errors_u3[j], "u3", [j])
        for k in range(len(T1s)):
            noise_thermal.add_quantum_error(errors_cx[j][k], "cx", [j, k])
            
    return noise_thermal

def qwNoiseExecute(iterations, thermal):
    '''This method executes the circuit. This is necessary, since the circuit has to be generated each time for the new gates to appear'''
    counts = [{}]*iterations
    
    if (thermal == False):
        for i in range(0,iterations):
            sys.stdout.write('\r'+"Simulation count: "+str(i+1))
            circ = qwQASM()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), shots=1).result()
            counts[i] = simulate.get_counts()
    else:
        noise_thermal = thermalRelaxationChannel()
        for i in range(0,iterations):
            sys.stdout.write('\r'+"Simulation count: "+str(i+1))
            circ = qwQASM()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), basis_gates=noise_thermal.basis_gates, 
                               noise_model=noise_thermal, shots=1).result()
            counts[i] = simulate.get_counts()
    
    return counts

def getCounts(counts, iterations):
    '''Method that formats the results of the simulation to a dictionary.'''
    l = [()]*len(counts)
    # Create a list of tuples of the form [(key, value), ...]
    for i in range(0,iterations):
        keys = list(counts[i].keys())[0]
        values = list(counts[i].values())[0]
        l[i] = (keys, values)

    # Make the list into a dictionary
    dct = {}    
    for a, b in l: 
        dct.setdefault(a, []).append(b)
    
    # Sum up all the duplicating locations to get their total occurences
    for i in dct:
        dct[i] = sum(dct[i])
    
    return dct

def hellingerDistance(p, q):
    '''Calculate the Hellinger distance between two probability distributions, P and Q. P and Q aregiven as simple 
    arrays containing the probabilities p[i] and q[i]. IMPORTANT: the probability arrays have to be ordered in the 
    same way.'''
    sum = 0
    for i in range (0, len(p)):
        sum = sum + (np.sqrt(p[i]) - np.sqrt(q[i]))**2
        
    h = (1/np.sqrt(2))*np.sqrt(sum)
        
    return h

def getProbabilities(dct,N):
    '''Creates list of probabilities from the given line of data.'''
    p = list(dct.values())
    for i in range(0,len(p)):
        p[i] = p[i]/N
    
    return p

######## Genetic Algorithm Methods ########

def initChrom(chromosome):
    '''Function used to return the chromosome that will be used to initialize the population.'''
    chromosome = [int(chromosome[i:i+1], 2) for i in range(0, len(chromosome))]
    
    return chromosome

def fixSameSupport(dct_ex, dct_si):
    '''Forces two dictionaries to have the same support.'''
    # First we import the entries of the experiments that dont appear in the simulations in the simulations
    # dictionary. Each entry will have probability 0
    for keys_ex in dct_ex.keys():
        if keys_ex not in dct_si:
            dct_si.update({keys_ex: 0})

    # Second, we import the entries of the simulations that don't appear in the experimental data dictionary.
    # Each entry will have probability 0
    for keys_si in dct_si.keys():
        if keys_si not in dct_ex:
            dct_ex.update({keys_si: 0})

    dct_ex = dict(OrderedDict(sorted(dct_ex.items())))
    dct_si = dict(OrderedDict(sorted(dct_si.items())))
    
    return dct_ex,dct_si

def getSubsystemRates(q, num_q, s_q):
    '''Gets the relevant error rates for the system we want. q is a list of tuples of the qubits in the system that two-qubit
    gates act on. s_q is the list of qubits of the real machine that participate (i.e Q1, Q0, Q3, etc etc)'''
    sqRates = singleQubitErrorRates() # Single-qubit error rates
    tqRates = twoQubitErrorRates() # Two-qubit error rates
    measRates = measureErrorRates() # Measurement error rates
    sqRatesSub = [0]*(num_q)
    tqRatesSub = [0]*len(q)
    measRatesSub = [0]*(num_q)
    
    # Prepare the single-qubit rates and the measure rates
    for i in range(0, num_q):
        s = ("Q" + str(s_q[i]))
        sqRatesSub[i] = sqRates[s]
        measRatesSub[i] = measRates[s]
    
    # Prepare the two-qubit rates
    for i in range(0, len(q)):
        s = ("Q" + str(q[i][0]) + "_" + str(q[i][1]))
        tqRatesSub[i] = tqRates[s]
    
    return sqRatesSub,tqRatesSub,measRatesSub

def paramEncoding(scalar, *param):
    '''Encode the parameters to bit-strings. Note: we know all the param arguments are lists. nor is the value
    that we will use as a scaling parameter for making the error rates to integers.'''
    values = []
    binaries = []
    chromosome = ""
    
    # Format the values so that they won't have a decimal point
    for i in range(0, len(param)):
        for j in range(0, len(param[i])):
            values.append(int(param[i][j]*scalar))
            
    # Find the longest binary representation, so we can decide the length of the error rates (we want equal length)
    # representations in the binary string.
    l = [0]*len(values)
    for i in range(0, len(values)):
        l[i] = len("{0:b}".format(values[i]))
    length = l[0]
    for i in range(1, len(values)):
        if (l[i] > length):
            length = l[i]
            
    print("=> The length of each encoded parameter is", length, "bits.")
    b = '0' + str(length) + 'b' # The string that gives the length of the binary representation
    
    # Make the values to binary string representation. IMPORTANT: careful with the number of bits. It is fine 
    # for the 2-qubit system. It is now scalable
    for i in range(0, len(values)):
        binaries.append(format(values[i], b))
        
    # Create the encoded parameter - chromosome
    for i in range(0, len(binaries)):
        chromosome = (chromosome + binaries[i])
        
    # Check if the length of the chromosome is correct, i.e num_q*length
    c = (len(chromosome) == len(values)*length)
    if (c == False):
        print("=> Error on chromosome length.")
    else:
        print("=> Chromosome length correct.")
    
    return chromosome

def decode(solution, scalar, num_rates, num_q):
    '''Decodes a solution/chromosome to its component error rates.'''
    # Decode genetic algorithm solution to error rates
    decoded_Q0Rate_bits = solution[0:(int(len(solution)/num_rates))]
    decoded_Q1Rate_bits = solution[(int(len(solution)/num_rates)):2*(int(len(solution)/num_rates))]
    decoded_Q2Rate_bits = solution[2*(int(len(solution)/num_rates)):3*(int(len(solution)/num_rates))]
    decoded_CNOT0_1Rate_bits = solution[3*(int(len(solution)/num_rates)):4*(int(len(solution)/num_rates))]
    decoded_CNOT1_2Rate_bits = solution[4*(int(len(solution)/num_rates)):5*(int(len(solution)/num_rates))]
    decoded_M0Rate_bits = solution[5*(int(len(solution)/num_rates)):6*(int(len(solution)/num_rates))]
    decoded_M1Rate_bits = solution[6*(int(len(solution)/num_rates)):7*(int(len(solution)/num_rates))]
    decoded_M2Rate_bits = solution[7*(int(len(solution)/num_rates)):8*(int(len(solution)/num_rates))]
    
    ### Fixes for the chromosome representation ###
    for i in range(0,len(decoded_Q0Rate_bits)):
        decoded_Q0Rate_bits[i] = str(decoded_Q0Rate_bits[i])
        decoded_Q1Rate_bits[i] = str(decoded_Q1Rate_bits[i])
        decoded_Q2Rate_bits[i] = str(decoded_Q2Rate_bits[i])
        decoded_CNOT0_1Rate_bits[i] = str(decoded_CNOT0_1Rate_bits[i])
        decoded_CNOT1_2Rate_bits[i] = str(decoded_CNOT1_2Rate_bits[i])
        decoded_M0Rate_bits[i] = str(decoded_M0Rate_bits[i])
        decoded_M1Rate_bits[i] = str(decoded_M1Rate_bits[i])
        decoded_M2Rate_bits[i] = str(decoded_M2Rate_bits[i])
    decoded_Q0Rate_bits = "".join(decoded_Q0Rate_bits)
    decoded_Q1Rate_bits = "".join(decoded_Q1Rate_bits)
    decoded_Q2Rate_bits = "".join(decoded_Q2Rate_bits)
    decoded_CNOT0_1Rate_bits = "".join(decoded_CNOT0_1Rate_bits)
    decoded_CNOT1_2Rate_bits = "".join(decoded_CNOT1_2Rate_bits)
    decoded_M0Rate_bits = "".join(decoded_M0Rate_bits)
    decoded_M1Rate_bits = "".join(decoded_M1Rate_bits)
    decoded_M2Rate_bits = "".join(decoded_M2Rate_bits)
    ###############################################
    
    decoded_Q0Rate = int(decoded_Q0Rate_bits, 2)/scalar
    decoded_Q1Rate = int(decoded_Q1Rate_bits, 2)/scalar
    decoded_Q2Rate = int(decoded_Q2Rate_bits, 2)/scalar
    decoded_CNOT0_1Rate = int(decoded_CNOT0_1Rate_bits, 2)/scalar
    decoded_CNOT1_2Rate = int(decoded_CNOT1_2Rate_bits, 2)/scalar
    decoded_M0Rate = int(decoded_M0Rate_bits, 2)/scalar
    decoded_M1Rate = int(decoded_M1Rate_bits, 2)/scalar
    decoded_M2Rate = int(decoded_M2Rate_bits, 2)/scalar
    
    decodedRates = [decoded_Q0Rate, decoded_Q1Rate, decoded_Q2Rate, decoded_CNOT0_1Rate, decoded_CNOT1_2Rate, decoded_M0Rate, decoded_M1Rate, decoded_M2Rate]
    
    return decodedRates

def hd_evaluate(solution):
    '''Function that evaluates the fitness of the new generation using Hellinger distance as the fitness function.
    Arguments: scalar (int) - the scalar used to make the error rates to integers, solution (str) - the solution resukting from
    the application of the Genetic Algorithm (or could be the chromosome), num_rates (int) - the number of error rates 
    encoded in the chromosome (3 for the simple two qubit system), num_q - the number of qubits in the system. Returns: 
    fitness (float) - the fitness value, i.e theHellinger distance, that we want to minimize'''
    fitness = 0.0
    scalar = 1000000
    num_rates = 8
    num_q = 3
    avgExData = {'00': 158.5, '01': 316.8, '10': 135.1, '11': 389.6}
    thermal = False
        
    # Decode genetic algorithm solution to error rates
    decoded_Q0Rate_bits = list(solution[0:(int(len(solution)/num_rates))])
    decoded_Q1Rate_bits = solution[(int(len(solution)/num_rates)):2*(int(len(solution)/num_rates))]
    decoded_Q2Rate_bits = solution[2*(int(len(solution)/num_rates)):3*(int(len(solution)/num_rates))]
    decoded_CNOT0_1Rate_bits = solution[3*(int(len(solution)/num_rates)):4*(int(len(solution)/num_rates))]
    decoded_CNOT1_2Rate_bits = solution[4*(int(len(solution)/num_rates)):5*(int(len(solution)/num_rates))]
    decoded_M0Rate_bits = solution[5*(int(len(solution)/num_rates)):6*(int(len(solution)/num_rates))]
    decoded_M1Rate_bits = solution[6*(int(len(solution)/num_rates)):7*(int(len(solution)/num_rates))]
    decoded_M2Rate_bits = solution[7*(int(len(solution)/num_rates)):8*(int(len(solution)/num_rates))]
        
    ### Fixes for the chromosome representation ###
    for i in range(0,len(decoded_Q0Rate_bits)):
        decoded_Q0Rate_bits[i] = str(decoded_Q0Rate_bits[i])
        decoded_Q1Rate_bits[i] = str(decoded_Q1Rate_bits[i])
        decoded_Q2Rate_bits[i] = str(decoded_Q2Rate_bits[i])
        decoded_CNOT0_1Rate_bits[i] = str(decoded_CNOT0_1Rate_bits[i])
        decoded_CNOT1_2Rate_bits[i] = str(decoded_CNOT1_2Rate_bits[i])
        decoded_M0Rate_bits[i] = str(decoded_M0Rate_bits[i])
        decoded_M1Rate_bits[i] = str(decoded_M1Rate_bits[i])
        decoded_M2Rate_bits[i] = str(decoded_M2Rate_bits[i])
    decoded_Q0Rate_bits = "".join(decoded_Q0Rate_bits)
    decoded_Q1Rate_bits = "".join(decoded_Q1Rate_bits)
    decoded_Q2Rate_bits = "".join(decoded_Q2Rate_bits)
    decoded_CNOT0_1Rate_bits = "".join(decoded_CNOT0_1Rate_bits)
    decoded_CNOT1_2Rate_bits = "".join(decoded_CNOT1_2Rate_bits)
    decoded_M0Rate_bits = "".join(decoded_M0Rate_bits)
    decoded_M1Rate_bits = "".join(decoded_M1Rate_bits)
    decoded_M2Rate_bits = "".join(decoded_M2Rate_bits)
    ###############################################
    
    Q0Rate = int(decoded_Q0Rate_bits, 2)/scalar
    Q1Rate = int(decoded_Q1Rate_bits, 2)/scalar
    Q2Rate = int(decoded_Q2Rate_bits, 2)/scalar
    CNOT0_1Rate = int(decoded_CNOT0_1Rate_bits, 2)/scalar
    CNOT1_2Rate = int(decoded_CNOT1_2Rate_bits, 2)/scalar
    M0Rate = int(decoded_M0Rate_bits, 2)/scalar
    M1Rate = int(decoded_M1Rate_bits, 2)/scalar
    M2Rate = int(decoded_M2Rate_bits, 2)/scalar
    
    ratesList = [Q0Rate, Q1Rate, Q2Rate, CNOT0_1Rate, CNOT1_2Rate, M0Rate, M1Rate, M2Rate]
    
    # Run simulation with the rates
    iterations = 1000 # Probably always fixed on 1,000
    counts = simRunQW.combinedExecute(iterations, thermal, num_q, ratesList)
    counts = simRunQW.getCombinedCounts(counts, iterations)
    counts = dict(OrderedDict(sorted(counts.items())))
    
    # Format the returned distributions in a way that we can calculate the Hellinger Distance
    p,q = fixSameSupport(avgExData, counts)
    p = getProbabilities(avgExData, iterations)
    q = getProbabilities(counts, iterations)
    
    # Calculate the HD as fitness score for the GA
    fitness = hellingerDistance(p, q)
    print((str(decode(solution, scalar, num_rates, num_q)) + ", with hd ="), fitness)
    
    return fitness,

def getBest(population, scalar):
    '''Returns the best solution generated by the optimization procedure.'''
    best_individuals = tools.selBest(population, k = 1)
    num_rates = 8
    best_Q0Rate = None
    best_Q1Rate = None
    best_Q2Rate = None
    best_CNOT0_1Rate = None
    best_CNOT1_2Rate = None
    best_M0Rate = None
    best_M1Rate = None
    best_M2Rate = None

    for bi in best_individuals:
        # Decode genetic algorithm solution to error rates
        Q0Rate_bits = bi[0:(int(len(bi)/num_rates))]
        Q1Rate_bits = bi[(int(len(bi)/num_rates)):2*(int(len(bi)/num_rates))]
        Q2Rate_bits = bi[2*(int(len(bi)/num_rates)):3*(int(len(bi)/num_rates))]
        CNOT0_1Rate_bits = bi[3*(int(len(bi)/num_rates)):4*(int(len(bi)/num_rates))]
        CNOT1_2Rate_bits = bi[4*(int(len(bi)/num_rates)):5*(int(len(bi)/num_rates))]
        M0Rate_bits = bi[5*(int(len(bi)/num_rates)):6*(int(len(bi)/num_rates))]
        M1Rate_bits = bi[6*(int(len(bi)/num_rates)):7*(int(len(bi)/num_rates))]
        M2Rate_bits = bi[7*(int(len(bi)/num_rates)):8*(int(len(bi)/num_rates))]

        ### Fixes for the chromosome representation ###
        for i in range(0,len(Q0Rate_bits)):
            Q0Rate_bits[i] = str(Q0Rate_bits[i])
            Q1Rate_bits[i] = str(Q1Rate_bits[i])
            Q2Rate_bits[i] = str(Q2Rate_bits[i])
            CNOT0_1Rate_bits[i] = str(CNOT0_1Rate_bits[i])
            CNOT1_2Rate_bits[i] = str(CNOT1_2Rate_bits[i])
            M0Rate_bits[i] = str(M0Rate_bits[i])
            M1Rate_bits[i] = str(M1Rate_bits[i])
            M2Rate_bits[i] = str(M2Rate_bits[i])
        Q0Rate_bits = "".join(Q0Rate_bits)
        Q1Rate_bits = "".join(Q1Rate_bits)
        Q2Rate_bits = "".join(Q2Rate_bits)
        CNOT0_1Rate_bits = "".join(CNOT0_1Rate_bits)
        CNOT1_2Rate_bits = "".join(CNOT1_2Rate_bits)
        M0Rate_bits = "".join(M0Rate_bits)
        M1Rate_bits = "".join(M1Rate_bits)
        M2Rate_bits = "".join(M2Rate_bits)
        ###############################################

        best_Q0Rate = int(Q0Rate_bits, 2)/scalar
        best_Q1Rate = int(Q1Rate_bits, 2)/scalar
        best_Q2Rate = int(Q2Rate_bits, 2)/scalar
        best_CNOT0_1Rate = int(CNOT0_1Rate_bits, 2)/scalar
        best_CNOT1_2Rate = int(CNOT1_2Rate_bits, 2)/scalar
        best_M0Rate = int(M0Rate_bits, 2)/scalar
        best_M1Rate = int(M1Rate_bits, 2)/scalar
        best_M2Rate = int(M2Rate_bits, 2)/scalar
        
        bestRates = [best_Q0Rate, best_Q1Rate, best_Q2Rate, best_CNOT0_1Rate, best_CNOT1_2Rate, best_M0Rate, best_M1Rate, best_M2Rate]
        
    return bestRates

def getIndividuals(creator, initChrom, n, chromosome):
    ''''''
    scalar = 1000000
    num_rates = 8
    num_q = 3
    individuals = []
    
    # Hardcode the IBMQ rates
    individual = initChrom(chromosome)
    b = '0' + str(int(len(individual)/num_rates)) + 'b'
    individual = creator(individual)
    individuals.append(individual)
        
    # Randomize the remaining rates
    for i in range(0, n-1):
        decodedRates = decode(initChrom(chromosome), scalar, num_rates, num_q)
        rc0 = format(abs(int((decodedRates[0] + np.random.normal(0, 0.0005, 1))*scalar)), b)
        rc1 = format(abs(int((decodedRates[1] + np.random.normal(0, 0.0005, 1))*scalar)), b)
        rc2 = format(abs(int((decodedRates[2] + np.random.normal(0, 0.0005, 1))*scalar)), b)
        rc3 = format(abs(int((decodedRates[3] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc4 = format(abs(int((decodedRates[4] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc5 = format(abs(int((decodedRates[5] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc6 = format(abs(int((decodedRates[6] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc7 = format(abs(int((decodedRates[7] + np.random.normal(0, 0.005, 1))*scalar)), b)
        randchrom = rc0 + rc1 + rc2 + rc3 + rc4 + rc5 + rc6 + rc7
        individual = initChrom(randchrom)
        individual = creator(individual)
        individuals.append(individual)
    
    return individuals

def runGA(population_size, num_generations, gene_length, scalar, chromosome, num_rates, num_q):
    '''Runs the parameter optimization and returns the best solution.'''
    # We want to minimise the HD, thus we give weights = -1
    creator.create('FitnessMin', base.Fitness, weights = (-1.0,))
    creator.create('Individual', list , fitness = creator.FitnessMin)
    
    # Create the tools for the GA
    toolbox = base.Toolbox()
    toolbox.register('binary', bernoulli.rvs, 0.5)
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.binary, n = gene_length)
    toolbox.register('population', getIndividuals, creator.Individual , initChrom) # For initializing with specific population
    toolbox.register('mate', tools.cxOrdered)
    toolbox.register('mutate', tools.mutFlipBit, indpb = 0.2)
    toolbox.register('select', tools.selTournament, tournsize = 4)
    toolbox.register('evaluate', hd_evaluate)

    # Generate the initial population with the specified size
    population = toolbox.population(n = population_size, chromosome = chromosome) # For initializing with specific population
    print("The starting population:", end = ' ')
    for i in range(0,population_size):
        print(decode(population[i], scalar, num_rates, num_q), end = ' ')
    print("\n")
    
    # Run the Genetic Algorithm
    start_time = time.time()
    r = algorithms.eaSimple(population, toolbox, cxpb = 0.5, mutpb = 0.2, ngen = num_generations, verbose = False)
    end_time = time.time()
    print("\nTime elapsed:", end_time - start_time, "seconds.")
    
    # Get the error rates that perform the best
    bestRates = getBest(population, scalar)
    
    return bestRates

######## Run the Parameter Optimization ########


def optimise():
    '''Method used to optimise the error rate parameters. All the results are shown while the method
    is run. Please allow ample time for the GA optimisation to succeed.'''
    # Required variables
    provider = IBMQ.load_account() # Loads the IBMQ account
    device = provider.get_backend('ibmq_16_melbourne') # Prefered device
    backend = Aer.get_backend("qasm_simulator") # The simulator
    iterations = 1000 # Iterations should remain constant to ensure consistency

    # Get the probabilities of the states from the state vector
    start_time = time.time()
    ideal_circ = noiseFreeqwQASM() # The measurements have to be commented out
    end_time = time.time()
    print("\nTime elapsed:", end_time - start_time, "seconds.")
    p_ideal = getStateVectorProbabilities(ideal_circ)
    p_ideal = dict(OrderedDict(sorted(p_ideal.items())))
    print("Ideal probability distribution:", p_ideal)

    # Run experiments on the quantum computer and import the data
    qw_circ = noiseFreeqwQASM()
    trials = 10
    runExperiments(trials, qw_circ, iterations, device, path)
    exData = getData(path, False)
    print("Quantum computer data:", exData)
    avgExData = getAvgData(exData)
    print("\nAverage counts on quantum computer trials:", avgExData)

    # Run the combined quantum noise simulator and get the distribution pre-optimization
    start_time = time.time()
    counts_comb = qwNoiseExecute(iterations, thermal = True)
    end_time = time.time()
    print("\nTime elapsed:", end_time - start_time, "seconds.")
    counts_comb = getCounts(counts_comb, iterations)
    counts_comb = dict(OrderedDict(sorted(counts_comb.items())))
    print("\nCounts on noisy quantum simulator:", counts_comb)

    # Calculate the HD pre-optimization
    h_pre = hellingerDistance(getProbabilities(avgExData, iterations), getProbabilities(counts_comb, iterations))
    print("Hellinger Distance pre-optimization:", h_pre)

    # Prepare for the GA optimization
    q_pairs = [(0,1), (1,2)] # List of qubit pairs in ibmq_16_melbourne
    s_q = [0, 1, 2] # The qubits themselves
    num_q = len(s_q) # Number of qubits in the system
    num_rates = 8 # Number of parameters for optimization
    scalar = 1000000 # Scalar used to eliminate floating point in the encoded parameters binary representation
    thermal = False # Decide whether we want the thermal relaxation channel or not. Note: if yes, the evaluation takes longer

    # Get the error rates relevant to our system
    sqRates,tqRates,measRates = getSubsystemRates(q_pairs, num_q, s_q)

    # Encode the parameters to get the chromosome bit-string
    chromosome = paramEncoding(scalar, sqRates, tqRates, measRates)
    init_chrom = decode(initChrom(chromosome), scalar, 8, num_q)
    print("Initial chromosome:", init_chrom, end = '\n')

    # Evaluate the initial Hellinger distance
    init_fitness = hd_evaluate(initChrom(chromosome))

    # Run the GA Optimization
    population_size = 4 # The number of solutions generated every time
    num_generations = 10 # The number of generations, i.e how many times the populations will reproduce
    gene_length = len(chromosome)
    bestRates = runGA(population_size, num_generations, gene_length, scalar, chromosome, num_rates, num_q)
    print("The optimized error rates are:", bestRates)

    # Run simulation with the best error rates resulting from the GA
    post_counts = combinedExecute(iterations, True, num_q, bestRates)
    post_counts = simRunQW.getCombinedCounts(post_counts, iterations)
    post_counts = dict(OrderedDict(sorted(post_counts.items())))
    print(post_counts)

    # Find the HD post-optimization
    h_post = hellingerDistance(getProbabilities(avgExData, iterations), getProbabilities(post_counts, iterations))
    print("Hellinger distance post-optimization:", h_post)
    
    return None