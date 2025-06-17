"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Approach: Sliding window using HashSet
"""

def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))  
