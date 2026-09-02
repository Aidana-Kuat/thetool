import sys
import subprocess


def main():
    # Check that the user gave a program and at least one value.
    if len(sys.argv) < 3:
        print("Usage: thetool program.py value1 value2 ...")
        return

    # Get the program we want to test.
    program = sys.argv[1]

    # Get all the test values.
    values = sys.argv[2:]

    # Run the program once for each value.
    for value in values:
        print(f'Input: "{value}"')

        try:
            result = subprocess.run(
            [sys.executable, program, value],
            timeout=2
            )

            if result.returncode == 0:
                print("PASS")
            else:
                print("ERROR")

        except subprocess.TimeoutExpired:
            print("TIMEOUT")

        print()