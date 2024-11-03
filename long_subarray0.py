
def longest_subarray(arr):
    l=[]
    i=0
    while i<len(arr)-1:
        p=False
        m=1
        while arr[i]==arr[i+1] :
            p=True
            m+=1
            i+=1 
            if  i<len(arr)-1:
                break

        if p==True:
            l.append(m)
        i+=1 
    max1=1
    for i in l:
        if max1<i:
            max1=i
    return max1
l=[]
for i in range(10):
    t=int(input("enter number "))
    l.append(t)

m=longest_subarray(l)




        

