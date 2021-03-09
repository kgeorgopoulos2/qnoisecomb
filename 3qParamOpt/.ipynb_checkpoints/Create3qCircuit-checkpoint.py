# Import libraries
import numpy as np
import sys
from numpy import pi as pi

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
    q = QuantumRegister(6, 'q')
    c = ClassicalRegister(3, 'c')
    circ = QuantumCircuit(q, c)
    circ.u2(0.0,3.141592653589793, q[5])
    line = 'circ.u2(0.0,3.141592653589793, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.barrier()
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
    circ.u2(0.0,3.141592653589793, q[3])
    line = 'circ.u2(0.0,3.141592653589793, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
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
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.u2(0.0,3.9269908169872414, q[3])
    line = 'circ.u2(0.0,3.9269908169872414, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u2(0.0,3.141592653589793, q[4])
    line = 'circ.u2(0.0,3.141592653589793, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[4])
    line = 'circ.u1(0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u2(0.0,3.9269908169872414, q[3])
    line = 'circ.u2(0.0,3.9269908169872414, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[5])
    line = 'circ.u1(0.7853981633974483, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[4])
    line = 'circ.u1(0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u2(0.0,3.9269908169872414, q[3])
    line = 'circ.u2(0.0,3.9269908169872414, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[5])
    line = 'circ.u1(0.7853981633974483, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u2(0.0,3.141592653589793, q[4])
    line = 'circ.u2(0.0,3.141592653589793, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
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
    circ.u2(0.0,3.9269908169872414, q[1])
    line = 'circ.u2(0.0,3.9269908169872414, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u2(0.0,3.141592653589793, q[3])
    line = 'circ.u2(0.0,3.141592653589793, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[4])
    line = 'circ.u1(0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u2(0.0,3.9269908169872414, q[3])
    line = 'circ.u2(0.0,3.9269908169872414, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[5])
    line = 'circ.u1(0.7853981633974483, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.barrier()
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
    circ.u3(3.141592653589793,0.0,3.141592653589793, q[5])
    line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
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
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
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
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.u2(0.0,3.9269908169872414, q[4])
    line = 'circ.u2(0.0,3.9269908169872414, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[4],q[5])
    line = 'circ.cx(q[4],q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[5])
    line = 'circ.cx(q[4],q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u2(0.0,3.9269908169872414, q[3])
    line = 'circ.u2(0.0,3.9269908169872414, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(0.7853981633974483, q[5])
    line = 'circ.u1(0.7853981633974483, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[4],q[5])
    line = 'circ.cx(q[4],q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.u1(0.7853981633974483, q[4])
    line = 'circ.u1(0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(-0.7853981633974483, q[5])
    line = 'circ.u1(-0.7853981633974483, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[5])
    line = 'circ.cx(q[4],q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[4])
    line = 'circ.u1(0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[4])
    line = 'circ.u1(-0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[5])
    line = 'circ.cx(q[4],q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[5],q[4])
    line = 'circ.cx(q[5],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[5])
    line = 'circ.cx(q[4],q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(-0.7853981633974483, q[3])
    line = 'circ.u1(-0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u1(0.7853981633974483, q[4])
    line = 'circ.u1(0.7853981633974483, q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u2(0.0,3.141592653589793, q[3])
    line = 'circ.u2(0.0,3.141592653589793, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
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
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.cx(q[2],q[3])
    line = 'circ.cx(q[2],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
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
    circ.u2(0.0,3.9269908169872414, q[3])
    line = 'circ.u2(0.0,3.9269908169872414, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[4],q[3])
    line = 'circ.cx(q[4],q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[4])
    line = 'circ.cx(q[3],q[4])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[4])
        elif (dep == ['Y']):
            circ.y(q[4])
        else:
            circ.z(q[4])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
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
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
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
    circ.u2(0.0,3.9269908169872414, q[1])
    line = 'circ.u2(0.0,3.9269908169872414, q[1])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[1])
        elif (dep == ['Y']):
            circ.y(q[1])
        else:
            circ.z(q[1])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
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
    circ.u1(0.7853981633974483, q[3])
    line = 'circ.u1(0.7853981633974483, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
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
    circ.cx(q[3],q[2])
    line = 'circ.cx(q[3],q[2])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[2])
        elif (dep == ['Y']):
            circ.y(q[2])
        else:
            circ.z(q[2])
    circ.u3(3.141592653589793,0.0,3.141592653589793, q[3])
    line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[3])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[3])
        elif (dep == ['Y']):
            circ.y(q[3])
        else:
            circ.z(q[3])
    circ.u2(0.0,3.9269908169872414, q[5])
    line = 'circ.u2(0.0,3.9269908169872414, q[5])'
    op = noisyGAGate(line, sqRates, tqRates)
    if (op == ['X']):
        dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
        if (dep == ['X']):
            circ.x(q[5])
        elif (dep == ['Y']):
            circ.y(q[5])
        else:
            circ.z(q[5])
    circ.barrier()
    line = 'circ.measure(q[1], c[0])'
    op = noisyGAMeasure(line, measRates)
    if (op == ['X']):
        circ.x(q[1])
    circ.measure(q[1], c[0])
    line = 'circ.measure(q[2], c[1])'
    op = noisyGAMeasure(line, measRates)
    if (op == ['X']):
        circ.x(q[2])
    circ.measure(q[2], c[1])
    line = 'circ.measure(q[0], c[2])'
    op = noisyGAMeasure(line, measRates)
    if (op == ['X']):
        circ.x(q[0])
    circ.measure(q[0], c[2])
    
    return circ