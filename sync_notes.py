#!/usr/bin/env python3
"""Sync docstrings from .py solution files into index.html DATA entries."""

from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).parent


def extract_docstring(py_file: Path) -> str | None:
    """Extract the module-level docstring from a .py file."""
    source = py_file.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    docstring = ast.get_docstring(tree)
    return docstring if docstring else None


def filename_to_key(filename: str) -> str:
    """Convert filename to a normalized key for matching.

    e.g. 'contains-duplicate.py' -> 'containsduplicate'
    """
    return re.sub(r"[^a-z0-9]", "", filename.removesuffix(".py").lower())


def problem_name_to_key(name: str) -> str:
    """Convert problem name to a normalized key for matching.

    e.g. 'Contains Duplicate' -> 'containsduplicate'
         'Two Sum II' -> 'twosumii'
    """
    return re.sub(r"[^a-z0-9]", "", name.lower())


def escape_for_js(text: str) -> str:
    """Escape a string for embedding in a JS string literal."""
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("\n", "\\n")
    text = text.replace("\r", "")
    return text


def is_fully_solved(py_file: Path) -> bool:
    """Check if all 3 approaches (_brute, _better, _optimal) are implemented."""
    source = py_file.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    suffixes = ("_brute", "_better", "_optimal")
    found: dict[str, ast.FunctionDef] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for s in suffixes:
                if node.name.endswith(s):
                    found[s] = node
    if len(found) != 3:
        return False
    # Check none of them are just `pass`
    for node in found.values():
        body = node.body
        # Skip docstring if present
        stmts = (
            body[1:]
            if (
                body
                and isinstance(body[0], ast.Expr)
                and isinstance(body[0].value, ast.Constant)
                and isinstance(body[0].value.value, str)
            )
            else body
        )
        if len(stmts) == 1 and isinstance(stmts[0], ast.Pass):
            return False
    return True


def collect_solutions() -> tuple[dict[str, str], set[str]]:
    """Collect docstrings and solved status from .py files."""
    notes: dict[str, str] = {}
    solved: set[str] = set()
    for py_file in ROOT.glob("*/*.py"):
        key = filename_to_key(py_file.name)
        docstring = extract_docstring(py_file)
        if docstring:
            notes[key] = docstring
        if is_fully_solved(py_file):
            solved.add(key)
    return notes, solved


def sync() -> int:
    """Sync docstrings and solved status into index.html. Returns count of updated entries."""
    notes, solved = collect_solutions()
    if not notes and not solved:
        return 0

    index_path = ROOT / "index.html"
    html = index_path.read_text()

    updated = 0
    problem_pattern = re.compile(r'\{ name: "([^"]+)"(.*?)\}(\s*[,\]])', re.DOTALL)

    def replace_entry(match: re.Match[str]) -> str:
        nonlocal updated
        name = match.group(1)
        rest = match.group(2)
        suffix = match.group(3)
        key = problem_name_to_key(name)

        if key not in notes and key not in solved:
            return match.group(0)

        # Remove existing n and s fields if present
        rest_clean = re.sub(r',\s*n:\s*"(?:[^"\\]|\\.)*"', "", rest)
        rest_clean = re.sub(r",\s*s:\s*true", "", rest_clean)

        extras = ""
        if key in notes:
            extras += ', n: "' + escape_for_js(notes[key]) + '"'
        if key in solved:
            extras += ", s: true"

        updated += 1
        return '{ name: "' + name + '"' + rest_clean + extras + "}" + suffix

    html = problem_pattern.sub(replace_entry, html)
    index_path.write_text(html)
    return updated


if __name__ == "__main__":
    count = sync()
    print(f"Synced {count} problem note(s) to index.html")
