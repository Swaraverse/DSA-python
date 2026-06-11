nums = [12,5,8,30,3]

largest = nums[0]

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]

print(largest)
