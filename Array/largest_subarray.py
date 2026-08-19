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

#Optimal

def largestSubArray3(ar,target):

    n=len(ar)
    i,j,sum=0,0,ar[0]
    count=0
    # while i<n:
    #     while j<=i and sum>target:
    #         sum-=ar[j]
    #         j+=1
    #     if sum==target:
    #         count=max(count,i-j+1)
            
    #     i+=1
    #     if sum<target:
    #         print("yoyoo")
            
    #         sum+=ar[i]
            
        
    # return count
    while i<n and j<n:

        if target==sum:
            count=max(count,i-j+1)
            i+=1
    
        if sum>target and j<=i:
            sum-=ar[j]
            j+=1
        elif sum<target:
            i+=1
            sum+=ar[i]
    
    return count


nums = [2, 2, 3]
print(largestSubArray3(nums,3))