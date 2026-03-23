# QUESTION: Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

"""
#Brute Force:
1. Use two nested loops — outer loop picks each element, inner loop compares it with every subsequent element
2. If any pair matches (nums[i] == nums[j]), set resp = True and break
3. Return resp
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Initialize an empty hashmap (dict) to store element counts
2. Loop through array, for each element increment its count in hashmap
3. If count of any element exceeds 1, return True immediately (break early)
TC -> O(n), SC -> O(n)

#Optimal Approach:
1. Initialize an empty hash set to track seen elements
2. Loop through the array, for each element check if it already exists in the set
3. If it exists, set resp = True and break (duplicate found)
4. If not, add it to the set and continue
TC -> O(n), SC -> O(n)

#KEY INSIGHT:
- A hash set gives O(1) lookup for existence checks — you only need to know if you've seen an element before, not how many times, making a set the ideal data structure over a counting hashmap
"""


# Brute Force
def has_duplicate_brute(nums: list[int]) -> bool:
    resp = False
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                resp = True
                break
    return resp


# Better - Hashmap count with early break
def has_duplicate_better(nums: list[int]) -> bool:
    count: dict[int, int] = {}
    resp = False
    for i in range(0, len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 0
        count[nums[i]] += 1

        if count[nums[i]] > 1:
            resp = True
            break

    return resp


# Optimal
def has_duplicate_optimal(nums: list[int]) -> bool:
    dup: set[int] = set()
    resp = False
    for i in range(0, len(nums)):
        if nums[i] not in dup:
            dup.add(nums[i])
        else:
            resp = True
            break
    return resp
