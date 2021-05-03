"""
Is unique. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional
data structure
"""


# Use with hash table data structure. Complexity O(N)


def solution(s: str) -> bool:
    char_map = {}
    for char in s:
        if char in char_map:
            return False
        else:
            char_map[char] = 1
    return True


""" 
Without additional data structure. We can use bruce force to solve this problem:
- We iterate each character in the input string. Then we iterate through the sub string from the element we are standing at
- If any same character occurs, we return False, if we iterate through all the element in the input string without any False,
we can return True
- Complexity: O(N^2)
"""


def solution1(s: str) -> bool:
    for i in range(len(s)):
        for char in s[i + 1:]:
            if s[i] == char:
                return False
    return True


print(solution("abcd"))
print(solution1("abcd"))
print(solution("avccs"))
print(solution1("avccs"))
