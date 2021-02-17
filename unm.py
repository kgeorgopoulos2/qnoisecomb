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
    
    %run -i "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/QASM Codes/Formatted2qQW.py"
        
    return circ

def noiseFreeqwQASM():
    '''Runs the formatted, noise-free python file from the path and returns the circuit.'''
    
    %run -i "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Unified Noise Model/QASM Codes/NoiseFreeFormatted2qQW.py"
    
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
    
    graph = [[0,1], [1,2], [2,3]] # The two-qubit gates that we are interested in
    names = [0, 1, 2, 3] # The single-qubit gates that we are interested in

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

def runUNM(path_data, graph, gates):
    '''Runs the Unified Noise Model. path_data: the location where the .csv file from the machine calibrations resides; graph: the two-qubit 
    pairs that participate in the quantum circuit; gates: the qubits that participate in the quantum circuit.'''
    # Getting the noise data
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
    
    return None