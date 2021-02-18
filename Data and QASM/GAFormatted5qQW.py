q = QuantumRegister(12, 'q')
c = ClassicalRegister(5, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[5])
line = 'circ.u2(0,pi, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[6])
line = 'circ.u2(0,pi, q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[2])
line = 'circ.u2(0,5*pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[7])
line = 'circ.u2(0,pi, q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[12])
line = 'circ.u1(pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[8])
line = 'circ.u2(0,5*pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[8])
line = 'circ.u1(-pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[8])
line = 'circ.u1(pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[10])
line = 'circ.u2(0,5*pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[8])
line = 'circ.u1(-pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[11])
line = 'circ.u1(9*pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[9])
line = 'circ.u1(9*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[12])
line = 'circ.u1(pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[3])
line = 'circ.u1(9*pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[12])
line = 'circ.u1(pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[11])
line = 'circ.u2(0,5*pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[12])
line = 'circ.u1(-pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[8])
line = 'circ.u2(0,5*pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[8])
line = 'circ.u1(pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[8])
line = 'circ.u1(-pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[6])
line = 'circ.u1(pi/4, q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[8])
line = 'circ.u1(-pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[12])
line = 'circ.u1(pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[3])
line = 'circ.u1(9*pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[11])
line = 'circ.u2(0,5*pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[12])
line = 'circ.u1(pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[9])
line = 'circ.u1(9*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[10])
line = 'circ.u2(0,5*pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[8])
line = 'circ.u1(pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[10])
line = 'circ.u2(0,5*pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[8])
line = 'circ.u1(-pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[10])
line = 'circ.u2(0,5*pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
circ.u3(pi,0,pi, q[10])
line = 'circ.u3(pi,0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[5])
line = 'circ.u2(0,5*pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[8])
line = 'circ.u1(-pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[6])
line = 'circ.u1(pi/4, q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[6])
line = 'circ.u2(0,5*pi/4, q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[11])
line = 'circ.u2(0,pi, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[4])
line = 'circ.u1(9*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[12])
line = 'circ.u1(-pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[3])
line = 'circ.u1(9*pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[2])
line = 'circ.u2(0,5*pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[9])
line = 'circ.u1(9*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[5])
line = 'circ.u2(0,5*pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[8])
line = 'circ.u2(0,5*pi/4, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[8])
line = 'circ.u2(0,pi, q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[11])
line = 'circ.u2(0,5*pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[10])
line = 'circ.u1(9*pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[12])
line = 'circ.u1(pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(9*pi/4, q[3])
line = 'circ.u1(9*pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[12])
line = 'circ.u1(-pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[12])
line = 'circ.u2(0,5*pi/4, q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[11])
line = 'circ.u1(-pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[11])
line = 'circ.u2(0,5*pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(pi/4, q[11])
line = 'circ.u1(pi/4, q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0,5*pi/4, q[2])
line = 'circ.u2(0,5*pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u3(pi,0,pi, q[4])
line = 'circ.u3(pi,0,pi, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
line = 'circ.measure(q[11], c[0])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[11], c[0])
line = 'circ.measure(q[2], c[1])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[2], c[1])
line = 'circ.measure(q[3], c[2])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[3], c[2])
line = 'circ.measure(q[5], c[3])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[5], c[3])
line = 'circ.measure(q[6], c[4])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[6], c[4])