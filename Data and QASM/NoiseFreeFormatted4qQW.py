q = QuantumRegister(10, 'q')
c = ClassicalRegister(4, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0,pi, q[7])
circ.barrier()
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[1])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,pi, q[5])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u2(0,5*pi/4, q[2])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u2(0,pi, q[6])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[4],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[8],q[7])
circ.cx(q[7],q[8])
circ.cx(q[8],q[7])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[8],q[9])
circ.u1(pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.u1(pi/4, q[4])
circ.u1(-pi/4, q[5])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[9],q[5])
circ.u2(0,5*pi/4, q[5])
circ.cx(q[5],q[6])
circ.u2(0,pi, q[5])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[10])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[4],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[9],q[5])
circ.u1(pi/4, q[5])
circ.cx(q[4],q[5])
circ.u1(pi/4, q[4])
circ.u1(-pi/4, q[5])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[5],q[4])
circ.u1(-pi/4, q[4])
circ.u1(pi/4, q[5])
circ.cx(q[5],q[4])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u1(9*pi/4, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u1(9*pi/4, q[1])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.u1(-pi/4, q[1])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.u1(pi/4, q[1])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.u1(-pi/4, q[1])
circ.u1(pi/4, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.u2(0,5*pi/4, q[1])
circ.cx(q[1],q[0])
circ.u1(-pi/4, q[0])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.u1(pi/4, q[0])
circ.u1(-pi/4, q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.u1(-pi/4, q[1])
circ.u1(pi/4, q[2])
circ.cx(q[2],q[1])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.u2(0,pi, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[3],q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[2])
circ.u2(0,pi, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u2(0,pi, q[2])
circ.cx(q[1],q[2])
circ.u1(-pi/4, q[2])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[3],q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[1])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.u1(pi/4, q[3])
circ.u2(0,5*pi/4, q[9])
circ.barrier()
circ.u2(0,pi, q[0])
circ.u3(pi,0,pi, q[3])
circ.cx(q[3],q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[3],q[2])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u2(0,5*pi/4, q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[6],q[8])
circ.cx(q[8],q[6])
circ.cx(q[6],q[8])
circ.u2(0,pi, q[9])
circ.cx(q[10],q[9])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.u1(pi/4, q[9])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[10])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[5],q[4])
circ.u1(-pi/4, q[4])
circ.u1(pi/4, q[5])
circ.cx(q[5],q[4])
circ.u2(0,5*pi/4, q[9])
circ.cx(q[9],q[8])
circ.u2(0,pi, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[9],q[5])
circ.u1(pi/4, q[5])
circ.cx(q[4],q[5])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[5])
circ.cx(q[9],q[5])
circ.u2(0,5*pi/4, q[5])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[10])
circ.u2(0,pi, q[10])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[3],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u1(9*pi/4, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(9*pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[1])
circ.cx(q[1],q[0])
circ.u1(-pi/4, q[0])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.u1(-pi/4, q[1])
circ.u1(pi/4, q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[5])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u2(0,pi, q[2])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.u2(0,pi, q[3])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.u1(pi/4, q[1])
circ.u1(-pi/4, q[2])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u3(pi,0,pi, q[2])
circ.barrier()
circ.measure(q[4], c[0])
circ.measure(q[1], c[1])
circ.measure(q[3], c[2])
circ.measure(q[8], c[3])