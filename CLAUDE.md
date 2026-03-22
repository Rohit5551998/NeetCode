# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

NeetCode problem solutions in Python and system design notes. Started with NeetCode 150, may expand beyond.

## Directory Structure

Each directory corresponds to a NeetCode section. Solutions go in the matching section directory.

18 coding section directories (e.g., `arrays-and-hashing/`, `trees/`, `1d-dynamic-programming/`) and 4 system design directories under `system-design/`.

## Conventions

- Language: Python
- Solution files: named after the problem (e.g., `two-sum.py`, `valid-anagram.py`)
- New sections can be added as directories when expanding beyond NeetCode 150
- Every solution file MUST start with a multi-line comment block documenting approaches:

```python
"""
BRUTE FORCE:
- Approach: <description>
- Time: O()
- Space: O()

BETTER:
- Approach: <description>
- Time: O()
- Space: O()

OPTIMAL:
- Approach: <description>
- Time: O()
- Space: O()

KEY INSIGHT:
- <core idea that makes the optimal solution work>
"""
```

- Fill in all approaches considered, not just the one implemented
- The same notes should match what's in the tracker (index.html)
- All functions must have type annotations

## Workflow

- `/solve <problem-name> <section>` — creates the file, guides you with hints, but does NOT write the solution for you
- `/validate <file-path>` — classifies your solution as brute force, better, or optimal with complexity analysis and hints to improve

## Hooks (automatic)

- **PostToolUse**: Auto-runs `ruff format` + `ruff check --fix` on every `.py` file after edit
- **PreToolUse**: Blocks edits to `index.html` (tracker) — requires user confirmation

## Git

- Do NOT add Co-Authored-By lines in commits

## Commands

```bash
ruff check .          # lint
ruff check . --fix    # lint and auto-fix
ruff format .         # format all files
ruff format --check . # check formatting without changing
mypy .                # type check
```
