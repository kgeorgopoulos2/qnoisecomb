q = QuantumRegister(15, 'q')
c = ClassicalRegister(6, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.barrier()
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u2(0.0,3.141592653589793, q[10])
line = 'circ.u2(0.0,3.141592653589793, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u2(0.0,3.141592653589793, q[6])
line = 'circ.u2(0.0,3.141592653589793, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.9269908169872414, q[4])
line = 'circ.u2(0.0,3.9269908169872414, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.141592653589793, q[7])
line = 'circ.u2(0.0,3.141592653589793, q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u2(0.0,3.141592653589793, q[8])
line = 'circ.u2(0.0,3.141592653589793, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u2(0.0,3.141592653589793, q[9])
line = 'circ.u2(0.0,3.141592653589793, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[1])
line = 'circ.cx(q[13],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(-0.7853981633974483, q[8])
line = 'circ.u1(-0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u1(-0.7853981633974483, q[7])
line = 'circ.u1(-0.7853981633974483, q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(0.7853981633974483, q[8])
line = 'circ.u1(0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(0.7853981633974483, q[7])
line = 'circ.u1(0.7853981633974483, q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u1(-0.7853981633974483, q[8])
line = 'circ.u1(-0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u2(0.0,3.9269908169872414, q[7])
line = 'circ.u2(0.0,3.9269908169872414, q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(-0.7853981633974483, q[8])
line = 'circ.u1(-0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.cx(q[7],q[8])
line = 'circ.cx(q[7],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u2(0.0,3.141592653589793, q[9])
line = 'circ.u2(0.0,3.141592653589793, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.141592653589793, q[10])
line = 'circ.u2(0.0,3.141592653589793, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(0.7853981633974483, q[8])
line = 'circ.u1(0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(-0.7853981633974483, q[8])
line = 'circ.u1(-0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(7.0685834705770345, q[8])
line = 'circ.u1(7.0685834705770345, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[6])
line = 'circ.u1(0.7853981633974483, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u2(0.0,3.141592653589793, q[5])
line = 'circ.u2(0.0,3.141592653589793, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u2(0.0,3.141592653589793, q[5])
line = 'circ.u2(0.0,3.141592653589793, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(7.0685834705770345, q[10])
line = 'circ.u1(7.0685834705770345, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(0.7853981633974483, q[1])
line = 'circ.u1(0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(7.0685834705770345, q[1])
line = 'circ.u1(7.0685834705770345, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(-0.7853981633974483, q[1])
line = 'circ.u1(-0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(0.7853981633974483, q[1])
line = 'circ.u1(0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(-0.7853981633974483, q[1])
line = 'circ.u1(-0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u2(0.0,3.9269908169872414, q[1])
line = 'circ.u2(0.0,3.9269908169872414, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(7.0685834705770345, q[9])
line = 'circ.u1(7.0685834705770345, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u2(0.0,3.9269908169872414, q[5])
line = 'circ.u2(0.0,3.9269908169872414, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[10])
line = 'circ.u2(0.0,3.9269908169872414, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u2(0.0,3.141592653589793, q[9])
line = 'circ.u2(0.0,3.141592653589793, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(7.0685834705770345, q[10])
line = 'circ.u1(7.0685834705770345, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(7.0685834705770345, q[12])
line = 'circ.u1(7.0685834705770345, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(7.0685834705770345, q[1])
line = 'circ.u1(7.0685834705770345, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(-0.7853981633974483, q[1])
line = 'circ.u1(-0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(0.7853981633974483, q[1])
line = 'circ.u1(0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(-0.7853981633974483, q[1])
line = 'circ.u1(-0.7853981633974483, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u2(0.0,3.9269908169872414, q[1])
line = 'circ.u2(0.0,3.9269908169872414, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.u1(-0.7853981633974483, q[13])
line = 'circ.u1(-0.7853981633974483, q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[12])
line = 'circ.u1(0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[1])
line = 'circ.cx(q[13],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[13])
line = 'circ.u1(0.7853981633974483, q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.u1(0.7853981633974483, q[12])
line = 'circ.u1(0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[13])
line = 'circ.u1(-0.7853981633974483, q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(7.0685834705770345, q[10])
line = 'circ.u1(7.0685834705770345, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[12])
line = 'circ.u1(0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(7.0685834705770345, q[11])
line = 'circ.u1(7.0685834705770345, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[5])
line = 'circ.u2(0.0,3.9269908169872414, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.9269908169872414, q[4])
line = 'circ.u2(0.0,3.9269908169872414, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[5])
line = 'circ.u2(0.0,3.9269908169872414, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.barrier()
circ.u3(3.141592653589793,0.0,3.141592653589793, q[10])
line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.141592653589793, q[12])
line = 'circ.u2(0.0,3.141592653589793, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[13])
line = 'circ.cx(q[12],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[1])
line = 'circ.cx(q[13],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.141592653589793, q[5])
line = 'circ.u2(0.0,3.141592653589793, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u2(0.0,3.141592653589793, q[6])
line = 'circ.u2(0.0,3.141592653589793, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.u2(0.0,3.141592653589793, q[9])
line = 'circ.u2(0.0,3.141592653589793, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u2(0.0,3.9269908169872414, q[1])
line = 'circ.u2(0.0,3.9269908169872414, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[1])
line = 'circ.cx(q[13],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u1(-0.7853981633974483, q[8])
line = 'circ.u1(-0.7853981633974483, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[7])
line = 'circ.cx(q[8],q[7])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[7])	elif (dep == ['Y']):		circ.y(q[7])	else:		circ.z(q[7])
circ.u2(0.0,3.141592653589793, q[8])
line = 'circ.u2(0.0,3.141592653589793, q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.141592653589793, q[10])
line = 'circ.u2(0.0,3.141592653589793, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[12])
line = 'circ.u1(0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(7.0685834705770345, q[11])
line = 'circ.u1(7.0685834705770345, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[13])
line = 'circ.u1(0.7853981633974483, q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u2(0.0,3.141592653589793, q[12])
line = 'circ.u2(0.0,3.141592653589793, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(7.0685834705770345, q[3])
line = 'circ.u1(7.0685834705770345, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(7.0685834705770345, q[5])
line = 'circ.u1(7.0685834705770345, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[12])
line = 'circ.u1(0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[13])
line = 'circ.u1(0.7853981633974483, q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(7.0685834705770345, q[9])
line = 'circ.u1(7.0685834705770345, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[9])
line = 'circ.cx(q[8],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[9])
line = 'circ.u1(0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[8])
line = 'circ.cx(q[9],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.u2(0.0,3.141592653589793, q[9])
line = 'circ.u2(0.0,3.141592653589793, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[12])
line = 'circ.u1(0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(7.0685834705770345, q[11])
line = 'circ.u1(7.0685834705770345, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[13])
line = 'circ.u1(0.7853981633974483, q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[13],q[12])
line = 'circ.cx(q[13],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.u2(0.0,3.141592653589793, q[12])
line = 'circ.u2(0.0,3.141592653589793, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[13],q[1])
line = 'circ.cx(q[13],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[13])
line = 'circ.cx(q[1],q[13])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[13])	elif (dep == ['Y']):		circ.y(q[13])	else:		circ.z(q[13])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[11])
line = 'circ.cx(q[12],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(7.0685834705770345, q[10])
line = 'circ.u1(7.0685834705770345, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(7.0685834705770345, q[5])
line = 'circ.u1(7.0685834705770345, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[11])
line = 'circ.u2(0.0,3.9269908169872414, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[12])
line = 'circ.cx(q[11],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(-0.7853981633974483, q[12])
line = 'circ.u1(-0.7853981633974483, q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.cx(q[12],q[2])
line = 'circ.cx(q[12],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[12])
line = 'circ.cx(q[2],q[12])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[12])	elif (dep == ['Y']):		circ.y(q[12])	else:		circ.z(q[12])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.u2(0.0,3.141592653589793, q[2])
line = 'circ.u2(0.0,3.141592653589793, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[2])
line = 'circ.u1(-0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[2])
line = 'circ.u1(0.7853981633974483, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.9269908169872414, q[2])
line = 'circ.u2(0.0,3.9269908169872414, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.141592653589793, q[3])
line = 'circ.u2(0.0,3.141592653589793, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[8],q[6])
line = 'circ.cx(q[8],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[8])
line = 'circ.cx(q[6],q[8])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[8])	elif (dep == ['Y']):		circ.y(q[8])	else:		circ.z(q[8])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[10])
line = 'circ.u1(-0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[11])
line = 'circ.u1(0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(-0.7853981633974483, q[11])
line = 'circ.u1(-0.7853981633974483, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[10],q[11])
line = 'circ.cx(q[10],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(7.0685834705770345, q[5])
line = 'circ.u1(7.0685834705770345, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u2(0.0,3.9269908169872414, q[5])
line = 'circ.u2(0.0,3.9269908169872414, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(7.0685834705770345, q[9])
line = 'circ.u1(7.0685834705770345, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.u1(-0.7853981633974483, q[9])
line = 'circ.u1(-0.7853981633974483, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[5])
line = 'circ.u1(-0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[9])
line = 'circ.cx(q[10],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[11],q[10])
line = 'circ.cx(q[11],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u2(0.0,3.141592653589793, q[11])
line = 'circ.u2(0.0,3.141592653589793, q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[3])
line = 'circ.u1(-0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[3])
line = 'circ.u2(0.0,3.9269908169872414, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[11],q[3])
line = 'circ.cx(q[11],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[11])
line = 'circ.cx(q[3],q[11])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[11])	elif (dep == ['Y']):		circ.y(q[11])	else:		circ.z(q[11])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[9],q[10])
line = 'circ.cx(q[9],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.u1(0.7853981633974483, q[10])
line = 'circ.u1(0.7853981633974483, q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[10],q[4])
line = 'circ.cx(q[10],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[9],q[5])
line = 'circ.cx(q[9],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[9])
line = 'circ.cx(q[5],q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.141592653589793, q[4])
line = 'circ.u2(0.0,3.141592653589793, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[4])
line = 'circ.u1(0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[5])
line = 'circ.u1(0.7853981633974483, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u1(0.7853981633974483, q[3])
line = 'circ.u1(0.7853981633974483, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.u1(-0.7853981633974483, q[4])
line = 'circ.u1(-0.7853981633974483, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[5])
line = 'circ.u2(0.0,3.9269908169872414, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[4],q[10])
line = 'circ.cx(q[4],q[10])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[10])	elif (dep == ['Y']):		circ.y(q[10])	else:		circ.z(q[10])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[6])
line = 'circ.cx(q[5],q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[6])	elif (dep == ['Y']):		circ.y(q[6])	else:		circ.z(q[6])
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.u3(3.141592653589793,0.0,3.141592653589793, q[4])
line = 'circ.u3(3.141592653589793,0.0,3.141592653589793, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.u2(0.0,3.9269908169872414, q[9])
line = 'circ.u2(0.0,3.9269908169872414, q[9])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[9])	elif (dep == ['Y']):		circ.y(q[9])	else:		circ.z(q[9])
circ.barrier()
line = 'circ.measure(q[3], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[3])
circ.measure(q[3], c[0])
line = 'circ.measure(q[6], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[6])
circ.measure(q[6], c[1])
line = 'circ.measure(q[10], c[2])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[10])
circ.measure(q[10], c[2])
line = 'circ.measure(q[2], c[3])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[2])
circ.measure(q[2], c[3])
line = 'circ.measure(q[5], c[4])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[5])
circ.measure(q[5], c[4])
line = 'circ.measure(q[7], c[5])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[7])
circ.measure(q[7], c[5])