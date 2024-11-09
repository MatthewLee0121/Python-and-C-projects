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

createString(50000)

endtime = time.time()
elapsed_time = endtime - starttime
print('Execution time:', elapsed_time, 'seconds')