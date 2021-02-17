def getQASMCode(device, job_id, path, filename):
    '''Retrieves the QASM code from the IBMQ backend. Args: device - the device on which the experiment was run, job_id - the
    id of the job, path - the name of the path we want the code writen.'''
    
    from qiskit import Aer, IBMQ 
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
    from qiskit.assembler import disassemble

    provider = IBMQ.load_account()
    device = provider.get_backend(device)
    result = device.retrieve_job(job_id)
    qob = result.qobj()

    jobs = disassemble(qob)
    qc = jobs[0][0]

    with open(path + "/" + filename + ".txt", 
              mode='wt', encoding='utf-8') as myfile:
        myfile.write(qc.qasm())
    
    return None

def QASMtoPython(path):
    '''Function that formats a txt file containing QASM code and outputs a txt file containing Python
    code, able to run on Qiskit.'''
    file = input("Please provide the name of the file: ")
    filename = (path + file + ".txt")
    
    # Import file and make each line a string in a list. Remember, all files must be in the QASM folder.
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]
    
    # Do the formatting on the operations
    for i in range(0,len(lines)):   
        if (("u1" in lines[i]) or ("u2" in lines[i]) or ("u3" in lines[i])):
            lines[i] = lines[i].replace(')', ',')
            lines[i] = lines[i].replace(';', ')')
            lines[i] = "circ." + lines[i]
        elif ("cx" in lines[i]):
            s = lines[i].split(',')
            s[0] = s[0].replace(' ', '(')
            s[1] = s[1].replace(';', ')')
            lines[i] = "circ." + s[0] + "," + s[1]
        elif ("x" in lines[i]):
            lines[i].replace(' ', '(')
            lines[i].replace(';', ')')
            lines[i] = "circ." + lines[i]
        elif ("barrier" in lines[i]):
            lines[i] = "circ.barrier()"
        elif ("measure" in lines[i]):
            s = lines[i].split(' ')
            s[2] = s[2].replace('->', ',')
            s[3] = s[3].replace(';', ')')
            lines[i] = "circ." + s[0] + "(" + s[1] + s[2] + " " + s[3]
            
        with open(path + "Formatted" + file + ".txt", 
                  mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(lines))
        myfile.close()
            
        with open(path + "NoiseFreeFormatted" + file + ".py", 
                  mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(lines))
        myfile.close()
            
    return ("Formatted" + file)
            
