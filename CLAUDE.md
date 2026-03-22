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
#Brute Force:
1. <step-by-step in pseudo-code + english>
TC -> O(), SC -> O()

#Better Approach:
1. <step-by-step in pseudo-code + english>
TC -> O(), SC -> O()

#Optimal Approach:
1. <step-by-step in pseudo-code + english>
TC -> O(), SC -> O()

#KEY INSIGHT:
- <core idea that makes the optimal solution work>
"""
```

- Each solution file has 3 separate functions: `<name>_brute`, `<name>_better`, `<name>_optimal`
- Only fill in notes for approaches the user has actually written — do NOT fill in or reveal approaches they haven't implemented yet
- Notes style: numbered steps in pseudo-code + english, with `TC -> O(), SC -> O()` at end (see Take-U-Forward-DSA repo for reference)
- Notes sync from .py docstrings to tracker (index.html) is automatic via `sync_notes.py` (runs as pre-commit hook)
- All functions must have type annotations

## Workflow

- `/solve <problem-name> <section>` — creates the file, guides you with hints, but does NOT write the solution for you
- `/validate <file-path>` — classifies your solution as brute force, better, or optimal with complexity analysis, hints to improve, and auto-syncs notes to both the `.py` file and tracker (`index.html` DATA `n` field)

## Hooks (automatic)

- **PostToolUse**: Auto-runs `ruff format` + `ruff check --fix` on every `.py` file after edit
- **PreToolUse**: Blocks edits to `index.html` (tracker) — requires user confirmation

## Lint Considerations

- `C0200` (consider-using-enumerate) is disabled — `for i in range(len(...))` is intentional in DSA code where index access matters
- Do NOT suggest `enumerate` replacements in solution files unless the user asks

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
