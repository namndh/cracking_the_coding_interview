"""
One Away. There are three types of edits that can be performed on stings: insert a character, remove a character,
remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

"""

"""
Ideas:
- We will check for each transformation:
    - Insert transformation: len(s2) - len(s1) == 1 and s1 contains all char of s2
    - Remove transformation: len(s1) - len(s2) == 1 and s2 contains all char of s1
    - Replace transformation: len(s1) == len(s2). s2 contains len(s1) - 1 char of s1
"""