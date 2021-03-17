q = QuantumRegister(6, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0.0,3.141592653589793, q[5])
line = 'circ.u2(0.0,3.141592653589793, q[5])'
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
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
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
circ.u1(0.7853981633974483, q[1])
line = 'circ.u1(0.7853981633974483, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
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
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
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
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.u2(0.0,3.141592653589793, q[2])
line = 'circ.u2(0.0,3.141592653589793, q[2])'
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
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
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
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
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
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
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
circ.u2(0.0,3.9269908169872414, q[1])
line = 'circ.u2(0.0,3.9269908169872414, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
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
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
circ.u2(0.0,3.141592653589793, q[1])
line = 'circ.u2(0.0,3.141592653589793, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.141592653589793, q[2])
line = 'circ.u2(0.0,3.141592653589793, q[2])'
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
circ.u3(3.141592653589793,0.0,3.141592653589793, q[5])
line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
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
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
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
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
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
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.u2(0.0,3.9269908169872414, q[4])
line = 'circ.u2(0.0,3.9269908169872414, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
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
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
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
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.u2(0.0,3.141592653589793, q[2])
line = 'circ.u2(0.0,3.141592653589793, q[2])'
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
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
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
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
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
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
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
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
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
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[1])
line = 'circ.u1(0.7853981633974483, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[1])
line = 'circ.u1(-0.7853981633974483, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.141592653589793, q[1])
line = 'circ.u2(0.0,3.141592653589793, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[1])
line = 'circ.u1(-0.7853981633974483, q[1])'
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
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
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
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[1])
line = 'circ.u1(0.7853981633974483, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
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
circ.u2(0.0,3.9269908169872414, q[1])
line = 'circ.u2(0.0,3.9269908169872414, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
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
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u3(3.141592653589793,0.0,3.141592653589793, q[3])
line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.u2(0.0,3.9269908169872414, q[5])
line = 'circ.u2(0.0,3.9269908169872414, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
line = 'circ.measure(q[1], c[0])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[1], c[0])
line = 'circ.measure(q[2], c[1])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[2], c[1])
line = 'circ.measure(q[0], c[2])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[0], c[2])