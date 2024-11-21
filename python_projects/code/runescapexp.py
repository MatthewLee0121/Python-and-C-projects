#xp per hour = 75k 
#xp needed difference 1.02mill 4 mill

def getdifference(a, b):
    return a - b


# print(str(getdifference(4, 1.02)) + " million")   xp needed

def timedivide(a, b):
    return (a*(10**6)) / b

#print(getdifference(4, 1.02)*(10**6))
print(timedivide(getdifference(4, 1.02), 75000))