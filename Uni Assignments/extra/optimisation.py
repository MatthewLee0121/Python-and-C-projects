def printLine():
    print('----------------------------------------------------------------------------------------------------------')
    print("")
    print("")

def title():
    printLine()
    print("                 Optimisation                    ")
    printLine()

def typesofproblems():
    printLine()
    print("Types of Optimisation problems")
    print(f"""
          Definition: Optimisation is the process of finding the best  solution under given constraints.
          1) Linear vs. Non-linear
          2) Unconstrained vs. Constrained
          3) Single-objective vs. Multi-objective
    """)
    printLine()

def lvnl():
    return 0
def ucvc():
    printLine()
    print("""2) Unconstrained vs. Constrained
          Unconstrained--> 
                minimise: f(x) = x^2
          constrained---> 
                minimise: f(x)=x^2 
                subject to x>= 1
""")
    printLine

def sovmo():
    return 0

def optilib():
    printLine()
    print("""Key libraries:
          i) scipy.optimize: Core Python Libraries
""")
    printLine()
    print("""Example of scipy optimise minimize:
          
          """)
    scipyoptminiexample()
    printLine()


def scipyoptminiexample():
    print("""from scipy.optimize import minimize
    
    def objective(x):
        return x[0]**2 + x[1]**2
    
    x0= [1, 1]

    result = minimize(objective, x0)
    print("Optimal Solution: ", result.x)
    print("Objective Function Value:", result.fun)
    """)
    print("""output:
          Optimal Solution: [-2.1308950e-08, 2.1308950e8]
           Objective Function Value:2.1233545e-16""")
    
def main():
    title()
    typesofproblems()
   # lvnl()
    ucvc()
    #sovmo()
    optilib()

if __name__ == "__main__":
    main()