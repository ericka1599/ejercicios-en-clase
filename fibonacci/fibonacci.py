def fib (num): 
    if num <= 2:
        return 1
    return fib(num-1) + fib(num-2)



num = int(input("Ingrese n: "))
print (fib(num))