def AddQuantumErrors(path, file):
    '''This function adds the probabilistic quantum errors that create the dephasing noise.'''
    # Read in the file and prepare it
    filename = (path + file + ".txt")
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]

    # Insert empty lines before every line so the operations can get there
    for i in range(0,len(lines)*2,2):
        lines.insert(i+1, '')
       
    # Do the formatting of the file
    for i in range(0,len(lines),2):
        if (("u1" in lines[i]) or ("u2" in lines[i]) or ("u3" in lines[i])):
            s = lines[i].split('[')
            s = s[1].split(']')
            q = s[0]
            lines[i+1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGate(line, sqRates, tqRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))" +
                          "\r\t" + "if (dep == ['X']):" +
                          "\r\t\t" + "circ.x(q[" + q + "])" + 
                          "\r\t" + "elif (dep == ['Y']):" +
                          "\r\t\t" + "circ.y(q[" + q + "])" +
                          "\r\t" + "else:" +
                          "\r\t\t" + "circ.z(q[" + q + "])")
        elif ("cx" in lines[i]):
            s = lines[i].split('(')
            s = s[1].split(',')
            s0 = s[0].split('[')
            s0 = s0[1].split(']')
            q1 = s0[0]
            s0 = s[1].split('[')
            s0 = s0[1].split(']')
            q2 = s0[0]
            lines[i+1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGate(line, sqRates, tqRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))" +
                          "\r\t" + "if (dep == ['X']):" +
                          "\r\t\t" + "circ.x(q[" + q2 + "])" +
                          "\r\t" + "elif (dep == ['Y']):" +
                          "\r\t\t" + "circ.y(q[" + q2 + "])" +
                          "\r\t" + "else:" +
                          "\r\t\t" + "circ.z(q[" + q2 + "])")
        elif (".x" in lines[i]):
            s = lines[i].split('[')
            s = s[1].split(']')
            q = s[0]
            lines[i+1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGate(line, sqRates, tqRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))" +
                          "\r\t" + "if (dep == ['X']):" +
                          "\r\t\t" + "circ.x(q[" + q + "])" +
                          "\r\t" + "elif (dep == ['Y']):" +
                          "\r\t\t" + "circ.y(q[" + q + "])" +
                          "\r\t" + "else:" +
                          "\r\t\t" + "circ.z(q[" + q + "])")
        elif ("measure" in lines[i]):
            s = lines[i].split('q')
            s = s[1].split('[')
            s = s[1].split(']')
            q = s[0]
            lines[i-1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyMeasure(line, measRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "circ.x(q[" + q + "])")
            
    # Delete the white lines
    keep = []
    for line in lines:
        if (line != ''):
            keep.append(line)
    
    with open(path + file + ".py", mode='wt', 
          encoding='utf-8') as myfile:
        myfile.write('\n'.join(keep))
    myfile.close()

    return None

def AddGAQuantumErrors(path, file):
    '''This function adds the probabilistic quantum errors that create the dephasing noise.'''
    # Read in the file and prepare it
    filename = (path + file + ".txt")
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]

    # Insert empty lines before every line so the operations can get there
    for i in range(0,len(lines)*2,2):
        lines.insert(i+1, '')
       
    # Do the formatting of the file
    for i in range(0,len(lines),2):
        if (("u1" in lines[i]) or ("u2" in lines[i]) or ("u3" in lines[i])):
            s = lines[i].split('[')
            s = s[1].split(']')
            q = s[0]
            lines[i+1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGAGate(line, sqRates, tqRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))" +
                          "\r\t" + "if (dep == ['X']):" +
                          "\r\t\t" + "circ.x(q[" + q + "])" + 
                          "\r\t" + "elif (dep == ['Y']):" +
                          "\r\t\t" + "circ.y(q[" + q + "])" +
                          "\r\t" + "else:" +
                          "\r\t\t" + "circ.z(q[" + q + "])")
        elif ("cx" in lines[i]):
            s = lines[i].split('(')
            s = s[1].split(',')
            s0 = s[0].split('[')
            s0 = s0[1].split(']')
            q1 = s0[0]
            s0 = s[1].split('[')
            s0 = s0[1].split(']')
            q2 = s0[0]
            lines[i+1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGAGate(line, sqRates, tqRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))" +
                          "\r\t" + "if (dep == ['X']):" +
                          "\r\t\t" + "circ.x(q[" + q2 + "])" +
                          "\r\t" + "elif (dep == ['Y']):" +
                          "\r\t\t" + "circ.y(q[" + q2 + "])" +
                          "\r\t" + "else:" +
                          "\r\t\t" + "circ.z(q[" + q2 + "])")
        elif (".x" in lines[i]):
            s = lines[i].split('[')
            s = s[1].split(']')
            q = s[0]
            lines[i+1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGAGate(line, sqRates, tqRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))" +
                          "\r\t" + "if (dep == ['X']):" +
                          "\r\t\t" + "circ.x(q[" + q + "])" +
                          "\r\t" + "elif (dep == ['Y']):" +
                          "\r\t\t" + "circ.y(q[" + q + "])" +
                          "\r\t" + "else:" +
                          "\r\t\t" + "circ.z(q[" + q + "])")
        elif ("measure" in lines[i]):
            s = lines[i].split('q')
            s = s[1].split('[')
            s = s[1].split(']')
            q = s[0]
            lines[i-1] = ("line = '" + lines[i] + "'" + "\r\n" + 
                          "op = noisyGAMeasure(line, measRates)" + "\r\n" + 
                          "if (op == ['X']):" +
                          "\r\t" + "circ.x(q[" + q + "])")
            
    # Delete the white lines
    keep = []
    for line in lines:
        if (line != ''):
            keep.append(line)
    
    with open(path + "GA" + file + ".py", mode='wt', 
          encoding='utf-8') as myfile:
        myfile.write('\n'.join(keep))
    myfile.close()

    return None

def generatePythonCodes(device, job_id, path, filename):
    '''Creates the python files from the QASM in specific locations'''
    
    getQASMCode(device, job_id, path, filename)
    ErrorComposer(path)
    
    return None