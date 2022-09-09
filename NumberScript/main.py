from . import interpreter
import argparse
import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

Interpreter = interpreter.Interpreter

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file to interpret")
parser.add_argument("-m", "--module", help="module to interpret", action="store_true")
parser.add_argument("-v", "--version", action="store_true", help="show version")
parser.add_argument("-d", "--debug", action="store_true", help="debug mode")
args = parser.parse_args()

ver = "1.13.0"

help = """
0 <- start
1 <- end
2thing <- print
3name:value <- var
4number[=/!/</>] <- Compare
5 <- pass
6 <- For-loops
7 <- Function Def
% <- comment
^number[+\-\/\*\#]number <- Math-Operation-Start
?condition|True|False <- If-Else
#path/to/file(don't put .ns at the end) <- Import
"""

def main():
    run = True

    space = ""

    for j in range(0, 16):
        space += " "

    for k in range(0, len(os.name)):
        space = space.replace(" ", "", 1)

    if args.file:
        with open(args.file, "r") as file:
            code = file.read()
            code = code.replace("\n", " ")
            if args.module:
                if args.debug:
                    print(Interpreter.interpret(Interpreter, code, library=True, debug=True))
                else:
                    print(Interpreter.interpret(Interpreter, code, library=True))
            else:
                if args.debug:
                    Interpreter.interpret(Interpreter, code, debug_mode=True)
                else:
                    Interpreter.interpret(Interpreter, code)

    elif args.version:
        print(f"Version: {ver}")
    else:
        print(f"""
            +------------------------------------------+
            | NumberScript Shell: Type 'exit' to exit. |
            | Version: {ver} Machine: {os.name}{space}|
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
                if args.debug:
                    Interpreter.interpret(Interpreter, code, debug_mode=True)
                else:
                    Interpreter.interpret(Interpreter, code)

if "__main__" == __name__:
    main()