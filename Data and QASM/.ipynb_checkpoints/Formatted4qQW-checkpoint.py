q = QuantumRegister(11, 'q')
c = ClassicalRegister(4, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0,pi, q[7])
line = 'circ.u2(0,pi, q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[5])
line = 'circ.u2(0,pi, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[2])
line = 'circ.u2(0,5*pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[6])
line = 'circ.u2(0,pi, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[5])
line = 'circ.u2(0,5*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[5])
line = 'circ.u2(0,pi, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[2])
line = 'circ.u1(9*pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[1])
line = 'circ.u1(9*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[0])
line = 'circ.u1(-pi/4, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[0])
line = 'circ.u1(pi/4, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
circ.u2(0,pi, q[0])
line = 'circ.u2(0,pi, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u3(pi,0,pi, q[3])
line = 'circ.u3(pi,0,pi, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[5])
line = 'circ.u2(0,5*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[2])
line = 'circ.u1(9*pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[3])
line = 'circ.u1(9*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[0])
line = 'circ.u1(-pi/4, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u3(pi,0,pi, q[2])
line = 'circ.u3(pi,0,pi, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
line = 'circ.measure(q[4], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[4], c[0])
line = 'circ.measure(q[1], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[1], c[1])
line = 'circ.measure(q[3], c[2])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[3], c[2])
line = 'circ.measure(q[8], c[3])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[8], c[3])