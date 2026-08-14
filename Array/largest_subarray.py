def largestSubArray(ar,target):
    sum=0
    cnt=0
    cur=0
    for num in ar:
        sum+=num
        cur+=1
        if sum==target:
            sum=num
            if cur>cnt:
                cnt=cur
            cur=1
    return cnt
nums = [-3, 2, 1]
print(largestSubArray(nums,15))