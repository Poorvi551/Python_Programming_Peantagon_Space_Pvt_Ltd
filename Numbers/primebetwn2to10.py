# WAP to print the prime number between the range 2 to 10
def prime_between_two_ten():
    for i in range(2,11):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,end=' ')
print(prime_between_two_ten())