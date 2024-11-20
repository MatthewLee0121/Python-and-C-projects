import time

starttime = time.time()

def signChange(a, b):
    if a * b < 0:
        return True
    return False

def midpoint(x1, x2):
    return (x1 + x2) / 2

def outputOfFx(x):
    return (x ** 2) - (3 * x) + 2

def bisectionMethod(f, a, b, tolerance=1e-6, max_iterations=100):
    if not signChange(f(a), f(b)):
        raise ValueError(f"The return of the function at the points a:{a} = {f(a)}, b:{b} = {f(b)} does not have a sign change, this implies 0 or multiple roots.")

    for i in range(max_iterations):
        mid = midpoint(a, b)
        f_mid = f(mid)
        
        if abs(f_mid) < tolerance:
            return mid
        
        if signChange(f(a), f_mid):
            b = mid
        else:
            a = mid
    
    return midpoint(a, b)

root = bisectionMethod(outputOfFx, 1.5, 4)
print("Root found:", root)

endtime = time.time()
elapsed_time = endtime - starttime
print('Execution time:', elapsed_time, 'seconds')