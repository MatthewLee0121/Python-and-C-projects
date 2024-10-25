#automate sin cos tan graph transformations

def insidebracket():
    #grabbing values
    xCoef = int(input("what is the coefficient of x inside the bracket? "))
    xAddition = int(input("what is the amount added inside the bracket? "))
    xAddition = xAddition * -1
    xCoef = 1 / xCoef

    return xCoef, xAddition

def outsidebracket():
    #grabbing values
    outCoef = int(input("what value are you multiplying by outside the bracket? "))
    outAddition = int(input("what value are you adding by outside the bracket? "))

    return outCoef, outAddition

def identifytrigfunc():
    #are we dealing with sin cos tan?
    trigfunc = input("sin, cos or tan? ")

    return trigfunc

equationvalues = [insidebracket(), outsidebracket(), identifytrigfunc()]
print(equationvalues)