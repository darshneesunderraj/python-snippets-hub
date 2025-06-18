# Problem: Check if two strings are anagrams
def is_anagram(s, t):
    return sorted(s) == sorted(t)

# Example
print(is_anagram("listen", "silent"))  # Output: True
