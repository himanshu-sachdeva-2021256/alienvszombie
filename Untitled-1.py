import sys

r0 = r1 = r2 = r3 = r4 = r5 = r6 = flag = 0
var_list = {}
labels = {}

registers = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
}

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
    dec=int(dec)
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 8):
        s = (8 - len(s)) * "0" + s
    return s


def errorHandle(i):
    print(f"INVALID OPERATION AT LINE {i}")
    exit()


def ins_valid(s, i):
    if (s[0] in A):
        if (len(s) != 4):
            print(f"INVALID INSTRUCTION AT LINE {i}")
            exit()
        if (s[1] not in registers or s[2] not in registers or s[3] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
            exit()

    #length of instruction to be checked for all the below instruction types

    if (s[0] in B):
        if (s[1] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
            exit()
        if ("$" not in s[2]):
            print(f"INVALID INSTRUCTION AT LINE {i}")
            exit()
        if (int(s[2][1:]) > 127):
            print(f"VALUE OF IMMEDIATE EXCEEDS THE LIMIT(MORE THAN 8 BITS) AT LINE {i}")
            exit()
    if (s[0] in C):
        if (s[1] not in registers or s[2] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
            exit()
    if (s[0] in D):
        if (s[1] not in registers):
            print(f"INVALID REGISTER NAME USED IN LINE {i}")
            exit()
        if (s[2] not in var_list):
            print(f"INVALID MEMORY ADDRESS AT LINE {i}")
            exit()
    if (s[0] in E):
        if (s[1] not in var_list):
            print(f"INVALID MEMORY ADDRESS AT LINE {i}")
            exit()


def typeA(s,i):
    ins_valid(s,i)
    ans = ""
    ans = A[s[0]] + "00" + registers[s[1]] + registers[s[2]] + registers[s[3]]
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeB(s,i):
    ins_valid(s,i)
    ans = ""
    ans = B[s[0]] + registers[s[1]] + dtob(s[2][1:])
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeC(s,i):
    ins_valid(s,i)
    ans = ""
    ans = C[s[0]] + "0" * 5 + registers[s[1]] + registers[s[2]]
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeD(s,i):
    ins_valid(s,i)
    ans = ""
    ans = D[s[0]] + registers[s[1]] + var_list[s[2]][0]
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeE(s,i):
    ins_valid(s,i)
    ans = ""
    ans = E[s[0]] + "000" + str(labels[s[1]])    # memadress of label to be added
    f = open("binary.txt", "a")
    f.write(ans + "\n")


def typeF(s,i):
    ins_valid(s,i)
    ans = ""
    ans = F[s[0]] + "0" * 11
    f = open("binary.txt", "a")
    f.write(ans + "\n")


variable_flag_check = 0

with open("file.txt","w") as f:
    while True:
        k = sys.stdin.readline()
        f.write(k)
        # print(k)
        if k.strip() == "hlt":
            break

with open("file.txt", "r") as f:
    g=open("binary.txt","w")
    g.close()
    l = []
    var_count = 0
    line_count = 0
    label_count = 0
    for i in f:
        s = i.split()
        l.append(s)
        line_count += 1

        if (s[0] == "var"):
            if variable_flag_check == 1:
                print("VARIABLE DECLARATION NOT AT BEGINING")
            elif (len(var_list) > 2 ** 8):
                print("TOO MANY VARIABLES")
            else:
                var_list[s[1]] = ["0", 0]  # [address,value] of variable
                var_count += 1

        elif (":" in i):
            # if (len(s)!=1):
            #     print("Illegal Use of Labeles")
            if (s[0][:-1] in var_list):
                print("Lable name same as variable")
            else:
                labels[s[0][:-1]]=dtob(line_count-1)
                label_count += 1
                l.pop()
                l.append(s[1:])

        elif ("FLAGS" in i):
            if s[0]!="mov":
                print("Illegal use of flag")
            elif len(s)!=3:
                print("Illegal use of flag")
            
        else:
            variable_flag_check=1

    curr_address = line_count - var_count
    for i in var_list:
        d = dtob(curr_address)
        if (len(d) > 8):
            print("INVALID MEMORY ADDRESS FOUND")
            exit()
        var_list[i][0] = d
        curr_address += 1

    i = 1
    if (l[-1][0]!="hlt"):
        print("hlt not used")
    for s in l:
        # print(s)
        if (s[0]) == "var":
            if s[1] not in var_list:
                print("INVALID USE OF VARIABLE NOT DECLARED")
        elif (s[0][-1]==":"):
            if s[0][:-1] not in var_list:
                print("INVALID USE OF LABEL NOT DECLARED")
            
        #variables labels to be handled here
        elif (s[0] == "mov"):
            if ("$" in s[2]):
                typeB(s,i)
            else:
                typeC(s,i)
        elif (s[0] in A):
            typeA(s,i)
        elif (s[0] in B):
            typeB(s,i)
        elif (s[0] in C):
            typeC(s,i)
        elif (s[0] in D):
            typeD(s,i)
        elif (s[0] in E):
            typeE(s,i)
        elif (s[0] in F):
            typeF(s,i)
        else:
            errorHandle(i)
        i += 1


with open("binary.txt","r") as f:
    k=f.read()
    sys.stdout.write(k)
