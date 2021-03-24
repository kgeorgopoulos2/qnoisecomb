# Import libraries
import numpy as np
from numpy import pi as pi
from PIL import Image
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys, random, ast, time
from pathlib import Path
import re
import pandas
import inspect

# Import GA libraries
from deap import base, creator, tools, algorithms
from scipy.stats import bernoulli
from bitstring import BitArray

# Import Qiskit
from qiskit import Aer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram
from qiskit.providers.aer import QasmSimulator
from qiskit.providers.aer.noise.errors import thermal_relaxation_error, pauli_error
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer import noise
from qiskit.tools.monitor import backend_monitor

############ Importing QASM codes ############

def qwQASM():
    '''Runs the formatted python file from the path and returns the circuit.'''
    
    %run -i "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/QASM Codes/Formatted6qQW.py"
        
    return circ

def noiseFreeqwQASM():
    '''Runs the formatted, noise-free python file from the path and returns the circuit.'''
    
    %run -i "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/QASM Codes/NoiseFreeFormatted6qQW.py"
    
    return circ

############ Getting the error rates ############

def machineData(path):
    '''Imports the error rates of the machine as the downloaded csv file. path - the path to the csv file, including
    the name of the csv file and ".csv".'''
    
    colnames = ["Qubit", "Frequency", "T1", "T2", "ReadoutError", "SQError", "TQError", "Date"]
    
    data = pandas.read_csv(path, names=colnames)
    
    return data

def getSingleQubitErrorRates(data):
    '''Returns as a dictionary the single qubit error rates, as they appear on ibmq_16_melbourne. NOTE: the 
    values deviate every time the machine gets callibrated.'''
    qubits = data.Qubit.tolist()
    del qubits[0]
    qubits[0] = '0'
    for i in range(0, len(qubits)):
        qubits[i] = ("Q" + qubits[i])
    rates = data.SQError.tolist()
    del rates[0]
    rates = [float(i) for i in rates]
    sqRates = dict(zip(qubits, rates))
    
    return sqRates

def getTwoQubitErrorRates(data):
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

def getMeasureErrorRates(data):
    '''Returns as a dictionary the measurement error rates, as they appear on ibmq_16_melbourne. NOTE: the values
    deviate every time the machine gets callibrated'''
    qubits = data.Qubit.tolist()
    del qubits[0]
    qubits[0] = '0'
    for i in range(0, len(qubits)):
        qubits[i] = ("Q" + qubits[i])
    rates = data.ReadoutError.tolist()
    del rates[0]
    rates = [float(i) for i in rates]
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
            print("ERROR: incompatible decay rates - Qubit Q" + str(i) + ", T2 =", T2s[i], "and T1 =", T1s[i])
    if (c == 0):
        print(r'Checking decoherence times: all ok')

    return T1s,T2s

############ Getting gate execution times ############

def getSQGateExecutionTime(gate, backend, names):
    '''Returns the average execution time of the single-qubit type gates we are interested in.'''
    # Single qubit gates
    s = [0]*len(names)
    for i in range(0,len(names)):
        s[i] = backend.properties().gate_length(gate, [i])

    return (np.mean(s)*(10**9))

def getTQGateExecutionTime(gate, backend, graph):
    '''Returns the average execution time of the two-qubit type gates in the circuit.'''
    # Two qubit gates

    t = [0]*len(graph)
    for i in range(0,len(graph)):
        t[i] = backend.properties().gate_length('cx', graph[i])

    return (np.mean(t)*(10**9))

############ Define the noisy opeartions ############

def noisyGate(line, sqRates, tqRates):
    '''Simulates a bit-flip channel. With a randomely generated probability p an X gate is chosen,
    whereas with (1-p) the Identity is chosen. The probability of error is chosen according to the
    qubit selected each time.'''
#     sqRates = getSingleQubitErrorRates() # Dictionary containing the single qubit error rates
#     tqRates = getTwoQubitErrorRates() # Dictionary containing the two qubit error rates
    
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

