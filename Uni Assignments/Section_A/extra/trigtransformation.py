#automate sin cos tan graph transformations

def insidebracket():
    #inside the bracket opposite
    xCoef = int(input("what is the coefficient of x? "))
    xAddition = int(input("what is the amount added or subtracted? remember to include the sign "))
    xAddition = xAddition * -1
    xCoef = 1 / xCoef

def identifytrigfunc():
    trigfunc = input("sin, cos or tan? ")

    return trigfunc

print(insidebracket(), identifytrigfunc())
