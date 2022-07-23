R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000"

registers = {
    "000": "R0",
    "001": "R1",
    "010": "R2",
    "011": "R3",
    "100": "R4",
    "101": "R5",
    "110": "R6",
    "111": "FLAGS"
}

A = {
    "00000": add,
    "00001": sub,
    "00110": mul,
    "01010": xor,
    "01011": or,
    "01100": and,
}

B = {
    "00010":mov,
    "01001":ls ,
    "01000":rs

}
F = {
    "10011":hlt
}

C = {
    "00011":mov,
    "00111":div,
    "01101":not,
    "01110":cmp
}

D = {
    "00100": ld,
    "00101": st,
}

E = {
    "01111":jmp ,
    "10000":jlt ,
    "10001":jgt ,
    "10010":je,
}
#VALUES IN THE DICTIONARIES ARE THE FUNCTIONS. USE DICT[KEY] TO CALL THE FUNCTION



def typeA(inst):

def typeB(inst):

def typeC(inst):

def typeD(inst):

def typeE(inst):

def typeF(inst):

#interpret the registers and the immediate values in each type of instruction above



def execute(inst):
    if(inst[:5] in A):
        typeA(inst)
    if (inst[:5] in B):
        typeB(inst)
    if (inst[:5] in C):
        typeC(inst)
    if (inst[:5] in D):
        typeD(inst)
    if (inst[:5] in E):
        typeE(inst)
    if (inst[:5] in F):
        typeF(inst)
