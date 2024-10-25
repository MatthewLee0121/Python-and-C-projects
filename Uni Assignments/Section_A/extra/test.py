#automate sin cos tan graph transformations

def insidebracket():
    #inside the bracket opposite
    xCoef = int(input("what is the coefficient of x? "))
    xaddition = int(input("what is the amount added or subtracted? remember to include the sign "))
    xaddition = xaddition * -1
    xCoef = 1 / xCoef

insidebracket()

def indetifytrigfunc():
    trigfunc = input("sin, cos or tan? ")

    return trigfunc