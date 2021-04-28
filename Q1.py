n=int(input("what is the element you wnat to remove:"))
a=[]
for i in  range(0,100):
    if n==i+1:
        continue
    a.insert(i, i+1)
sum1=sum(a)
sum2=100*101/2
print("the element went missing is:",int(sum2-sum1))