---
name: validate
description: Analyze a solution and classify it as brute force, better, or optimal with explanation
---

# Validate a Solution

## Arguments
- `<file-path>`: Path to the solution file (e.g., `arrays-and-hashing/two-sum.py`)

## Workflow

1. **Read the solution file** and identify the problem name from the filename/docstring.

2. **Look up the problem** — use WebSearch to find the exact problem on LeetCode/NeetCode to understand constraints and known optimal complexity. If web search fails, ask the user for the problem link. NEVER guess optimal complexity from memory.

3. **Analyze the current implementation:**
   - Identify the algorithm/approach used
   - Determine the time complexity (Big O)
   - Determine the space complexity (Big O)

4. **Classify the solution** as one of:

   | Classification | Criteria |
   |---------------|----------|
   | **BRUTE FORCE** | Naive approach, typically O(n^2) or worse, no clever data structures |
   | **BETTER** | Improved over brute force but not optimal (e.g., sorting-based O(n log n) when O(n) exists) |
   | **OPTIMAL** | Best known time/space complexity for this problem |

5. **Output a verdict** in this format:

   ```
   ## Verdict: [BRUTE FORCE / BETTER / OPTIMAL]

   **Your approach:** <one-line description of what the code does>
   **Time:** O(...)
   **Space:** O(...)

   **Why this classification:**
   - <explain why it falls into this category>

   **Can you do better?** [Yes/No]
   - <if yes, give a HINT not the answer — e.g., "Think about trading space for time" or "What data structure gives O(1) lookup?">
   ```

6. **If the solution is optimal:**
   - Confirm it and congratulate
   - Check if the notes template in the docstring is filled in — if not, remind the user to complete it

7. **Do NOT:**
   - Write or rewrite the solution
   - Give away the better/optimal approach directly — only hints
   - Change the code in any way
