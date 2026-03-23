# QUESTION: Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.
#
# Example 1:
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
#
# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
#
# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
# Only one valid answer exists.

"""
BRUTE FORCE:
1. Use two nested loops — outer loop picks element i, inner loop picks element j (starting from i+1)
2. Check if nums[i] + nums[j] == target
3. If match found, store [i, j] as result
4. Return the result
TC -> O(n^2), SC -> O(1)

BETTER:
1. Copy the array, then sort it
2. Use two pointers (l=0, r=len-1) on the sorted array
3. If sum == target, record sorted indices and break
4. If sum < target, move left pointer right; if sum > target, move right pointer left
5. Map the sorted indices back to original array indices by scanning original array
TC -> O(n log n), SC -> O(n)

OPTIMAL:
1. Initialize an empty hashmap to store {value: index}
2. Iterate through array, for each element compute complement = target - nums[i]
3. If complement exists in hashmap, return [hashmap[complement], i]
4. Otherwise, store nums[i] -> i in the hashmap
TC -> O(n), SC -> O(n)

KEY INSIGHT:
- For each element, the "partner" it needs is (target - current). A hashmap lets you check in O(1) if you've already seen that partner, turning a two-loop search into a single pass.
"""


def two_sum_brute(nums: list[int], target: int) -> list[int]:
    resp = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                resp = [i, j]
    return resp


def two_sum_better(nums: list[int], target: int) -> list[int]:
    resp = []
    ans = []
    a = nums
    nums = sorted(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            resp = [l, r]
            break
        if nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1

    for i in range(0, len(a)):
        if a[i] == nums[resp[0]] or a[i] == nums[resp[1]]:
            ans.append(i)

    return ans


def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    map = {}
    resp = []
    for i in range(0, len(nums)):
        if target - nums[i] in map:
            resp = [map[(target - nums[i])], i]
            break
        map[nums[i]] = i
    return resp
