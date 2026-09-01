import sys
import subprocess

# Get the Python file we want to test.
program = sys.argv[1]

# Get all the values that the user entered after the file name.
values = sys.argv[2:]

# Run the program once for each value.
for value in values:
    print(f'Input: "{value}"')

    try:
        # Run the target program with the current value.
        # Stop it if it runs for more than 2 seconds.
        result = subprocess.run(
            ["python3", program, value],
            timeout=2
        )

        # If the program finishes normally, mark it as a pass.
        if result.returncode == 0:
            print("PASS")

        # If the program crashes or exits with an error, mark it as an error.
        else:
            print("ERROR")

    # If the program takes too long, mark it as a timeout.
    except subprocess.TimeoutExpired:
        print("TIMEOUT")

    # Add a blank line between test results.
    print()