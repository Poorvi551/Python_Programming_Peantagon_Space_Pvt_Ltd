# WAP to find the largest word in the string
def largest_word(s):
    word=s.split()
    large=''
    for i in word:
        if len(i)>len(large):
            large=i
    return large
s=input("Enter string:")
print(largest_word(s))