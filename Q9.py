a=input("Please enter the elements with spaces between them:").split()
n=len(a)
for i in range(n):
    a[i]=int(a[i])
for i in range(n-1):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Sortes array :",a)