# wap to find the duplicate characters from given string
def duplicate_char(s):
    dup=''
    res=''
    for i in s:
        if i in res:
            dup+=i
        else:
            res+=i
    return dup
s=input("Enter string:")
print(duplicate_char(s))