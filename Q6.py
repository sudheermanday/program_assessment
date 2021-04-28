s=input("Please enter a sentence:").split()
for i in range(len(s)):
    s[i]=s[i][::-1]
str1=" ".join(s)
print(str1)