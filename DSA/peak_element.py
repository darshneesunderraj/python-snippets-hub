"""
Problem: Find Peak Element
Link: https://leetcode.com/problems/find-peak-element/
Approach: Binary search on index
"""

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid  # peak is in the left half
        else:
            left = mid + 1  # peak is in the right half

    return left  # or right


print(findPeakElement([1, 2, 3, 1]))  