def noisyMeasure(line, measRates):
    '''Simulates the noisey measurement. The probability is chosen according to the qubit being measured. The
    argument `line` is a string containing the line of code that this  '''
#     measRates = getMeasureErrorRates() # Dictionary containing the measurement error rates per qubit
    
    # Find out which qubit is being measured
    s = line.split('q')
    s = s[1].split('[')
    s = s[1].split(']')
    qubit = ("Q" + s[0])
    
    op = list(np.random.choice(["X", "I"], 1, p=[measRates[qubit], 1-measRates[qubit]]))
    
    return op

############ Define the TRC ############

def thermalRelaxationChannel(backend, T1s, T2s, graph, gates):
    '''Method that returns the thermal relaxation error quantum channel.'''

    # Instruction times (in nanoseconds)
    time_u1 = 10 # virtual gate
    time_u2 = getSQGateExecutionTime('x', backend, gates) # Average of all u2 times
    time_u3 = getSQGateExecutionTime('x', backend, gates) # Average of all u3 times
    time_cx = getTQGateExecutionTime('cx', backend, graph) # Average of all cx times
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

############ Define the method that executes a QW simulation ############

def qwNoiseExecute(iterations, thermal, backend, T1s, T2s, graph, gates):
    '''This method executes the circuit. This is necessary, since the circuit has to be generated each time for the new gates to appear'''
    counts = [{}]*iterations
    
    if (thermal == False):
        for i in range(0,iterations):
            sys.stdout.write('\r'+"Simulation count: "+str(i+1))
            circ = qwQASM()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), shots=1).result()
            counts[i] = simulate.get_counts()
    else:
        noise_thermal = thermalRelaxationChannel(backend, T1s, T2s, graph, gates)
        for i in range(0,iterations):
            sys.stdout.write('\r'+"Simulation count: "+str(i+1))
            circ = qwQASM()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), basis_gates=noise_thermal.basis_gates, 
                               noise_model=noise_thermal, shots=1).result()
            counts[i] = simulate.get_counts()
    
    return counts

############ Simulation ancillary methods ############

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
        qstate[format(i, '#08b')[2:]] = dct[i]
                        
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

############ Quantum computer experiments and data methods ############

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

############ Assist methods for GA optimization ############
def runCreateCircuit():
    '''Runs the formatted python file from the path and returns the circuit.'''
    
    %run -i "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/Create6qCircuit.py"
        
    return None

