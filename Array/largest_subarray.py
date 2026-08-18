#Brute force
def largestSubArray(ar,target):
    n=len(ar)
    count=0
    for startindex in range(n):
        for endindex in range(startindex,n):
            sum=0
            for i in range(startindex,endindex+1):
                sum+=ar[i]
            if sum==target:
                count=max(count,endindex-startindex+1)

    return count

#Hashing

def largestSubArray2(ar,target):
    n=len(ar)
    count=0
    sum=0
    hash={}
    for i in range(n):
        sum+=ar[i]
        if sum==target:
            count=i+1
        dif=sum-target
        
        if dif in hash:
            count=max(count,i-hash[dif])

        if sum not in hash:
            hash[sum]=i

    return count

   
nums = [10, 5, 2, 7, 1, 9]
print(largestSubArray2(nums,15))