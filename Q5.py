s=input("please enter the string:")
flag=True
for i in s:
    if i>='0' and i<='9':
        continue
    else:
        flag=False
        break
if flag:
    print("String contains only digis")
else:
    print("String contains characters")