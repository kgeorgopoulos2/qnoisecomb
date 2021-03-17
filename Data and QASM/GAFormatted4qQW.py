q = QuantumRegister(11, 'q')
c = ClassicalRegister(4, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0,pi, q[7])
line = 'circ.u2(0,pi, q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[7])
	elif (dep == ['Y']):
		circ.y(q[7])
	else:
		circ.z(q[7])
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
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u2(0,pi, q[5])
line = 'circ.u2(0,pi, q[5])'
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
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u2(0,5*pi/4, q[2])
line = 'circ.u2(0,5*pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
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
circ.u2(0,pi, q[6])
line = 'circ.u2(0,pi, q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[6])
	elif (dep == ['Y']):
		circ.y(q[6])
	else:
		circ.z(q[6])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[6])
	elif (dep == ['Y']):
		circ.y(q[6])
	else:
		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[6])
	elif (dep == ['Y']):
		circ.y(q[6])
	else:
		circ.z(q[6])
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
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[7])
	elif (dep == ['Y']):
		circ.y(q[7])
	else:
		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[8])
	elif (dep == ['Y']):
		circ.y(q[8])
	else:
		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[7])
	elif (dep == ['Y']):
		circ.y(q[7])
	else:
		circ.z(q[7])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
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
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[8])
	elif (dep == ['Y']):
		circ.y(q[8])
	else:
		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[8])
	elif (dep == ['Y']):
		circ.y(q[8])
	else:
		circ.z(q[8])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.u2(0,5*pi/4, q[5])
line = 'circ.u2(0,5*pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[6])
	elif (dep == ['Y']):
		circ.y(q[6])
	else:
		circ.z(q[6])
circ.u2(0,pi, q[5])
line = 'circ.u2(0,pi, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
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
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
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
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
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
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
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
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
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
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(9*pi/4, q[2])
line = 'circ.u1(9*pi/4, q[2])'
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
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[3])
	elif (dep == ['Y']):
		circ.y(q[3])
	else:
		circ.z(q[3])
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
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
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(9*pi/4, q[1])
line = 'circ.u1(9*pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
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
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
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
circ.u1(-pi/4, q[0])
line = 'circ.u1(-pi/4, q[0])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(pi/4, q[0])
line = 'circ.u1(pi/4, q[0])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[0])
	elif (dep == ['Y']):
		circ.y(q[0])
	else:
		circ.z(q[0])
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
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
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[3])
	elif (dep == ['Y']):
		circ.y(q[3])
	else:
		circ.z(q[3])
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.barrier()
circ.u2(0,pi, q[0])
line = 'circ.u2(0,pi, q[0])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[0])
	elif (dep == ['Y']):
		circ.y(q[0])
	else:
		circ.z(q[0])
circ.u3(pi,0,pi, q[3])
line = 'circ.u3(pi,0,pi, q[3])'
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
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u2(0,5*pi/4, q[4])
line = 'circ.u2(0,5*pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[8])
	elif (dep == ['Y']):
		circ.y(q[8])
	else:
		circ.z(q[8])
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[6])
	elif (dep == ['Y']):
		circ.y(q[6])
	else:
		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[8])
	elif (dep == ['Y']):
		circ.y(q[8])
	else:
		circ.z(q[8])
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.u1(pi/4, q[10])
line = 'circ.u1(pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u1(-pi/4, q[9])
line = 'circ.u1(-pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
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
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
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
circ.u2(0,5*pi/4, q[9])
line = 'circ.u2(0,5*pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[8])
	elif (dep == ['Y']):
		circ.y(q[8])
	else:
		circ.z(q[8])
circ.u2(0,pi, q[9])
line = 'circ.u2(0,pi, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
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
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.u1(pi/4, q[5])
line = 'circ.u1(pi/4, q[5])'
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
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u1(-pi/4, q[5])
line = 'circ.u1(-pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.u2(0,5*pi/4, q[5])
line = 'circ.u2(0,5*pi/4, q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u1(-pi/4, q[10])
line = 'circ.u1(-pi/4, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u1(pi/4, q[9])
line = 'circ.u1(pi/4, q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.u2(0,pi, q[10])
line = 'circ.u2(0,pi, q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[4])
	elif (dep == ['Y']):
		circ.y(q[4])
	else:
		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[10])
	elif (dep == ['Y']):
		circ.y(q[10])
	else:
		circ.z(q[10])
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
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(9*pi/4, q[2])
line = 'circ.u1(9*pi/4, q[2])'
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
circ.u1(pi/4, q[4])
line = 'circ.u1(pi/4, q[4])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[3])
	elif (dep == ['Y']):
		circ.y(q[3])
	else:
		circ.z(q[3])
circ.u1(-pi/4, q[4])
line = 'circ.u1(-pi/4, q[4])'
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
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(9*pi/4, q[3])
line = 'circ.u1(9*pi/4, q[3])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
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
circ.u1(-pi/4, q[0])
line = 'circ.u1(-pi/4, q[0])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[5])
	elif (dep == ['Y']):
		circ.y(q[5])
	else:
		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[9])
	elif (dep == ['Y']):
		circ.y(q[9])
	else:
		circ.z(q[9])
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(-pi/4, q[1])
line = 'circ.u1(-pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
circ.u2(0,pi, q[4])
line = 'circ.u2(0,pi, q[4])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,pi, q[2])
line = 'circ.u2(0,pi, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[1])
line = 'circ.u2(0,5*pi/4, q[1])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u2(0,pi, q[3])
line = 'circ.u2(0,pi, q[3])'
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
circ.u1(-pi/4, q[3])
line = 'circ.u1(-pi/4, q[3])'
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
circ.u1(pi/4, q[2])
line = 'circ.u1(pi/4, q[2])'
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
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u1(pi/4, q[3])
line = 'circ.u1(pi/4, q[3])'
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
circ.u1(pi/4, q[1])
line = 'circ.u1(pi/4, q[1])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[1])
	elif (dep == ['Y']):
		circ.y(q[1])
	else:
		circ.z(q[1])
circ.u1(-pi/4, q[2])
line = 'circ.u1(-pi/4, q[2])'
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
circ.u2(0,5*pi/4, q[3])
line = 'circ.u2(0,5*pi/4, q[3])'
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
circ.u3(pi,0,pi, q[2])
line = 'circ.u3(pi,0,pi, q[2])'
op = noisyGAGate(line, sqRates, tqRates)
if (op == ['X']):
	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))
	if (dep == ['X']):
		circ.x(q[2])
	elif (dep == ['Y']):
		circ.y(q[2])
	else:
		circ.z(q[2])
circ.barrier()
line = 'circ.measure(q[4], c[0])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
	circ.x(q[4])
circ.measure(q[4], c[0])
line = 'circ.measure(q[1], c[1])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
	circ.x(q[1])
circ.measure(q[1], c[1])
line = 'circ.measure(q[3], c[2])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
	circ.x(q[3])
circ.measure(q[3], c[2])
line = 'circ.measure(q[8], c[3])'
op = noisyGAMeasure(line, measRates)
if (op == ['X']):
	circ.x(q[8])
circ.measure(q[8], c[3])