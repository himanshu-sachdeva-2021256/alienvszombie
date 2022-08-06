import math

space = input("memory space: ").split()
addressable = input("Addressable type: ").split()
bits = 0
factor = 0
if ("b" in space[1]):
    bits = 1
if ("word" in space[1] or "Word" in space[1]):
    word = 1
if ("G" in space[1] or "g" in space[1]):
    factor = 3
if ("M" in space[1] or "m" in space[1]):
    factor = 2
if ("K" in space[1] or "k" in space[1]):
    factor = 1
if ("T" in space[1] or "t" in space[1]):
    factor = 4
size = 0
if (addressable[0].lower() == "byte"):
    size = 8
elif (addressable[0].lower() == "bit"):
    size = 1
elif (addressable[0].lower() == "nibble"):
    size = 4


def ISA():
    global space
    global size
    if (bits == 1):
        unique = int(space[0]) * (1024 * factor) / size
    else:
        unique = int(space[0]) * (1024 * factor) * 8 / size
    bit_req = int(math.log(unique, 2))
    len_inst = int(input("length of inst: "))
    reg = int(input("length of register: "))
    opcode = len_inst - reg - bit_req
    filler = len_inst - 2 * reg - opcode
    max_inst = 2 ** opcode
    max_reg = 2 ** reg
    print("min bits required for address=", bit_req)
    print("bit required for opcode=", opcode)
    print("filler bits=", filler)
    print("max number of inst=", max_inst)
    print("max number of registers=", max_reg)


def sysen():
    global size
    t = int(input("\nTYPE 1 or TYPE 2\n"))
    if (t == 1):
        cpubits = input("cpu bits: ").split()
        enh = input("enhancement: ").split()
        s = 1
        if ("byte" in enh):
            s = 8
        if ("bit" in enh):
            s = 1
        if ("nibble" in enh):
            s = 4
        if ("word" in enh):
            s = int(cpubits[0])
        if (size == 0):
            size = int(cpubits[0])  # word addressable weren't assigned a size initially

        if (bits == 1):
            unique = int(space[0]) * (1024 * factor) / size
        elif (word == 1):
            unique = (int(space[0])*int(cpubits[0]) * (1024 ** factor)) / size
        else:
            unique = int(space[0]) * (1024 * factor) * 8 / size
        curr_pins = math.log(unique, 2)
        if (bits == 1):
            u = int(space[0]) * (1024 * factor) / s
        elif(word==1):
            u=(int(space[0])*int(cpubits[0]) * (1024 ** factor)) / s
        else:
            u = int(space[0]) * (1024 * factor) * 8 / s
        new_pins = math.log(u, 2)
        print()
        print(int(new_pins - curr_pins))
    if (t == 2):
        cpubits = input("cpu bits: ").split()
        pins = input("no. of pins: ").split()
        addr_type = input("Addressable type: ").split()
        cpubits = int(cpubits[0])
        pins = int(pins[0])
        s = 1
        if (addr_type[0].lower() == "byte"):
            s = 1
        if (addr_type[0].lower() == "bit"):
            s = 1 / 8
        if (addr_type[0].lower() == "nibble"):
            s = 1 / 2
        if (addr_type[0].lower() == "word"):
            s = cpubits / 8
        mem_size = (2 ** pins) * s
        print("memory size=", int(mem_size), " Bytes")


n = input("""QUERY INPUT: 
1.ISA
2.System enhancement\n""")
if (n == "1"):
    ISA()
else:
    sysen()
