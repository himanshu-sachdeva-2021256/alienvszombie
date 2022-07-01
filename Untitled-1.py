r0 = r1 = r2 = r3 = r4 = r5 = r6 = flag = 0

registers = {
    "r0": "000",
    "r1": "001",
    "r2": "010",
    "r3": "011",
    "r4": "100",
    "r5": "101",
    "r6": "110",
    "flags": "111",
}
var_list = {}
# opcode={
#     "add":"10000",
#     "sub":"10001",
#     "mov":["10010","10011"],
#     "ld":"10100",
#     "st":"10101",
#     "mul":"10110",
#     "div":"10111",
#     "rs":"11000",
#     "ls":"11001",
#     "xor":"11010",
#     "or":"11011",
#     "and":"11100",
#     "not":"11101",
#     "cmp":"11110",
#     "jmp":"11111",
#     "jlt":"01100",
#     "jgt":"01101",
#     "je":"01111",
#     "hlt":"01010"
# }

A = {
    "add": "10000",
    "sub": "10001",
    "mul": "10110",
    "xor": "11010",
    "or": "11011",
    "and": "11100"
}
B = {
    "mov": "10010",
    "ls": "11001",
    "rs": "11000"

}
F = {
    "hlt": "01010"
}

C = {
    "mov": "10011",
    "div": "10111",
    "not": "11101",
    "cmp": "11110"
}

D = {
    "ld": "10100",
    "st": "10101",
}

E = {
    "jmp": "11111",
    "jlt": "01100",
    "jgt": "01101",
    "je": "01111",
}


def dtob(dec):
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    return s


def errorHandle(i):
    print(f"INVALID OPERATION AT LINE {i}")


def ins_valid(s, i):
    if (s[0] in A):
        if (len(s) != 4):
            print(f"INVALID INSTRUCTION AT LINE {i}")
        if (s[1] not in registers or s[2] not in registers or s[3] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")

    if (s[0] in B):
        if (s[1] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
        if ("$" not in s[2]):
            print(f"INVALID INSTRUCTION AT LINE {i}")
        if (int(s[2][1:]) > 127):
            print(f"VALUE OF IMMEDIATE EXCEEDS THE LIMIT(MORE THAN 8 BITS) AT LINE {i}")

    if (s[0] in C):
        if (s[1] not in registers or s[2] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
    if (s[0] in D):
        if (s[1] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
        if (s[2] not in var_list):
            print(f"INVALID MEMORY ADDRESS AT LINE {i}")
    if (s[0] in E):
        if (s[1] not in var_list):
            print(f"INVALID MEMORY ADDRESS AT LINE {i}")


def typeA(s):
    ans = ""
    ans = A[s[0]] + "00" + registers[s[1]] + registers[s[2]] + registers[s[3]]
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeB(s):
    ans = ""
    ans = B[s[0]] + registers(s[1]) + dtob(s[2][1:])
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeC(s):
    ans = ""
    ans = C[s[0]] + "00000" + registers[s[1]] + registers[s[2]]
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeD(s):
    ans = ""
    ans = D[s[0]] + registers[s[1]] + var_list[]  # memadress to be added
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeE(s):
    ans = ""
    ans = E[s[0]] + "000"  # memadress to be added
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeF(s):
    ans = ""
    ans = F[s[0]] + "0" * 11
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def errorHandle():
    pass


with open("file.txt", "r") as f:
    l = []
    var_count = 0
    ins_count = 0
    for i in f:
        s = i.split()
        l.append(s)
        ins_count += 1

        if (s[0] == "var"):
            if (len(var_list) > 2 ** 8):
                print("TOO MANY VARIBALES")
            else:
                var_list[s[1]] = [0, 0]
                var_count += 1

    curr_address = ins_count + 1
    for i in var_list:
        var_list[i][0] = curr_address
        curr_address += 1

    i = 1
    for s in l:
        if (s[0] == "mov"):
            if ("$" in s[2]):
                typeB(s)
            else:
                typeC(s)
        elif (s[0] in A):
            typeA(s)
        elif (s[0] in B):
            typeB(s)
        elif (s[0] in C):
            typeC(s)
        elif (s[0] in D):
            typeD(s)
        elif (s[0] in E):
            typeE(s)
        elif (s[0] in F):
            typeF(s)
        else:
            errorHandle(i)
        i += 1
