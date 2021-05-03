from collections import defaultdict

"""
Check permutation. Given two strings, write a method to decide if one is permutation of the other
"""

"""
Solution 1: we can separate the input strings as list then sort these lists then we compare these to sorted lists
- Complexity is O(NlogN + MlogM)
"""


def solution(s1: str, s2: str) -> bool:
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    return s1 == s2


"""
Solution 2: we can count map to count occurrences of every characters in each input strings. Two input strings are 
permutation of each others while the map of each input string contains the same characters with the same occurrences
"""


def solution1(s1: str, s2: str) -> bool:
    count_map1 = defaultdict(int)
    count_map2 = defaultdict(int)
    for char in s1:
        count_map1[char] += 1
    for char in s2:
        count_map2[char] += 1
    for char in s1:
        if char not in s2 or count_map1[char] != count_map2[char]:
            return False
    for char in s2:
        if char not in s1 or count_map1[char] != count_map2[char]:
            return False
    return True


print(solution('abc', 'abce'))
print(solution1('abc', 'abce'))
