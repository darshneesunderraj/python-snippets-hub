"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Approach: HashMap to store visited elements and their indices
"""

def twoSum(nums, target):
    num_map = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

print(twoSum([2, 7, 11, 15], 9))  
