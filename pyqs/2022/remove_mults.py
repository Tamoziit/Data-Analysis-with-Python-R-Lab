nums = [2, 4, 5, 6, 11, 16]

res = [x for x in nums if x % nums[0] != 0 or x == nums[0]]

print(nums)
print(res)