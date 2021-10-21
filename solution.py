
def minDistance(nums,min , max):
    n = len(nums)
    print(min,max)
    dist=999999999      # Initializing a big value for the distance
    if min==max:
        return 1
    else:
        for i in range(n):
            for k in range(i+1, n):
                if (min ==nums[i]and max== nums[k] or max==nums[i] and min == nums[k]) and dist> abs(i-k):
                    dist = abs(i-k)
                    return abs(i-k)



def locate_minandmax(nums):
    min = nums[0]
    max= nums[0]
    n = len(nums)

    for i in range(0, n):
        if nums[i]>max:
            max=nums[i]
        elif nums[i]<min:
            min =nums[i]
    return minDistance(nums, min,max)
