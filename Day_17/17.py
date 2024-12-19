reg_A = 0
reg_B = 0
reg_C = 0
operation_pointer = 0
output_list = []

def xor(n1, n2):
    return n1^n2


def operand(n):
    if n >= 0 and n<=3:
        return n
    elif n==4:
        return reg_A
    elif n==5:
        return reg_B
    elif n==6:
        return reg_C

def opcode(n, ope):
    global operation_pointer, reg_A, reg_B, reg_C, output_list
    if n==0:
        reg_A = reg_A//(2**operand(ope))
        operation_pointer += 2
    if n==1:
        reg_B = xor(reg_B, ope)
        operation_pointer += 2
    if n==2:
        reg_B = operand(ope)%8
        operation_pointer += 2
    if n==3:
        if reg_A == 0:
            operation_pointer += 2
        else:
            operation_pointer = ope
    if n==4:
        reg_B = xor(reg_B, reg_C)
        operation_pointer += 2
    if n==5:
        output_list.append(operand(ope)%8)
        operation_pointer += 2
    if n==6:
        reg_B = reg_A//(2**operand(ope))
        operation_pointer += 2
    if n==7:
        reg_C = reg_A//(2**operand(ope))
        operation_pointer += 2

def search(depth, l):
    if depth == len(commands):
        return l[0]//8
    for val in l:
        b = val%8
        b = b^3
        c = val//(2**b)
        b = b^c
        b = b^3
        if commands[depth] == b%8:
            res = search(depth+1, [val*8+i for i in range(8)])
            if res != None:
                return res

with open("input.txt", "r") as file:
    string = file.read()
    second_star = bool(int(input("First star (1) or Second star (2) : "))-1)
    reg_A = int(string.splitlines()[0].split(": ")[1])
    reg_B = int(string.splitlines()[1].split(": ")[1])
    reg_C = int(string.splitlines()[2].split(": ")[1])
    commands = [int(val) for val in string.splitlines()[4].split(": ")[1].split(",")]
    if not second_star:
        while operation_pointer < len(commands):
            opcode(commands[operation_pointer], commands[operation_pointer+1])
        print(",".join([str(val) for val in output_list]))        
    else:
        commands.reverse()
        print(search(0, [1, 2, 3, 4, 5, 6, 7]))