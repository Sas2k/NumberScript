class Interpreter():
    def __init__(self):
        pass

    def interpret(code: str) -> str:
        code = code.split(" ")
        codes = ""
        for i in range(len(code)):
            codes += code[i]
        code = codes.split("\n")
        variables = {}
        for j in range(0, len(code)):
            if code[j].startswith("0"):
                variables = {}
            
            if code[j].startswith("1"):
                variables = {}
                return

            if code[j].startswith("2"):
                if code[j][1:] in variables.keys():
                    for x in range(0, len(variables)):
                        var_names = list(variables.keys())
                        if var_names[x] == code[j][1:]:
                            print(variables[var_names[x]])

                else:
                    print(code[j][1:])

            if code[j].startswith("3"):
                vars = code[j].split(":")
                var_name = vars[0].replace("3", "")
                variables[var_name] = vars[1]

            if code[j].startswith("%"):
                continue
