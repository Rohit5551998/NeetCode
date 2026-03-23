# QUESTION: Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
#
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
#
# Constraints:
# s and t consist of lowercase English letters.

"""
BRUTE FORCE:
1. Sort both strings s and t using sorted()
2. Compare the two sorted lists for equality
3. If equal, return True — otherwise return False
TC -> O(n log n), SC -> O(n)

BETTER:
1. Initialize a fixed-size array count of 26 zeros (one per lowercase letter)
2. Iterate through string s, increment count at index (ord(char) - ord('a'))
3. Iterate through string t, decrement count at index (ord(char) - ord('a'))
4. Iterate through count array, if any value is non-zero return False
5. If all counts are zero, return True
TC -> O(n + m), SC -> O(1) — fixed 26-element array, lower constant factor than hashmap

OPTIMAL:
1. Initialize an empty hashmap count to store character frequencies
2. Iterate through string s, for each char increment its count in the map
3. Iterate through string t, for each char decrement its count in the map
4. Iterate through the hashmap, if any value is non-zero return False
5. If all counts are zero, return True — strings are anagrams
TC -> O(n + m), SC -> O(1) — hashmap bounded by alphabet size (at most 26 keys), does not grow with input

KEY INSIGHT:
- Two strings are anagrams iff they have identical character frequencies — count up for one string, count down for the other, and check everything cancels to zero
"""


def is_anagram_brute(s: str, t: str) -> bool:
    resp = False
    if sorted(s) == sorted(t):
        resp = True
    return resp


def is_anagram_better(s: str, t: str) -> bool:
        count = [0]*26

        for i in range(0, len(s)):
            count[ord(s[i]) - ord('a')] += 1

        for i in range(0, len(t)):
            count[ord(t[i]) - ord('a')] -= 1

        resp = True
        for i in range(0, len(count)):
            if (count[i] != 0):
                resp = False
                break

        return resp


def is_anagram_optimal(s: str, t: str) -> bool:
    count = {}
    for i in range(0, len(s)):
        if s[i] not in count:
            count[s[i]] = 0
        count[s[i]] += 1

    for i in range(0, len(t)):
        if t[i] not in count:
            count[t[i]] = 0
        count[t[i]] -= 1

    resp = True
    for k, v in count.items():
        if v != 0:
            resp = False
            break
    return resp