def combinedExecute(iterations, thermal, ratesList, backend, T1s, T2s, graph, gates):
    '''This method executes the combined model. This is necessary, since the circuit has to be generated each time for the new gates to appear'''
    counts = [{}]*iterations
    runCreateCircuit()
    
    # Update the error rates with the new ones from the list
    sqRates = {'Q0': ratesList[0], 'Q1': ratesList[1], 'Q2': ratesList[2], 'Q3': ratesList[3], 'Q4': ratesList[4], 'Q5': ratesList[5], 'Q6': ratesList[6], 'Q7': ratesList[7], 'Q8': ratesList[8], 'Q9': ratesList[9], 'Q10': ratesList[10], 'Q11': ratesList[11], 'Q12': ratesList[12], 'Q13': ratesList[13]}
    tqRates = {'Q0_1': ratesList[14], 'Q1_0': ratesList[14], 'Q1_2': ratesList[15], 'Q2_1': ratesList[15], 'Q2_3': ratesList[16], 'Q3_2': ratesList[16], 'Q3_4': ratesList[17], 'Q4_3': ratesList[17], 'Q4_5': ratesList[18], 'Q5_4': ratesList[18], 'Q5_6': ratesList[19], 'Q6_5': ratesList[19],  'Q7_8': ratesList[20], 'Q8_7': ratesList[20], 'Q8_9': ratesList[21], 'Q9_8': ratesList[21], 'Q9_10': ratesList[22], 'Q10_9': ratesList[22], 'Q10_11': ratesList[23], 'Q11_10': ratesList[23], 'Q11_12': ratesList[24], 'Q12_11': ratesList[24], 'Q12_13': ratesList[25], 'Q13_12': ratesList[25], 'Q1_13': ratesList[26], 'Q13_1': ratesList[26], 'Q2_12': ratesList[27], 'Q12_2': ratesList[27], 'Q3_11': ratesList[28], 'Q11_3': ratesList[28], 'Q4_10': ratesList[29], 'Q10_4': ratesList[29], 'Q5_9': ratesList[30], 'Q9_5': ratesList[30], 'Q6_8': ratesList[31], 'Q8_6': ratesList[31]}
    measRates = {'Q3': ratesList[32], 'Q6': ratesList[33], 'Q10': ratesList[34], 'Q2': ratesList[35], 'Q5': ratesList[36], 'Q7': ratesList[37],}
    
    # Execute the simulation
    if (thermal == True):
        noise_thermal = thermalRelaxationChannel(backend, T1s, T2s, graph, gates)
        for i in range(0,iterations):
            circ = createCircuit(sqRates, tqRates, measRates)
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), basis_gates=noise_thermal.basis_gates, 
                               noise_model=noise_thermal, shots=1).result()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), shots=1).result()
            counts[i] = simulate.get_counts()
    else:
        for i in range(0,iterations):
            circ = createCircuit(sqRates, tqRates, measRates)
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), shots=1).result()
            counts[i] = simulate.get_counts()
    
    return counts

def getCombinedCounts(counts, iterations):
    '''Method that formats the results of the simulation for the combined model to a dictionary.'''
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

def noisyGAGate(line, sqRates, tqRates):
    '''Simulates a bit-flip channel. With a randomely generated probability p an X gate is chosen,
    whereas with (1-p) the Identity is chosen. The probability of error is chosen according to the
    qubit selected each time.'''
    # Generate the operation according to single- or two-qubit error rates
    if (("u1" in line) or ("u2" in line) or ("u3" in line) or (".x" in line)):
        s = line.split('[')
        s = s[1].split(']')
        qubit = ("Q" + s[0])
        op = list(np.random.choice(["X", "I"], 1, p=[sqRates[qubit], 1-sqRates[qubit]]))
    elif (".cx" in line):
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

def noisyGAMeasure(line, measRates):
    '''Simulates the noisey measurement. The probability is chosen according to the qubit being measured. The
    argument `line` is a string containing the line of code that this  '''    
    # Find out which qubit is being measured
    s = line.split('q')
    s = s[1].split('[')
    s = s[1].split(']')
    qubit = ("Q" + s[0])
    
    op = list(np.random.choice(["X", "I"], 1, p=[measRates[qubit], 1-measRates[qubit]]))
    
    return op

############ Importing GA QASM codes ############

def qwGAQASM():
    '''Runs the formatted python file from the path and returns the circuit.'''
    
    %run -i "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/QASM Codes/GAFormatted4qQW.py"
        
    return circ

############ GA preparation methods ############

