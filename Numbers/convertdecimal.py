# WAP to convert binary to decimal
def convert_decimal(n):
    n = str(n)          # treat binary as string
    dec = 0
    power = 0
    for i in range(len(n)-1, -1, -1):   # right to left
        dec += int(n[i]) * (2 ** power)
        power += 1
    return dec

n = int(input("Enter binary num: "))
print(convert_decimal(n))