def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

numero = int(input("Informe um número: "))
fib_seq = fibonacci(numero)

if numero in fib_seq:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
