def sumVal(N):
    if N <= 0:
        return 0
    return N + sumVal(N - 1)

print(sumVal(4))

#The output will be "10"
