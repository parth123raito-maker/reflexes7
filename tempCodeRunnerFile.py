nums = [2, 3, 9, 100, 9]
x = 9
idx = 0
while idx < len(nums):
    if nums[idx] == x:
        print("found ya=", idx)
        break
        idx += 1