import time

starttime = time.time()

def createString(num):
    emptyList = []
    for i in range(num + 1):
        emptyList.append(str(i))
    listIntoString = ' + '.join(emptyList)
    answer = 0
    for x in range(len(listIntoString) + 1):
        answer += x #maxes out at 1700 numbers roughly
    
    #answer = eval(listIntoString) #this works

    print(f'{listIntoString} = {answer}')

    return answer

for i in range(1, 10000000):
    createString(i)

endtime = time.time()
elapsed_time = endtime - starttime
print('Execution time:', elapsed_time, 'seconds')
