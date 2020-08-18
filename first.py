n=int(input("Enter number of elements in main array: "))
print("Enter elements :")
arr1=[]
for i in range(0,n):
        z=int(input())
        arr1.append(z)

k=int(input("Enter size of window: "))
if(k<=n):
        for i in range(0,n):
                j=k
                p=i
                count=0
                while(j and (n-i>=k)):
                        if(arr1[p]<0):
                                print(arr1[p],end=" ")
                                count=1
                                break
                        else:
                                p=p+1
                                j=j-1
                if(count==0 and (n-i>=k)):
                        print(count,end=" ")
else:
        print("Not possible ")


