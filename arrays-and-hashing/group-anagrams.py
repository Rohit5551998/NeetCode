# QUESTION: Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
#
# Example 3:
# Input: strs = [""]
# Output: [[""]]
#
# Constraints:
# 1 <= strs.length <= 1000
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

"""
BRUTE FORCE:
1. Initialize a list of groups and a visited set to track already-grouped strings
2. For each unvisited string, start a new group with it
3. Compare it against every other unvisited string by sorting both and checking equality
4. If they match, add to the current group and mark as visited
5. Append the group to the result
TC -> O(n^2 * m log m), SC -> O(n * m)

BETTER:
1. Initialize an empty hashmap to store groups (key -> list of strings)
2. For each string, sort its characters and join them to form a key
3. If the key doesn't exist in the map, create a new empty list for it
4. Append the original string to the list mapped by that sorted key
5. Iterate over the hashmap values and collect all groups into the result
TC -> O(m * n log n), SC -> O(m * n)
where m = number of strings, n = length of longest string

OPTIMAL:
1. Initialize an empty hashmap to store groups (key -> list of strings)
2. For each string, create a size-26 array of zeros (one slot per lowercase letter)
3. For each character in the string, increment the count at index (ord(char) - ord('a'))
4. Convert the frequency array to a dash-separated string to use as the hashmap key
5. If the key doesn't exist in the map, create a new empty list for it
6. Append the original string to the list mapped by that frequency key
7. Reset the frequency array for the next string
8. Collect all hashmap values into the result
TC -> O(m * n), SC -> O(m * n)
where m = number of strings, n = length of longest string

KEY INSIGHT:
- Two strings are anagrams iff they have identical character frequency counts. A size-26 count array uniquely identifies an anagram group in O(n) instead of O(n log n) sorting.
"""


def group_anagrams_brute(strs: list[str]) -> list[list[str]]:
    # SKIP: impractical O(n^2 * m log m), documented in notes above
    pass


def group_anagrams_better(strs: list[str]) -> list[list[str]]:
    map = {}
    res = []
    for i in range(0, len(strs)):
        key = "".join(sorted(strs[i]))
        if key not in map:
            map[key] = []
        map[key].append(strs[i])

    for k, v in map.items():
        res.append(v)

    return res


def group_anagrams_optimal(strs: list[str]) -> list[list[str]]:
    map1 = {}
    res = [0] * 26
    for i in range(0, len(strs)):
        for j in range(0, len(strs[i])):
            res[ord(strs[i][j]) - ord("a")] += 1

        key = "-".join(map(str, res))
        if key not in map1:
            map1[key] = []
        map1[key].append(strs[i])
        res = [0] * 26

    resp = []
    for k, v in map1.items():
        resp.append(v)

    return resp
