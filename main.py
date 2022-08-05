from interpreter import Interpreter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="file to interpret")

args = parser.parse_args()
run = True

if args.file:
    with open(args.file, "r") as file:
        code = file.read()
        Interpreter.interpret(code)
else:
    print("""
        NumberScript Shell: Type 'exit' to exit.
        Version: 1.0
    """)
    while run:
        code = input(">")
        if code == "exit":
            run = False
        else:
            Interpreter.interpret(code)