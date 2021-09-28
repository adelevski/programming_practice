
nums = [2,2,3,4]
# Output: 3

# nums = [4,2,3,4]
# Output: 4

def triangleNumber(nums):
    nums, count, n = sorted(nums), 0, len(nums)
    for i in range(2, n):
        left, right = 0, i-1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += (right - left)
                right -= 1
            else:
                left += 1
    return count


print(triangleNumber(nums))