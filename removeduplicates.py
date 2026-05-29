def rem_duplicate(l):
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
    return out
l=eval(input("Enter list:"))
print(rem_duplicate(l))
