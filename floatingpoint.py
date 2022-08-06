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


def floattob(dec):
    final=""
    for i in range(5):
        print(dec)
        dec=float("0."+str(dec))
        dec=float(dec)
        dec=dec*2
        final=final+str(dec)[0]
        dec=str(dec)[2:]
    return final


def exponent(num):
    num=int(num.split(".")[0])
    l=dtob(num)
    for i in range(len(l)):
        if l[i]=="1":
            break

    # print(l[i:])
    expo=3+len(l[i:])-1
    # print(l)
    return [dtob(expo)[-8:],l[i:]]

def floatingpoint(num):
    dec=int(num.split(".")[1])
    # num=int(num.split(".")[0])
    print("---",num)
    expo,mane=exponent(num)
    # expo,mane=[1,2]
    dec=floattob(dec)
    print(expo[-3:])
    print((str(mane)+str(dec))[:5])
    return str(expo)[-3:]+(str(mane[1:])+str(dec))[:5]
    
print(floatingpoint("1.5"))
# 111
# 10000

