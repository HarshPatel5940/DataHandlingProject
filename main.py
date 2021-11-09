import sys
from Loop import Project
from os import system as cmd

# INSTALL REQUIREMENTS:
# 1. Python 3.6+
# 2. termcolor
# 3. pandas

# Possible Problems:
# Don't Run it in IDLE, it will not work as Intended.
# Check all the file paths in modules.py (line 6,7,8)


if __name__ == "__main__":
    if "pythonw.exe" in f"{sys.executable}":
        cmd("start main.py")
    else:
        Project()
