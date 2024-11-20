import time

starttime = time.time()

def createString(num):
    emptyList = []
    for i in range(num + 1):
        emptyList.append(str(i))
    listIntoString = ' + '.join(emptyList)
    answer = eval(listIntoString)

    print(f'{listIntoString} = {answer}')

    return answer

for i in range(1, 1000, 10):
    createString(i)

endtime = time.time()
elapsed_time = endtime - starttime
print('Execution time:', elapsed_time, 'seconds')
