def twoSum(nums, target):
    for i in range(len(nums)):
        if nums[i]+nums[i+1] == target:
            return [i, i+1]
print(twoSum([3,7,2,15],9))