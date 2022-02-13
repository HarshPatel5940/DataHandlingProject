from os import system as cmd
from sys import executable as check

from MainLoop import LibProject as Project

# INSTALL REQUIREMENTS:
# 1. Python 3.6+
# 2. termcolor
# 3. pandas

# Possible Problems:
# To run in Linux use (python3 main.py)
# Check all the file paths in config.py


if __name__ == "__main__":
    if "pythonw.exe" in f"{check}":
        cmd("start main.py")
    else:
        Project()
