---
name: solve
description: Set up a NeetCode problem and guide the user through solving it without giving the solution
---

# Solve a NeetCode Problem

## Arguments
- `<problem-name>`: Name of the problem (e.g., "Two Sum", "Valid Anagram")
- `<section>`: Section directory (e.g., "arrays-and-hashing", "two-pointers")

## Workflow

1. **Fetch the problem statement** — use WebSearch to look up the exact problem on NeetCode/LeetCode. Extract:
   - Problem description
   - All examples with input/output
   - Constraints

   If web search fails, ask the user to paste the problem statement. NEVER guess from memory.

2. **Create the solution file** at `<section>/<problem-name-kebab>.py` with the question comment block at the top followed by the notes template:

```python
# QUESTION: <Problem Name>
# <problem description line 1>
# <problem description line 2>
# ...
# Example 1:
# Input: ...
# Output: ...
#
# Constraints:
# ...

"""
BRUTE FORCE:
- Approach:
- Time: O()
- Space: O()

BETTER:
- Approach:
- Time: O()
- Space: O()

OPTIMAL:
- Approach:
- Time: O()
- Space: O()

KEY INSIGHT:
-
"""
```

   The `# QUESTION:` block is the single source of truth for problem text — it syncs to the tracker UI via `sync_notes.py`.

3. **Present the problem** to the user from the fetched data (description, examples, constraints).

4. **Guide without solving:**
   - Ask the user what their first instinct is
   - If they're stuck, give a **hint** (e.g., "Think about what data structure lets you do O(1) lookups")
   - If they propose an approach, confirm if it's correct and ask about the complexity
   - Nudge toward better approaches with questions, not answers (e.g., "Can you do better than O(n^2)? What if you sorted first?")
   - NEVER write the solution code — the user must write it themselves

5. **After the user writes their solution:**
   - Run checks: `python3 -m ruff format <file>` && `python3 -m ruff check <file>` && `python3 -m mypy <file>`
   - Fix any lint/type issues together
   - Ask the user to fill in the notes template with the approaches they considered

6. **Do NOT:**
   - Write or complete the solution function
   - Give away the optimal approach directly
   - Skip ahead if the user hasn't attempted it yet
