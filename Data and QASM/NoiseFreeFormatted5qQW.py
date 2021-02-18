q = QuantumRegister(12, 'q')
c = ClassicalRegister(5, 'c')
circ = QuantumCircuit(q, c)
circ.u2(0,pi, q[9])
circ.barrier()
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
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
circ.cx(q[2],q[3])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
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
circ.u2(0,5*pi/4, q[4])
circ.u2(0,pi, q[6])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[4],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[5],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u2(0,5*pi/4, q[2])
circ.u1(pi/4, q[5])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.u2(0,pi, q[7])
circ.u2(0,pi, q[8])
circ.cx(q[8],q[7])
circ.cx(q[7],q[8])
circ.cx(q[8],q[7])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[7])
circ.cx(q[7],q[8])
circ.cx(q[8],q[7])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.cx(q[1],q[2])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[9])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[10],q[4])
circ.u1(pi/4, q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.cx(q[1],q[2])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[11])
circ.u1(pi/4, q[12])
circ.cx(q[12],q[11])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.cx(q[8],q[7])
circ.cx(q[7],q[8])
circ.cx(q[8],q[7])
circ.u1(-pi/4, q[9])
circ.cx(q[8],q[9])
circ.u1(pi/4, q[9])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[9])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.u2(0,5*pi/4, q[8])
circ.cx(q[8],q[6])
circ.u2(0,pi, q[8])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[9],q[8])
circ.u1(-pi/4, q[8])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[9])
circ.cx(q[8],q[9])
circ.u1(pi/4, q[8])
circ.u1(-pi/4, q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.u2(0,5*pi/4, q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[9],q[8])
circ.u1(-pi/4, q[8])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[8])
circ.u2(0,pi, q[8])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.cx(q[8],q[7])
circ.cx(q[7],q[8])
circ.cx(q[8],q[7])
circ.u1(-pi/4, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[11],q[10])
circ.u2(0,pi, q[10])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[4],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[4],q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u1(9*pi/4, q[11])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[10])
circ.u2(0,pi, q[10])
circ.u1(9*pi/4, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[8],q[9])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.cx(q[8],q[7])
circ.cx(q[7],q[8])
circ.cx(q[8],q[7])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[11])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[2],q[3])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[11])
circ.u1(pi/4, q[12])
circ.cx(q[12],q[11])
circ.u1(9*pi/4, q[3])
circ.cx(q[11],q[3])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[11])
circ.u1(pi/4, q[12])
circ.cx(q[3],q[11])
circ.u2(0,5*pi/4, q[11])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[12])
circ.u1(-pi/4, q[12])
circ.u1(pi/4, q[2])
circ.cx(q[2],q[12])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[11])
circ.cx(q[10],q[11])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.u2(0,5*pi/4, q[9])
circ.cx(q[9],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[8],q[9])
circ.u1(pi/4, q[9])
circ.cx(q[5],q[9])
circ.u1(pi/4, q[5])
circ.u1(-pi/4, q[9])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.u2(0,5*pi/4, q[8])
circ.cx(q[9],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[6])
circ.cx(q[6],q[8])
circ.cx(q[8],q[6])
circ.cx(q[6],q[8])
circ.cx(q[9],q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u2(0,pi, q[9])
circ.cx(q[8],q[9])
circ.u1(-pi/4, q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[6],q[8])
circ.u1(pi/4, q[8])
circ.cx(q[9],q[8])
circ.u1(-pi/4, q[8])
circ.cx(q[6],q[8])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[6],q[8])
circ.u1(pi/4, q[6])
circ.u1(-pi/4, q[8])
circ.cx(q[6],q[8])
circ.u2(0,pi, q[8])
circ.u2(0,5*pi/4, q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.u1(pi/4, q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[10])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[10])
circ.u2(0,pi, q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[11])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.cx(q[12],q[11])
circ.u1(pi/4, q[11])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[11])
circ.u1(-pi/4, q[11])
circ.cx(q[12],q[11])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[11])
circ.u1(pi/4, q[12])
circ.cx(q[12],q[11])
circ.u1(9*pi/4, q[3])
circ.cx(q[11],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[12],q[11])
circ.u1(pi/4, q[11])
circ.cx(q[3],q[11])
circ.u1(-pi/4, q[11])
circ.cx(q[12],q[11])
circ.u2(0,5*pi/4, q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[12],q[2])
circ.u1(pi/4, q[12])
circ.u1(-pi/4, q[2])
circ.cx(q[12],q[2])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.u1(9*pi/4, q[9])
circ.cx(q[10],q[9])
circ.u1(-pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[6],q[5])
circ.u1(pi/4, q[5])
circ.cx(q[5],q[9])
circ.cx(q[6],q[8])
circ.cx(q[8],q[6])
circ.cx(q[6],q[8])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[9])
circ.cx(q[8],q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.u2(0,5*pi/4, q[10])
circ.cx(q[10],q[4])
circ.u2(0,pi, q[10])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[8],q[9])
circ.u1(pi/4, q[8])
circ.u1(-pi/4, q[9])
circ.cx(q[8],q[9])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[9],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[9],q[10])
circ.u2(0,5*pi/4, q[10])
circ.cx(q[9],q[8])
circ.u1(-pi/4, q[8])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[8])
circ.u2(0,pi, q[8])
circ.cx(q[6],q[8])
circ.cx(q[8],q[6])
circ.cx(q[6],q[8])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[4],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[11],q[10])
circ.u2(0,5*pi/4, q[10])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[11])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.u2(0,pi, q[3])
circ.cx(q[11],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[11])
circ.u1(-pi/4, q[3])
circ.cx(q[4],q[3])
circ.u2(0,5*pi/4, q[3])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[11])
circ.barrier()
circ.u3(pi,0,pi, q[10])
circ.cx(q[10],q[11])
circ.u2(0,pi, q[2])
circ.u2(0,pi, q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[4],q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[10])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[4],q[5])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[11])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[3],q[4])
circ.cx(q[3],q[11])
circ.u1(-pi/4, q[11])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.u2(0,5*pi/4, q[4])
circ.u2(0,pi, q[8])
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
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[6],q[8])
circ.u1(-pi/4, q[8])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.u1(pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[6],q[5])
circ.u1(-pi/4, q[5])
circ.cx(q[4],q[5])
circ.u1(pi/4, q[6])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[4],q[5])
circ.u1(pi/4, q[4])
circ.u1(-pi/4, q[5])
circ.u2(0,5*pi/4, q[6])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[10],q[4])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.u1(-pi/4, q[4])
circ.cx(q[10],q[4])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[11])
circ.cx(q[10],q[11])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.u2(0,5*pi/4, q[4])
circ.cx(q[5],q[6])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.u2(0,pi, q[4])
circ.cx(q[3],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[10],q[4])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.u1(-pi/4, q[4])
circ.cx(q[10],q[4])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[11])
circ.cx(q[10],q[11])
circ.cx(q[10],q[9])
circ.u2(0,pi, q[11])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.u2(0,5*pi/4, q[4])
circ.cx(q[5],q[6])
circ.cx(q[6],q[5])
circ.cx(q[5],q[6])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[11],q[10])
circ.u2(0,pi, q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[3],q[11])
circ.u1(-pi/4, q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.u1(9*pi/4, q[4])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[9],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
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
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.cx(q[11],q[12])
circ.u1(pi/4, q[11])
circ.u1(-pi/4, q[12])
circ.cx(q[11],q[12])
circ.cx(q[2],q[12])
circ.cx(q[12],q[2])
circ.cx(q[2],q[12])
circ.u1(9*pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[11])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.u2(0,5*pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[12],q[2])
circ.u1(9*pi/4, q[9])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[3],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[5],q[4])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.u2(0,5*pi/4, q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[8],q[9])
circ.u1(pi/4, q[9])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[9])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.u2(0,5*pi/4, q[8])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[8],q[9])
circ.u2(0,pi, q[8])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[10],q[9])
circ.u1(-pi/4, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[11],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u2(0,5*pi/4, q[11])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.u1(pi/4, q[9])
circ.cx(q[10],q[9])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[9])
circ.cx(q[10],q[9])
circ.u2(0,pi, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[4],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[4],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[3],q[4])
circ.u1(pi/4, q[3])
circ.u1(-pi/4, q[4])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.u1(9*pi/4, q[10])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.u1(pi/4, q[4])
circ.cx(q[4],q[3])
circ.u2(0,pi, q[3])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[12],q[2])
circ.u1(pi/4, q[12])
circ.u1(-pi/4, q[2])
circ.cx(q[12],q[2])
circ.u1(9*pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[12],q[11])
circ.u1(pi/4, q[11])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[2],q[12])
circ.u1(-pi/4, q[12])
circ.cx(q[11],q[12])
circ.u2(0,5*pi/4, q[12])
circ.u1(pi/4, q[2])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[12],q[11])
circ.cx(q[11],q[12])
circ.cx(q[12],q[11])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[3],q[2])
circ.u1(-pi/4, q[2])
circ.u1(pi/4, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[9],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[10])
circ.u1(-pi/4, q[11])
circ.cx(q[10],q[11])
circ.u2(0,5*pi/4, q[9])
circ.cx(q[9],q[5])
circ.u2(0,pi, q[9])
circ.cx(q[10],q[9])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.cx(q[9],q[10])
circ.u1(pi/4, q[10])
circ.cx(q[11],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[11])
circ.cx(q[9],q[10])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.u2(0,5*pi/4, q[11])
circ.cx(q[9],q[10])
circ.u1(-pi/4, q[10])
circ.u1(pi/4, q[9])
circ.cx(q[9],q[10])
circ.u2(0,pi, q[10])
circ.cx(q[4],q[10])
circ.cx(q[10],q[4])
circ.cx(q[4],q[10])
circ.cx(q[10],q[9])
circ.cx(q[3],q[4])
circ.u1(-pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[3])
circ.cx(q[4],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[2],q[3])
circ.u2(0,pi, q[3])
circ.cx(q[2],q[3])
circ.u1(-pi/4, q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.u2(0,5*pi/4, q[4])
circ.cx(q[4],q[5])
circ.cx(q[5],q[4])
circ.cx(q[4],q[5])
circ.cx(q[9],q[10])
circ.cx(q[10],q[9])
circ.cx(q[10],q[11])
circ.u1(pi/4, q[11])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[10])
circ.cx(q[10],q[11])
circ.cx(q[11],q[10])
circ.cx(q[2],q[3])
circ.u1(pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[11],q[3])
circ.u1(pi/4, q[11])
circ.u2(0,5*pi/4, q[2])
circ.u1(-pi/4, q[3])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[11],q[3])
circ.cx(q[3],q[11])
circ.cx(q[3],q[2])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[9],q[8])
circ.cx(q[8],q[9])
circ.cx(q[9],q[8])
circ.cx(q[5],q[9])
circ.cx(q[9],q[5])
circ.cx(q[5],q[9])
circ.cx(q[4],q[5])
circ.u3(pi,0,pi, q[4])
circ.barrier()
circ.measure(q[11], c[0])
circ.measure(q[2], c[1])
circ.measure(q[3], c[2])
circ.measure(q[5], c[3])
circ.measure(q[6], c[4])