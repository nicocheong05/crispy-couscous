def sumTo(n):
    if n == 0:
        return 0
    return sumTo(n-1) + n


answer = sumTo(100)
print(answer)