def getSubsystemRates(q, num_q, s_q, m_q, data):
    '''Gets the relevant error rates for the system we want. q is a list of tuples of the qubits in the system that two-qubit
    gates act on. s_q is the list of qubits of the real machine that participate (i.e Q1, Q0, Q3, etc etc)'''
    sqRates = getSingleQubitErrorRates(data) # Single-qubit error rates
    tqRates = getTwoQubitErrorRates(data) # Two-qubit error rates
    measRates = getMeasureErrorRates(data) # Measurement error rates
    sqRatesSub = [0]*(num_q)
    tqRatesSub = [0]*(len(q))
    measRatesSub = [0]*len(m_q)
    qs = [""]*(num_q)
    qp = [""]*(len(q))
    qm = [""]*len(m_q)
    
    # Prepare the single-qubit rates
    for i in range(0, num_q):
        s = ("Q" + str(s_q[i]))
        qs[i] = s
        sqRatesSub[i] = sqRates[s]
        
    # Prepare the measure rates
    for i in range(0, len(m_q)):
        s = ("Q" + str(m_q[i]))
        qm[i] = s
        measRatesSub[i] = measRates[s]
    
    # Prepare the two-qubit rates for both directions of the qubit pairs
    for i in range(0, len(q)):
        s = ("Q" + str(q[i][0]) + "_" + str(q[i][1]))
        qp[i] = s
        tqRatesSub[i] = tqRates[s]
    
    sqRatesSubDct = dict(zip(qs, sqRatesSub))
    tqRatesSubDct = dict(zip(qp, tqRatesSub))
    measRatesSubDct = dict(zip(qm, measRatesSub))
    
    return sqRatesSubDct,tqRatesSubDct,measRatesSubDct

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

def initChrom(chromosome):
    '''Function used to return the chromosome that will be used to initialize the population.'''
    chromosome = [int(chromosome[i:i+1], 2) for i in range(0, len(chromosome))]
    
    return chromosome

def decode(solution, scalar, num_rates, num_q):
    '''Decodes a solution/chromosome to its component error rates.'''
    decoded_bits = [None]*num_rates
    decoded_rates = [None]*num_rates
    
    # Decode genetic algorithm solution to error rates
    for i in range(0, num_rates):
        decoded_bits[i] = solution[i*(int(len(solution)/num_rates)):(i+1)*(int(len(solution)/num_rates))]
        
    ### Fixes for the chromosome representation ###
    for j in range(0, len(decoded_bits[0])):
        for i in range (0, num_rates):
            decoded_bits[i][j] = str(decoded_bits[i][j])
    
    for i in range(0, num_rates):
        decoded_bits[i] = "".join(decoded_bits[i])
    ###############################################
    
    for i in range(0, num_rates):
        decoded_rates[i] = int(decoded_bits[i], 2)/scalar
    
    return decoded_rates

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

############ GA running methods ############

def hd_evaluate(solution):
    '''Function that evaluates the fitness of the new generation using Hellinger distance as the fitness function.
    Arguments: scalar (int) - the scalar used to make the error rates to integers, solution (str) - the solution resukting from
    the application of the Genetic Algorithm (or could be the chromosome), num_rates (int) - the number of error rates 
    encoded in the chromosome (3 for the simple two qubit system), num_q - the number of qubits in the system. Returns: 
    fitness (float) - the fitness value, i.e theHellinger distance, that we want to minimize'''
    fitness = 0.0
    scalar = 1000000
    num_rates = 38
    num_q = 14
    avgExData = {'000000': 187, '000001': 68, '000010': 87, '000011': 27, '000100': 65, '000101': 26, '000110': 37, '000111': 16, '001000': 50, '001001': 16, '001010': 23, '001011': 10, '001100': 19, '001101': 8, '001110': 12, '001111': 9, '010000': 59, '010001': 14, '010010': 44, '010011': 15, '010100': 20, '010101': 13, '010110': 21, '010111': 5, '011000': 14, '011001': 12, '011010': 19, '011011': 7, '011100': 30, '011101': 14, '011110': 31, '011111': 15, '100000': 2, '100001': 1, '100010': 2, '100011': 0, '100100': 0, '100101': 0, '100110': 0, '100111': 0, '101000': 0, '101001': 0, '101010': 0, '101011': 0, '101100': 0, '101101': 1, '101110': 0, '101111': 0, '110000': 0, '110001': 0, '110010': 0, '110011': 0, '110100': 0, '110101': 0, '110110': 0, '110111': 0, '111000': 0, '111001': 0, '111010': 0, '111011': 0, '111100': 0, '111101': 0, '111110': 0, '111111': 1}
    thermal = True
    graph = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [7,8], [8,9], [9,10], [10,11], [11,12], [12,13], 
         [1,13], [2,12], [3,11], [4,10], [5,9], [6,8]]    
    gates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # The single-qubit gates that we are interested in
    device = provider.get_backend('ibmq_16_melbourne')
    T1s,T2s = getDecoherenceTimes(data)
        
    # Decode genetic algorithm solution to error rates
    ratesList = decode(solution, scalar, num_rates, num_q)
    
    # Run simulation with the rates
    iterations = 1000 # Probably always fixed on 1,000
    counts = combinedExecute(iterations, thermal, ratesList, device, T1s, T2s, graph, gates)
    counts = getCombinedCounts(counts, iterations)
    counts = dict(OrderedDict(sorted(counts.items())))
    
    # Format the returned distributions in a way that we can calculate the Hellinger Distance
    p,q = fixSameSupport(avgExData, counts)
    p = getProbabilities(avgExData, iterations)
    q = getProbabilities(counts, iterations)
    
    # Calculate the HD as fitness score for the GA
    fitness = hellingerDistance(p, q)
    print((str(decode(solution, scalar, num_rates, num_q)) + ", with hd ="), fitness)
    
    return fitness,

