def factorial_loop(n):
    if n<0:
        return "factorial is not defiend for negative integers"
    result=1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial_loop(5))
print(factorial_loop(4))
