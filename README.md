# thetool

A lightweight Python command-line tool for quickly testing how a program behaves across normal, unusual, and invalid inputs.

## What it does

`thetool` runs a target Python program with each input you provide and classifies the result as:

- `PASS` — the program finishes normally
- `ERROR` — the program raises an exception
- `TIMEOUT` — the program does not finish within the allowed time

This makes it useful for simple robustness testing and for quickly exploring edge cases without manually rerunning the same program over and over.

## Quick start

Make sure the Python program you want to test accepts its input from the command line.

For example, if `sqrt_program.py` is in the current directory:

```bash
uv sync --dev
uv run thetool sqrt_program.py 4 -1 hello 1000000
```

## Example output

```text
Input: "4"
The root of 4 is 2.0
PASS

Input: "-1"
TIMEOUT

Input: "hello"
ValueError: invalid literal for int() with base 10: 'hello'
ERROR

Input: "1000000"
The root of 1000000 is 1000.0
PASS
```

Exact error messages and file paths may vary by program and system.

## Why I built it

I built `thetool` to make repeated input testing faster and easier while learning about software testing, edge cases, input validation, and program behavior.