def getBest(population, scalar, num_rates, num_q):
    '''Returns the best solution generated by the optimization procedure.'''
    best_individuals = tools.selBest(population, k = 1)

    for bi in best_individuals:
        # Decode genetic algorithm solution to error rates
        best_rates = decode(bi, scalar, num_rates, num_q)
        
    return best_rates

def getIndividuals(creator, initChrom, n, chromosome):
    ''''''
    scalar = 1000000
    num_rates = 38
    num_q = 14
    individuals = []
    
    # Hardcode the IBMQ rates
    individual = initChrom(chromosome)
    b = '0' + str(int(len(individual)/num_rates)) + 'b'
    individual = creator(individual)
    individuals.append(individual)
        
    # Randomize the remaining rates
    for i in range(0, n-1):
        decodedRates = decode(initChrom(chromosome), scalar, num_rates, num_q)
        rc0 = format(abs(int((decodedRates[0] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc1 = format(abs(int((decodedRates[1] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc2 = format(abs(int((decodedRates[2] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc3 = format(abs(int((decodedRates[3] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc4 = format(abs(int((decodedRates[4] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc5 = format(abs(int((decodedRates[5] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc6 = format(abs(int((decodedRates[6] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc7 = format(abs(int((decodedRates[7] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc8 = format(abs(int((decodedRates[8] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc9 = format(abs(int((decodedRates[9] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc10 = format(abs(int((decodedRates[10] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc11 = format(abs(int((decodedRates[11] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc12 = format(abs(int((decodedRates[12] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc13 = format(abs(int((decodedRates[13] + np.random.normal(0, 0.0002, 1))*scalar)), b)
        rc14 = format(abs(int((decodedRates[14] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc15 = format(abs(int((decodedRates[15] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc16 = format(abs(int((decodedRates[16] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc17 = format(abs(int((decodedRates[17] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc18 = format(abs(int((decodedRates[18] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc19 = format(abs(int((decodedRates[19] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc20 = format(abs(int((decodedRates[20] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc21 = format(abs(int((decodedRates[21] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc22 = format(abs(int((decodedRates[22] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc23 = format(abs(int((decodedRates[23] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc24 = format(abs(int((decodedRates[24] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc25 = format(abs(int((decodedRates[25] + np.random.normal(0, 0.0.005, 1))*scalar)), b)
        rc26 = format(abs(int((decodedRates[26] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc27 = format(abs(int((decodedRates[27] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc28 = format(abs(int((decodedRates[28] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc29 = format(abs(int((decodedRates[29] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc30 = format(abs(int((decodedRates[30] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc31 = format(abs(int((decodedRates[31] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc32 = format(abs(int((decodedRates[32] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc33 = format(abs(int((decodedRates[33] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc34 = format(abs(int((decodedRates[34] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc35 = format(abs(int((decodedRates[35] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc36 = format(abs(int((decodedRates[36] + np.random.normal(0, 0.005, 1))*scalar)), b)
        rc37 = format(abs(int((decodedRates[37] + np.random.normal(0, 0.005, 1))*scalar)), b)
        randchrom = rc0 + rc1 + rc2 + rc3 + rc4 + rc5 + rc6 + rc7 + rc8 + rc9 + rc10 + rc11 + rc12 + rc13 + rc14 + rc15 + rc16 + rc17 + rc18 + rc19 + rc20 + rc21 + rc22 + rc23 + rc24 + rc25 + rc26 + rc27 + rc28 + rc29 + rc30 + rc31 + rc32 + rc33 + rc34 + rc35 + rc36 + rc37
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
    r = algorithms.eaSimple(population, toolbox, cxpb = 0.7, mutpb = 0.1, ngen = num_generations, verbose = False)
    end_time = time.time()
    print("\nTime elapsed:", end_time - start_time, "seconds.")
    
    # Get the error rates that perform the best
    bestRates = getBest(population, scalar, num_rates, num_q)
    
    return bestRates

############ Run the parameter optimization ############

def optimise():
    '''Method used to optimise the error rate parameters. All the results are shown while the method
    is run. Please allow ample time for the GA optimisation to succeed.'''
    # Required variables
    provider = IBMQ.load_account() # Loads the IBMQ account
    device = provider.get_backend('ibmq_16_melbourne') # Prefered device
    backend = Aer.get_backend("qasm_simulator") # The simulator
    iterations = 1000 # Iterations should remain constant to ensure consistency

    # Run the combined quantum noise simulator and get the distribution pre-optimization
    # Getting the noise data
    path_data = "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/Data/ibmq_16_melbourne_calibrations.csv" # Import the path where the noise data are stored
    data = machineData(path_data)
    graph = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [7,8], [8,9], [9,10], [10,11], [11,12], [12,13], 
         [1,13], [2,12], [3,11], [4,10], [5,9], [6,8]]
    gates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # The single-qubit gates that we are interested in

    sqRates = getSingleQubitErrorRates(data) # Dictionary containing the single qubit error rates
    tqRates = getTwoQubitErrorRates(data) # Dictionary containing the two qubit error rates
    measRates = getMeasureErrorRates(data) # Dictionary containing the measurement error rates per qubit
    T1s,T2s = getDecoherenceTimes(data)

    circ = qwQASM()
    nfcirc = noiseFreeqwQASM()

    # Run simulations with the UNM
    start_time = time.time()
    counts_comb = qwNoiseExecute(iterations, thermal = True, backend = device, T1s = T1s, T2s = T2s, graph = graph, gates = gates)
    end_time = time.time()
    print("\nTime elapsed:", end_time - start_time, "seconds.")
    counts_comb = getCounts(counts_comb, iterations)
    counts_comb = dict(OrderedDict(sorted(counts_comb.items())))
    print("\nCounts on noisy quantum simulator:", counts_comb)

    # Calculate the HD pre-optimization
    avgExData = {'000000': 187, '000001': 68, '000010': 87, '000011': 27, '000100': 65, '000101': 26, '000110': 37, '000111': 16, '001000': 50, '001001': 16, '001010': 23, '001011': 10, '001100': 19, '001101': 8, '001110': 12, '001111': 9, '010000': 59, '010001': 14, '010010': 44, '010011': 15, '010100': 20, '010101': 13, '010110': 21, '010111': 5, '011000': 14, '011001': 12, '011010': 19, '011011': 7, '011100': 30, '011101': 14, '011110': 31, '011111': 15, '100000': 2, '100001': 1, '100010': 2, '100011': 0, '100100': 0, '100101': 0, '100110': 0, '100111': 0, '101000': 0, '101001': 0, '101010': 0, '101011': 0, '101100': 0, '101101': 1, '101110': 0, '101111': 0, '110000': 0, '110001': 0, '110010': 0, '110011': 0, '110100': 0, '110101': 0, '110110': 0, '110111': 0, '111000': 0, '111001': 0, '111010': 0, '111011': 0, '111100': 0, '111101': 0, '111110': 0, '111111': 1} # The averaged distribution from the Quantum Computer
    
    # Get the probabilities of the **ordered** dictionaries
    p = getProbabilities(counts_comb, iterations)
    q = getProbabilities(avgExData, iterations)

    # Calculate the HD
    h_pre = hellingerDistance(p,q)
    print("The HD between the UNM and the Quantum Computer for", iterations, "iterations is:", h_pre)

   # Prepare for the GA optimization
    q_pairs = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (7,8), (8,9), (9,10), (10,11), (11,12), (12,13), 
               (1,13), (2,12), (3,11), (4,10), (5,9), (6,8)] # List of qubit pairs in ibmq_16_melbourne
    s_q = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # The qubits themselves
    m_q = [3, 6, 10, 2, 5, 7] # The qubits being measured
    num_q = len(s_q) # Number of qubits in the system
    num_rates = 38 # Number of parameters for optimization
    scalar = 1000000 # Scalar used to eliminate floating point in the encoded parameters binary representation
    thermal = True # Decide whether we want the thermal relaxation channel or not.

    # Get the error rates relevant to our system as dictionaries and lists
    sqRatesDct,tqRatesDct,measRatesDct = getSubsystemRates(q_pairs, num_q, s_q, m_q, data)

    print("Single-qubit rates with qubit information:", sqRatesDct)
    print("Two-qubit rates with qubit information::", tqRatesDct)
    print("Measurement rates with qubit information::", measRatesDct, "\n")

    sqRates = list(sqRatesDct.values())
    tqRates = list(tqRatesDct.values()) # Use set to remove duplicates
    measRates = list(measRatesDct.values())
    print("Single-qubit rates:", sqRates)
    print("Two-qubit rates:", tqRates)
    print("Measurement rates:", measRates, "\n")

    # Encode the parameters to get the chromosome bit-string
    chromosome = paramEncoding(scalar, sqRates, tqRates, measRates)
    init_chrom = decode(initChrom(chromosome), scalar, 14, num_q)
    print("Initial chromosome:", init_chrom, end = '\n')
    print("\n")

    # Evaluate the initial Hellinger distance
    init_fitness = hd_evaluate(initChrom(chromosome))
    
    # Run the Genetic Algorithm Optimization
    population_size = 20 # The number of solutions generated every time
    num_generations = 50 # The number of generations, i.e how many times the populations will reproduce
    gene_length = len(chromosome)

    bestRates = runGA(population_size, num_generations, gene_length, scalar, chromosome, num_rates, num_q)
    print("The optimized error rates are:", bestRates)
    
    # Calculate the post-optimization HD
    # Run simulations with the UNM
    start_time = time.time()
    post_counts = combinedExecute(iterations, thermal = True, ratesList = bestRates, backend = device, T1s = T1s, T2s = T2s, graph = graph, gates = gates)
    end_time = time.time()
    print("\nTime elapsed:", end_time - start_time, "seconds.")
    post_counts = getCounts(post_counts, iterations)
    post_counts = dict(OrderedDict(sorted(post_counts.items())))
    print("\nCounts on noisy quantum simulator:", post_counts)

    # Get the probabilities of the **ordered** dictionaries
    p = getProbabilities(post_counts, iterations)
    q = getProbabilities(avgExData, iterations)

    # Calculate the HD
    h_post = hellingerDistance(p,q)
    print("The HD between the UNM and the Quantum Computer post-optimization for", iterations, "iterations is:", h_post)
    
    return None