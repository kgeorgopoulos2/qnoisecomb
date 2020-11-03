# Import libraries
import numpy as np
import sys

# Import Qiskit
from qiskit import Aer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.providers.aer import QasmSimulator
from qiskit.providers.aer.noise.errors import thermal_relaxation_error, pauli_error
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer import noise

import CreateCircuit

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

def machineData(path):
    '''Imports the error rates of the machine as the downloaded csv file. path - the path to the csv file, including
    the name of the csv file and ".csv".'''
    
    colnames = ["Qubit", "T1", "T2", "Frequency", "ReadoutError", "SQError", "TQError", "Date"]
    
    data = pandas.read_csv(path, names=colnames)
    
    return data

def thermalRelaxationError():
    '''Method that returns the thermal relaxation error quantum channel.'''
    # T1 and T2
    data = machineData(path)
    T1s,T2s = getDecoherenceTimes()
    
    # Gaussian pulse times, aka execution time, for CNOT gates (in nanoseconds).
    TCXs = {'Q1_0':239,'Q1_2':174,'Q2_3':261,'Q4_3':266,'Q5_4':300,'Q5_6':300,'Q7_8':220,'Q9_8':434,'Q9_10':300,'Q11_10':261,
            'Q11_12':261,'Q13_12':300,'Q13_1':652,'Q12_2':1043,'Q11_3':286,'Q4_10':261,'Q5_9':348,'Q6_8':348}

    # Instruction times (in nanoseconds)
    time_u1 = 10 # virtual gate
    time_u2 = 50 # (single X90 pulse)
    time_u3 = 100 # (two X90 pulses)
    time_cx = 239 # Only interested in 'Q1_0'
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

def combinedExecute(iterations, thermal, num_q, ratesList):
    '''This method executes the combined model. This is necessary, since the circuit has to be generated each time for the new gates to appear'''
    counts = [{}]*iterations
    
    # Update the error rates with the new ones from the list
    sqRates = {'Q0': ratesList[0], 'Q1': ratesList[1], 'Q2': ratesList[2]}
    tqRates = {'Q0_1': ratesList[3], 'Q1_0': ratesList[3], 'Q1_2': ratesList[4], 'Q2_1': ratesList[4]}
    measRates = {'Q0': ratesList[5], 'Q1': ratesList[6], 'Q2': ratesList[7]}
    
    # Execute the simulation
    if (thermal == True):
        noise_thermal = thermalRelaxationError()
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