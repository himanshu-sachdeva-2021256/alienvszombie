R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000"

registers = {
    "000": R0,
    "001": R1,
    "010": R2,
    "011": R3,
    "100": R4,
    "101": R5,
    "110": R6,
    "111": FLAGS
}
def binToDec(binary):
    decimal=i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * (2**i)
        binary = binary//10
        i += 1
    return decimal

def dtob(dec):
    dec=int(dec)
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 16):
        s = (16 - len(s)) * "0" + s
    return s


def add(inst):
    registers[inst[7:10]]=registers[inst[10:14]]+registers[inst[14:]]
    if binToDec(int(registers[inst[7:10]]))>255:
        registers["111"]="0000000000001000"
        registers[inst[7:10]]="11111111"
def sub(inst):
    registers[inst[7:10]]=registers[inst[10:14]]-registers[inst[14:]]
    if binToDec(int(registers[inst[7:10]]))<0:
        registers["111"]="0000000000001000"
        registers[inst[7:10]]="0"
def mul(inst):
    registers[inst[7:10]]=registers[inst[10:14]]*registers[inst[14:]]
    if binToDec(int(registers[inst[7:10]]))>255:
        registers["111"]="0000000000001000"
        registers[inst[7:10]]="11111111"
    if binToDec(int(registers[inst[7:10]]))<0:
        registers["111"]="0000000000001000"
        registers[inst[7:10]]="0"
        
def xor(inst):
    registers[inst[7:10]]=registers[inst[10:14]]^registers[inst[14:]]
def or1(inst):
    registers[inst[7:10]]=registers[inst[10:14]] | registers[inst[14:]]
def and1(inst):
    registers[inst[7:10]]=registers[inst[10:14]] & registers[inst[14:]]
def movr(inst):
    registers[inst[14:]]=registers[inst[10:14]]
def div(inst):
    registers["000"]=int(registers[inst[10:14]])/int(registers[inst[14:]])
    registers["001"]=int(registers[inst[10:14]])%int(registers[inst[14:]])
def not1(inst):
    registers[inst[14:]]=~registers[inst[10:14]]
def cmp(inst):
    if(registers[inst[10:14]]>registers[inst[14:]]):
        registers["111"]="0000000000000010"
    elif(registers[inst[10:14]]==registers[inst[14:]]):
        registers["111"]="0000000000000001"
    elif(registers[inst[10:14]]<registers[inst[14:]]):
        registers["111"]="0000000000000100"
A = {
    "00000": add,
    "00001": sub,
    "00110": mul,
    "01010": xor,
    "01011": or1,
    "01100": and1,
}

B = {
    "00010":movi,
    "01001":ls ,
    "01000":rs

}
F = {
    "10011":hlt
}

C = {
    "00011":movr,
    "00111":div,
    "01101":not1,
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

# def typeA(inst):
#     A[inst[:5]](inst)

# def typeB(inst):

# def typeC(inst):

# def typeD(inst):

# def typeE(inst):

# def typeF(inst):

# #interpret the registers and the immediate values in each type of instruction above



def execute(inst):
    if(inst[:5] in A):
        A[inst[:5]](inst)
    if (inst[:5] in B):
        typeB(inst)
    if (inst[:5] in C):
        C[inst[:5]](inst)
    if (inst[:5] in D):
        typeD(inst)
    if (inst[:5] in E):
        typeE(inst)
    if (inst[:5] in F):
        typeF(inst)
