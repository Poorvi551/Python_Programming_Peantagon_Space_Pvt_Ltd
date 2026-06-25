def ext_low(s,res='',i=0):
    if i>=len(s):
        return res
    if 'a'<=s[i]<='z':
        res=res+s[i]
    return ext_low(s,res,i+1)
s=input("Enter string:")
print(ext_low(s))