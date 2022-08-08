from . import interpreter
import argparse
import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

Interpreter = interpreter.Interpreter

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file to interpret")
parser.add_argument("-v", "--version", action="store_true", help="show version")
args = parser.parse_args()

ver = "1.9.2"

run = True

help = """
0 <- start
1 <- end
2thing <- print
3name:value <- var
4number[=/!/</>] <- Compare
5 <- pass
6 <- For-loops
% <- comment
^number[+\-\/\*\#]number <- Math-Operation-Start
?conditon:True:False <- If-Else
"""

space = ""
for j in range(0, 16):
    space += " "

for k in range(0, len(os.name)):
    space = space.replace(" ", "", 1)

if args.file:
    with open(args.file, "r") as file:
        code = file.read()
        code = code.replace("\n", " ")
        Interpreter.interpret(Interpreter, code)
elif args.version:
    print(f"Version: {ver}")
else:
    print(f"""
        +------------------------------------------+
        | NumberScript Shell: Type 'exit' to exit. |
        | Version: {ver} Machine: {os.name} {space}|
        | Type 'help' for more information.        |
        | {current_time}                                 |
        +------------------------------------------+
    """)
    while run:
        code = input(">")
        if code == "exit":
            run = False
        elif code == "help":
            print(help)
        else:
            Interpreter.interpret(Interpreter, code)