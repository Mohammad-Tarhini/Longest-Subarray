"""Finds the length of the longest subarray with an equal number of 0s and 1s."""
def long_subarray(arr):
    max_length=0
    i=0
    while i<len(arr):
        j=len(arr)-1
        while j>=i:
            sum=0
            for k in range(i,j+1):
                if arr[k]==0:
                    sum-=1
                else:
                    sum+=1
            if sum==0:
                max_length=max(max_length,j+1-i)
                break   
            
            j-=1
        i+=1
    return max_length