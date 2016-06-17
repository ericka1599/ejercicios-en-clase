def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a
    
n = int(input("Ingrese el numero: "))
print (fibonacci(n))