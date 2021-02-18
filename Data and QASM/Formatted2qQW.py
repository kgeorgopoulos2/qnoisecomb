q = QuantumRegister(4, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0,pi, q[1])
line = 'circ.u2(0,pi, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
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
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
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
circ.barrier()
circ.u3(pi,0,pi, q[3])
line = 'circ.u3(pi,0,pi, q[3])'
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
circ.u2(0,pi, q[1])
line = 'circ.u2(0,pi, q[1])'
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
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
line = 'circ.measure(q[1], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[1], c[0])
line = 'circ.measure(q[3], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[3], c[1])