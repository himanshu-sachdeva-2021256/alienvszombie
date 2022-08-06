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
        dec=float("0."+str(dec))
        dec=float(dec)
        dec=dec*2
        final=final+str(dec)[0]
        dec=str(dec)[2:]
    return final

def btofloat(binary):
    decimal = 0
    i=1
    while (binary != 0):
        # print("#"+str(binary), end=" ")
        dec=int(str(binary)[0])
        decimal = decimal + dec * (0.5 ** i)
        i += 1
        binary = int(str(binary)[1:])
        # print("#"+str(binary))
    return decimal    

def exponent(num):
    num=int(num.split(".")[0])
    l=dtob(num)
    for i in range(len(l)):
        if l[i]=="1":
            break
    expo=3+len(l[i:])-1

    return [dtob(expo)[-8:],l[i:]]

def floatingpoint(num):
    dec=int(num.split(".")[1])
    expo,mane=exponent(num)
    dec=floattob(dec)
    # print(expo[-3:])
    # print((str(mane)+str(dec))[:5])
    return str(expo)[-3:]+(str(mane[1:])+str(dec))[:5]
    
def floattodecimal(num):
    expo=num[:3]
    mane=num[3:]
    # print(expo)
    # print(mane)
    i=binToDec(expo)-3
    # print(i)
    dexpo=(binToDec("1"+mane[:i]))
    dmane=(btofloat(mane[i:]))
    return (float(dexpo)+float(dmane))

print(floatingpoint("1.5"))
print("!!")

# check statement
print(floattodecimal(floatingpoint("5.25")))