import sys

R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000"
PC = 0
newPC = 0
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
    binary = int(binary)
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
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) + binToDec(int(registers[inst[7:10]])))
    if binToDec(int(registers[inst[13:16]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "1" * 16
    else:
        registers["111"] = "0" * 16


def sub(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] =  dtob(binToDec(int(registers[inst[7:10]])) - (binToDec(int(registers[inst[10:13]]))))
    if binToDec(int(registers[inst[13:16]])) < 0:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "0" * 16
    else:
        registers["111"] = "0" * 16


def mul(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) * binToDec(int(registers[inst[7:10]])))
    if binToDec(int(registers[inst[13:16]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "1" * 16
    elif binToDec(int(registers[inst[13:16]])) < 0:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "0" * 16
    else:
        registers["111"] = "0" * 16


def xor(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) ^ binToDec(int(registers[inst[7:10]])))
    registers["111"] = "0" * 16


def or1(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) | binToDec(int(registers[inst[7:10]])))
    registers["111"] = "0" * 16


def and1(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) & binToDec(int(registers[inst[7:10]])))
    registers["111"] = "0" * 16


def movr(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = registers[inst[10:13]]
    registers["111"] = "0" * 16


def div(inst):
    global newPC
    newPC += 1
    registers["000"] = dtob(binToDec(int(registers[inst[10:13]])) // binToDec(int(registers[inst[13:16]])))
    registers["001"] = dtob(binToDec(int(registers[inst[10:13]])) % binToDec(int(registers[inst[13:16]])))
    registers["111"] = "0" * 16


def not1(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(~binToDec(int(registers[inst[10:13]])))
    registers["111"] = "0" * 16


def cmp1(inst):
    global newPC
    newPC += 1
    if ((binToDec(int(registers[inst[10:13]]))) > binToDec(int(registers[inst[13:16]]))):
        registers["111"] = "0000000000000010"
    elif ((binToDec(int(registers[inst[10:13]]))) == binToDec(int(registers[inst[13:16]]))):
        # print(binToDec(int(registers[inst[10:13]])),binToDec(int(registers[inst[13:16]])))
        registers["111"] = "0000000000000001"
    elif ((binToDec(int(registers[inst[10:13]]))) < binToDec(int(registers[inst[13:16]]))):
        # print(binToDec(int(registers[inst[10:13]])),binToDec(int(registers[inst[13:16]])))
        registers["111"] = "0000000000000100"


def movi(inst):
    global newPC
    newPC += 1
    registers[inst[5:8]] = dtob(binToDec(inst[8:]))
    registers["111"] = "0" * 16


def ls(inst):
    global newPC
    newPC += 1
    registers["111"] = "0" * 16
    registers[inst[5:8]] = dtob((binToDec(registers[inst[5:]])) * 2 ** binToDec(inst[8:]))


def rs(inst):
    global newPC
    newPC += 1
    registers["111"] = "0" * 16
    registers[inst[5:8]] = dtob((binToDec(registers[inst[5:]])) // 2 ** binToDec(inst[8:]))


def ld(inst):
    global newPC
    newPC += 1
    registers[inst[5:8]] = mem[binToDec(inst[8:])]
    registers["111"] = "0" * 16


def st(inst):
    global newPC
    newPC += 1
    mem[binToDec(inst[8:])] = registers[inst[5:8]]
    registers["111"] = "0" * 16


def jmp(inst):
    global newPC
    newPC = binToDec(inst[8:])
    registers["111"] = "0" * 16


def jgt(inst):
    global newPC
    if (registers["111"] == "0000000000000010"):
        newPC = binToDec(inst[8:])
    else:
        newPC+=1
    registers["111"] = "0" * 16


def jlt(inst):
    global newPC
    # print("heello",newPC)
    if (registers["111"] == "0000000000000100"):
        newPC = binToDec(inst[8:])
    else:
        newPC+=1
    registers["111"] = "0" * 16
    # print(newPC)
    # exit()

def je(inst):
    global newPC
    if (registers["111"] == "0000000000000001"):
        newPC = binToDec(inst[8:])
    else:
        newPC+=1
    registers["111"] = "0" * 16


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
    "01010": "hlt"
}

C = {
    "10011": movr,
    "10111": div,
    "11101": not1,
    "11110": cmp1
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
    # 
    # (type(inst))
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


with open("test.txt", "w") as w:
    pass

instruction_list = []

for line in sys.stdin:
    if line == '' or line == '\n':
        break
    instruction_list.append(line.strip())

mem = instruction_list
l = len(instruction_list)
while (l < 256):
    mem.append("0" * 16)
    l += 1


def regprint():
    print(registers["000"], registers["001"], registers["010"], registers["011"], registers["100"], registers["101"],
          registers["110"], registers["111"], sep=" ")


def memdump():
    for i in mem:
        with open("test.txt", "a") as w:
            w.write(i)
            w.write("\n")
        print(i)


def dtob2(dec):
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 8):
        s = (8 - len(s)) * "0" + s
    return s
y=[0]
x=[]
halt_flag = 0
while (halt_flag == 0):
# for ijk in range(0,50):
    instruction = mem[PC]
    if (instruction[:5] == "01010"):
        halt_flag = 1
    execute(instruction)
    with open("test.txt", "a") as w:
        w.write(dtob2(PC) + " ")
    print(dtob2(PC), end=" ")
    PC = newPC
    y.append(PC)
    # print(newPC)
    regprint()
n=len(y)
for i in range(1,n+1):
    y.append(i)

memdump()

# l = [
#      "1001000100000100",
#      "1001001000000100",
#      "1011000001010011",
#      "1010101100000110",
#      "1010010000000110",
#      "0101000000000000",
#
#
#     "1001000100000101",
#     "1001000100000101",
#     "1001000100000101",
#     "1001000100000101",
#     "1001000100000101",
#     "1001000100000101",
#     "0101000000000000"


# ]


# for i in range(len(l)):
#     execute(l[i])
#     print(dtob2(PC), registers["000"], registers["001"], registers["010"], registers["011"], registers["100"],
#           registers["101"], registers["110"], registers["111"], sep=" ")
#     PC = newPC
