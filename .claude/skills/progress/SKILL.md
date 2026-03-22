---
name: progress
description: Show NeetCode 150 solve progress — how many problems solved per section, total stats, and what's next
disable-model-invocation: true
---

# Progress

Show a summary of solving progress across all NeetCode sections.

## Workflow

1. Run `python3 sync_notes.py` from the project root to get the latest state.

2. Run a Python script to analyze all `.py` solution files and report:

```python
import ast
from pathlib import Path

ROOT = Path(".")
sections = {}

for py_file in sorted(ROOT.glob("*/*.py")):
    if py_file.parent.name.startswith(".") or py_file.name == "sync_notes.py":
        continue
    section = py_file.parent.name
    if section not in sections:
        sections[section] = {"total": 0, "solved": 0, "partial": 0, "files": []}

    sections[section]["total"] += 1
    source = py_file.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        continue

    suffixes = ("_brute", "_better", "_optimal")
    implemented = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for s in suffixes:
                if node.name.endswith(s):
                    body = node.body
                    stmts = body[1:] if (body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str)) else body
                    if not (len(stmts) == 1 and isinstance(stmts[0], ast.Pass)):
                        implemented += 1

    if implemented == 3:
        sections[section]["solved"] += 1
    elif implemented > 0:
        sections[section]["partial"] += 1
        sections[section]["files"].append(f"  {py_file.name} ({implemented}/3)")

total_solved = sum(s["solved"] for s in sections.values())
total_partial = sum(s["partial"] for s in sections.values())
total_files = sum(s["total"] for s in sections.values())

print(f"## NeetCode Progress: {total_solved}/{total_files} solved, {total_partial} in progress\n")
for name, info in sections.items():
    status = f"{info['solved']}/{info['total']} solved"
    if info["partial"]:
        status += f", {info['partial']} in progress"
    print(f"- **{name}**: {status}")
    for f in info["files"]:
        print(f)
```

3. Display the output to the user in a clean format.
