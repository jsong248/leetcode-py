def Tribonacci(n):
    t_seq = [0, 1, 1]
    for i in range(3, n+1):
        t_seq[i%3] = t_seq[0] + t_seq[1] + t_seq[2]
    return t_seq[n%3]
print(Tribonacci(4))