with open('input.txt') as f:
    registers,programs = f.read().split('\n\n')

registers = {line.split(': ')[0].split()[1]: int(line.split(': ')[1]) for line in registers.splitlines()}
programs = [int(num) for num in programs.replace('\n','').split()[1].split(',')]

outputs = []

def combo(num,registers):
    if num<=3:
        return num
    elif num==4:
        return registers['A']
    elif num == 5:
        return registers['B']
    elif num == 6:
        return registers['C']

def adv(num,registers,instr):
    registers['A']=registers['A']//(2**combo(num,registers))
    return registers,instr+2

def bxl(num,registers,instr):
    registers['B'] = registers['B']^num
    return registers,instr+2

def bst(num,registers,instr):
    registers['B'] = combo(num,registers)%8
    return registers,instr+2

def jnz(num,registers,instr):
    if registers['A'] == 0:
        return registers,instr+2
    else:
        return registers,num

def bxc(num,registers,instr):
    registers['B'] = registers['B']^registers['C']
    return registers,instr+2

def out(num,registers,instr):
    outputs.append(combo(num,registers)%8)
    return registers,instr+2

def bdv(num,registers,instr):
    registers['B']=registers['A']//(2**combo(num,registers))
    return registers,instr+2

def cdv(num,registers,instr):
    registers['C']=registers['A']//(2**combo(num,registers))
    return registers,instr+2

length = len(programs)
instr = 0
while instr in range(length):
    opcode = programs[instr]
    function = [adv,bxl,bst,jnz,bxc,out,bdv,cdv][opcode]
    num = programs[instr+1]
    registers,instr = function(num,registers,instr)
    
answer = ','.join(str(num) for num in outputs)
print(answer)