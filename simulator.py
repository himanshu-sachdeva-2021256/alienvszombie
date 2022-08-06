R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000"
PC = 0
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
    binary=int(binary)
    decimal = i = 0
    while (binary != 0):
        # print((binary))
        dec = binary % 10
        decimal = decimal + dec * (2 ** i)
        binary = binary // 10
        i += 1
    return decimal


def dtob(dec):
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 16):
        s = (16 - len(s)) * "0" + s
    return s


def add(inst):
    registers[inst[7:10]] = dtob(binToDec(int(registers[inst[10:13]])) + binToDec(int(registers[inst[13:]])))
    if binToDec(int(registers[inst[7:10]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[7:10]] = "1"*16
    else:
        registers["111"] = "0"*16


def sub(inst):
    registers[inst[7:10]] = dtob(binToDec(int(registers[inst[10:13]])) - binToDec(int(registers[inst[13:]])))
    if binToDec(int(registers[inst[7:10]])) < 0:
        registers["111"] = "0000000000001000"
        registers[inst[7:10]] = "0"*16
    else:
        registers["111"] = "0"*16


def mul(inst):
    registers[inst[7:10]] = dtob(binToDec(int(registers[inst[10:13]])) * binToDec(int(registers[inst[13:]])))
    if binToDec(int(registers[inst[7:10]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[7:10]] = "1"*16
    elif binToDec(int(registers[inst[7:10]])) < 0:
        registers["111"] = "0000000000001000"
        registers[inst[7:10]] = "0"*16
    else:
        registers["111"] = "0"*16


def xor(inst):
    registers[inst[7:10]] = dtob(binToDec(int(registers[inst[10:13]])) ^ binToDec(int(registers[inst[13:]])))
    registers["111"] = "0"*16


def or1(inst):
    registers[inst[7:10]] = dtob(binToDec(int(registers[inst[10:13]])) | binToDec(int(registers[inst[13:]])))
    registers["111"] = "0"*16


def and1(inst):
    registers[inst[7:10]] = dtob(binToDec(int(registers[inst[10:13]])) & binToDec(int(registers[inst[13:]])))
    registers["111"] = "0"*16


def movr(inst):
    registers[inst[13:]] = registers[inst[10:13]]
    registers["111"] = "0"*16


def div(inst):
    registers["000"] = dtob(binToDec(int(registers[inst[10:13]])) // binToDec(int(registers[inst[13:]])))
    registers["001"] = dtob(binToDec(int(registers[inst[10:13]])) % binToDec(int(registers[inst[13:]])))
    registers["111"] = "0"*16


def not1(inst):
    registers[inst[13:]] = dtob(~binToDec(int(registers[inst[10:13]])))
    registers["111"] = "0"*16


def cmp(inst):
    if ((binToDec(int(registers[inst[10:13]]))) > binToDec(int(registers[inst[13:]]))):
        registers["111"] = "0000000000000010"
    elif ((binToDec(int(registers[inst[10:13]]))) == binToDec(int(registers[inst[13:]]))):
        registers["111"] = "0000000000000001"
    elif ((binToDec(int(registers[inst[10:13]]))) < binToDec(int(registers[inst[13:]]))):
        registers["111"] = "0" * 16


def movi(inst):
    registers[inst[5:8]] = dtob(binToDec(inst[8:]))
    registers["111"] = "0" * 16


def ls(inst):
    registers["111"] = "0" * 16
    registers[inst[5:8]] = dtob(2 * binToDec(inst[8:]))


def rs(inst):
    registers["111"] = "0" * 16
    registers[inst[5:8]] = dtob(binToDec(inst[8:]) // 2)


def ld(inst):
    registers["111"] = "0" * 16


def st(inst):
    registers["111"] = "0" * 16


def jmp(inst):
    global PC
    PC = binToDec(inst[8:])
    registers["111"] = "0" * 16


def jgt(inst):
    global PC
    if (FLAGS[13] == 1):
        PC = binToDec(inst[8:])
    registers["111"] = "0" * 16


def jlt(inst):
    global PC
    if (FLAGS[13] == 1):
        PC = binToDec(inst[8:])
    registers["111"] = "0" * 16


def je(inst):
    global PC
    if (FLAGS[15] == 1):
        PC = binToDec(inst[8:])
    registers["111"] = "0" * 16


def hlt():
    pass


A = {
    "10000": add,
    "10001": sub,
    "10110": mul,
    "11010": xor,
    "11011": or1,
    "11100": and1,
}

B = {
    "10010": movi,
    "11001": ls,
    "11000": rs

}
F = {
    "01010": hlt
}

C = {
    "10011": movr,
    "10111": div,
    "11101": not1,
    "11110": cmp
}

D = {
    "10100": ld,
    "10101": st,
}

E = {
    "11111": jmp,
    "01100": jlt,
    "01101": jgt,
    "01111": je,
}


def execute(inst):
    # print(type(inst))
    if (inst[:5] in A):
        A[inst[:5]](inst)
    if (inst[:5] in B):
        B[inst[:5]](inst)
    if (inst[:5] in C):
        C[inst[:5]](inst)
    if (inst[:5] in D):
        D[inst[:5]](inst)
    if (inst[:5] in E):
        E[inst[:5]](inst)
    if (inst[:5] in F):
        exit()



l=[
    "1001000100000100",
    "1001001000000100",
    "1011000001010011",
    "1010101100000110",
    "1010010000000110",
    "0101000000000000",
]

for i in range(len(l)):
    execute(l[i])
    print(dtob(PC)[8:],registers["000"],registers["001"],registers["010"],registers["011"],registers["100"],registers["101"],registers["110"],registers["111"],sep="  ")
    PC+=1
print(dtob(PC)[7:],registers["000"],registers["001"],registers["010"],registers["011"],registers["100"],registers["101"],registers["110"],registers["111"],sep="  ")
    