from tarfile import REGULAR_TYPES


r0=r1=r2=r3=r4=r5=r6=flag=0

registers={
    "r0":"000",
    "r1": "001",
    "r2": "010",
    "r3": "011",
    "r4": "100",
    "r5": "101",
    "r6": "110",
    "flags": "111",
}

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

A={
    "add":"10000",
    "sub":"10001",
    "mul":"10110",
    "xor":"11010",
    "or":"11011",
    "and":"11100"
}
B={
    "mov":"10010",
    "ls":"11001",
    "rs":"11000"
    
}


C={
    "mov":"10011",
    "div":"10111",
    "not":"11101",
    "cmp":"11110"
}

D={
    "ld":"10100",
    "st":"10101",
}

E={
   "jmp":"11111",
   "jlt":"01100",
   "jgt":"01101",
   "je":"01111",
}
F={
    "hlt":"01010"
}
def typeA(s):
    ans=""
    ans=A[s[0]]+"00"+registers[s[1]]+registers[s[2]]+registers[s[3]]
    f=open("binary.txt","a")
    f.write(ans+"\n")
def typeB(s):
    ans=""
    ans=B[s[0]]+registers(s[1])+dtob(s[2][1:])  
    f=open("binary.txt","a")
    f.write(ans+"\n")  
def typeC(s):
    ans=""
    ans=C[s[0]]+"00000"+registers[s[1]]+registers[s[2]]
    f=open("binary.txt","a")
    f.write(ans+"\n")

def typeD(s):
    ans=""
    ans=D[s[0]]+registers[s[1]] #memadress to be added
    f=open("binary.txt","a")
    f.write(ans+"\n")
    
def typeE(s):
    ans=""
    ans=E[s[0]]+"000" #memadress to be added
    f=open("binary.txt","a")
    f.write(ans+"\n")
    
def typeF(s):
    ans=""
    ans=F[s[0]]+"0"*11
    f=open("binary.txt","a")
    f.write(ans+"\n") 
    
def errorHandle(s):
    pass

def dtob(dec):
    s=""
    while(dec>0):
        s=(str)(dec%2)+s
        dec=dec//2
    return s         

    
with open("file.txt","r") as f:
    s=""
    for i in f:
        s=i.split()
        if(s[0]=="mov"):
            if("$" in s):
                typeB()
            else:
                typeC()
        elif(s[0] in A.keys()):
            typeA(s)
        elif(s[0] in B.keys()):
            typeB(s)
        elif(s[0] in C.keys()):
            typeC(s)
        elif(s[0] in D.keys()):
            typeD(s)
        elif(s[0] in E.keys()):
            typeE(s)
        elif(s[0] in F.keys()):
            typeF(s)
        else:
            errorHandle(s)