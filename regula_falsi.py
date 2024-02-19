import numpy as np

def regula_falsi(xLower, xUpper, func):
    maxInt = 100000
    epsilon = np.finfo(float).eps
    ulp = np.finfo(float).tiny

    #cache the result of func(xLower) and func(xUpper)
    f_lower = func(xLower)
    f_upper = func(xUpper)

    #validate bracket
    if(f_lower * f_upper > 0):
        return None, -1, None, None
    
    #Check the bounds for a root
    if(f_lower == 0):
        return xLower, 0, f_lower, 0
    
    if(f_upper == 0):
        return xUpper, 0, f_upper, 0
    
    #Initialize root snd iteration counter
    root = xLower
    iteration = 0

    #Calculate a new approximated root using the regula falsi formula in loop with maxInt upper iteration bound
    for _ in range(maxInt):
        root_prev = root
        
        f_xLower = func(xLower)
        f_xUpper = func(xUpper)

        root = xUpper - (f_xUpper * (xLower - xUpper)) / (f_xLower - f_xUpper)
        f_root = func(root)

        iteration += 1

        #update the bounds
        if(f_xLower * f_root < 0):
            xUpper = root
        else:
            xLower = root

        #check our conditions for convergence
        if(abs(f_root) < epsilon or abs(root - root_prev) < ulp):
            return root, 0, f_root, iteration
        
    return root, 0, f_root, iteration

def TestFuncOne(x):
    return (x ** 4) - (6 * x ** 3) + (12 * x ** 2) - (10 * x) + 3

def TestFuncTwo(x):
    return (x ** 3) - (7 * x ** 2) + (15 * x) - 9

if __name__ == '__main__':
    print("Testing Regula Falsi on Test Function One")
    print(regula_falsi(1.5, 2.5, TestFuncOne))
    print(regula_falsi(0, 1.5, TestFuncOne))

    print("Testing Regula Falsi on Test Function Two")
    print(regula_falsi(1.5, 2.5, TestFuncTwo))
    print(regula_falsi(0, 1.5, TestFuncTwo))