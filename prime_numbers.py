limit=int(input("Enter the limit: "))
print("Prime numbers between 1 and",limit,"are:")
for num in range(1,limit+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)