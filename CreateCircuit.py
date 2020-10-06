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

# Probably call the code from the .py file within the following method, instead of copy-pasting it.

def createCircuit(sqRates, tqRates, measRates):
    ''''''
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(2, 'c')
    circ = QuantumCircuit(q, c)
    
    circ.u2(0.0,3.141592653589793, q[1])
    line = 'circ.u2(0.0,3.141592653589793, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u2(0.0,3.141592653589793, q[2])
    line = 'circ.u2(0.0,3.141592653589793, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(-0.7853981633974483, q[1])
    line = 'circ.u1(-0.7853981633974483, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(0.7853981633974483, q[1])
    line = 'circ.u1(0.7853981633974483, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(-0.7853981633974483, q[1])
    line = 'circ.u1(-0.7853981633974483, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(0.7853981633974483, q[2])
    line = 'circ.u1(0.7853981633974483, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(0.7853981633974483, q[0])
    line = 'circ.u1(0.7853981633974483, q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.u1(-0.7853981633974483, q[1])
    line = 'circ.u1(-0.7853981633974483, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[0])
    line = 'circ.cx(q[1],q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.u3(3.141592653589793,0.0,3.141592653589793, q[1])
    line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[0])
    line = 'circ.cx(q[1],q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.u2(0.0,3.9269908169872414, q[2])
    line = 'circ.u2(0.0,3.9269908169872414, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.u2(0.0,3.141592653589793, q[2])
    line = 'circ.u2(0.0,3.141592653589793, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[0])
    line = 'circ.cx(q[1],q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(-0.7853981633974483, q[2])
    line = 'circ.u1(-0.7853981633974483, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.u1(0.7853981633974483, q[2])
    line = 'circ.u1(0.7853981633974483, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(0.7853981633974483, q[0])
    line = 'circ.u1(0.7853981633974483, q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.u1(-0.7853981633974483, q[1])
    line = 'circ.u1(-0.7853981633974483, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[0])
    line = 'circ.cx(q[1],q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.cx(q[0],q[1])
    line = 'circ.cx(q[0],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u2(0.0,3.9269908169872414, q[0])
    line = 'circ.u2(0.0,3.9269908169872414, q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(-0.7853981633974483, q[1])
    line = 'circ.u1(-0.7853981633974483, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(0.7853981633974483, q[2])
    line = 'circ.u1(0.7853981633974483, q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[1])
    line = 'circ.cx(q[2],q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[1],q[0])
    line = 'circ.cx(q[1],q[0])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[0])
        elif (dep == ['Y']):
            circ.y(q[0])
        else:
            circ.z(q[0])
    circ.cx(q[1],q[2])
    line = 'circ.cx(q[1],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.u3(3.141592653589793,0.0,3.141592653589793, q[1])
    line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.barrier()
    line = 'circ.measure(q[2], c[0])'
    op = noisyGAMeasure(line, measRates)
    if (op == ['X']):
        circ.x(q[2])
    circ.measure(q[2], c[0])
    line = 'circ.measure(q[0], c[1])'
    op = noisyGAMeasure(line, measRates)
    if (op == ['X']):
        circ.x(q[0])
    circ.measure(q[0], c[1])
    
    return circ