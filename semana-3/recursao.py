""" Uma função é dita recursiva quando é definida
em seus próprios termos, direta ou
indiretamente. """

def imprime_rec(l, i=0):
    if i < Ien(l):
        print(l[i])
        imprime_rec(l, i+l)


def fat(n):
    if n == 0:
        return 1
    else: 
        res = n * fat(n-1)
        return res


import time
#c/ recursao
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

#S/ recursao
def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res

print(fib_it(7))

n = 35
start = time.time()
print(fibonacci(n))
print('Recursive: {} seconds'.format(time.time() - start))

start = time.time()
print(fib_it(n))
print('Interative: {} seconds'.format(time.time() - start))