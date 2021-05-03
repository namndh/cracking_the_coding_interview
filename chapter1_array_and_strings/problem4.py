from collections import defaultdict
"""
Palindrome Permutation: Given a string, write a function to check if it is a permutations of a palindrome.
"""

"""
A string that can create a palindrome iff:
- all char in string must occurs an even number of times
- there is only one char in string occur an odd number of times
To solve this problem, we can create a hash map count of occurrences of all char in the input string, and ensure there
is no char occurs an odd numbers
"""


def solution(s: str) -> bool:
    count_map = defaultdict(int)
    count_odd = 0
    s = s.lower()
    for char in s:
        if ord(char) >= 97:
            count_map[char] += 1
            if count_map[char] % 2 == 0:
                count_odd -= 1
            else:
                count_odd += 1
    print(count_map)
    print(count_odd)
    return count_odd <= 1


print(solution("Do geese see God?"))
