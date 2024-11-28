import time

starttime = time.time()

def createString(num):
    print(num)
    emptyList = []
    for i in range(num + 1):
        emptyList.append(str(i))
    listIntoString = ' + '.join(emptyList)
    answer = 0
    for x in range(len(emptyList) + 1):
        answer += x #maxes out at 1700 numbers roughly
        if x > 9223372036854775807:
            print("max safe exceeded")
            break
    #answer = eval(listIntoString) #this works  9223372036854775807

    print(f'{listIntoString} = {answer}')

    return answer

for i in range(1, 1000000, 10000):
    createString(i)

endtime = time.time()
elapsed_time = endtime - starttime
print('Execution time:', elapsed_time, 'seconds')
