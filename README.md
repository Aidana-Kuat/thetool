# thetool

A small Python CLI for testing how a program behaves with different input values.

You can give it any values you want, and `thetool` will run the program with each one and report whether it: finishes normally (`PASS`), produces an error (`ERROR`), takes too long — (`TIMEOUT`).

## Quick start
Make sure sqrt_program.py is in the current folder. 
Then run: 

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
Traceback (most recent call last):
  File "/Users/.../sqrt_program.py", line 20, in <module>
    ...
ValueError: invalid literal for int() with base 10: 'hello'
ERROR

Input: "1000000"
The root of 1000000 is 1000.0
PASS
```

The exact error message and file path may be different depending on the program and computer being used.

`thetool` is useful for quickly trying normal, unusual, and invalid inputs to see how a Python program responds.

The program being tested should accept its input from the command line.
