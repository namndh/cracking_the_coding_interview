"""
URLify: Write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient space
at the end to hold the additional characters, and that you are given the "true" length of the string
"""


def solution(s: str, length: int) -> str:
    s = s.strip()
    return s.replace(" ", "%20")

