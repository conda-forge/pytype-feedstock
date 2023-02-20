"""
A short script to run pytype with a real file to check

This should catch whether you can actually run pytype

(in particular if pytypw works with the conda-installed ninja)

NOTE: I suppose it would be more robust to see if it actually
      does the check correctly, but that's really pytype's problem
"""
import sys
import subprocess
from pathlib import Path

TEST_FILE = """

def fun(x: int):
    return x * 2

# this should type check with no errors
y = fun(2)

# this should type check with an error
# z = fun(2.0)
"""

filepath = Path("python_test_file.py")

with open(filepath, 'w', encoding='utf-8') as pyfile:
    pyfile.write(TEST_FILE)

try:
    subprocess.check_call(("pytype", str(filepath)))
    # it worked
    sys.exit(0)
except subprocess.CalledProcessError:
    # something went wrong
    print("Something went wrong running pytype")
    raise
finally:
    filepath.unlink(missing_ok=False)



