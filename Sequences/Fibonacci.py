def Fibonacci(n):
    f_seq = [0, 1]
    for i in range(2, n+1):
        f_seq[i%2] = f_seq[0] + f_seq[1]
    return f_seq[n%2]
print(Fibonacci(1))