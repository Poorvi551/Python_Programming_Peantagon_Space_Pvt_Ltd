def sum_nat(n):
    if n==1:
        return 1
    return n*sum_nat(n-1)
print(sum_nat(4 ))