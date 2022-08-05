def Checker(re_code: str, variables: dict) -> bool:
    if "=" in re_code:
        code = re_code.split("=")
        if code[0] in variables:
            code[0] = variables[code[0]]
        if code [1] in  variables:
            code[1] = variables[code[1]]
        return code[0] == code[1]

    elif "!" in re_code:
        code = re_code.split("!")
        if code[0] in variables:
            code[0] = variables[code[0]]
        if code [1] in  variables:
            code[1] = variables[code[1]]
        return code[0] != code[1]

    elif "<" in re_code:
        code = re_code.split("<")
        if code[0] in variables:
            code[0] = variables[code[0]]
        if code [1] in  variables:
            code[1] = variables[code[1]]
        return code[0] < code[1]

    elif ">" in re_code:
        code = re_code.split(">")
        if code[0] in variables:
            code[0] = variables[code[0]]
        if code [1] in  variables:
            code[1] = variables[code[1]]
        return code[0] > code[1]


class Interpreter():
    def __init__(self):
        pass

    def interpret(self, code: str) -> str:
        code = code.split(" ")

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
                vars = code[j].replace("3", "", 1).split(":")
                var_name = vars[0]
                var_content = vars[1]
                variables[var_name] = var_content

            if code[j].startswith("^"):
                removed_code = code[j].replace("^", "")

                if "+" in removed_code:
                    removed_code = removed_code.split("+")
                    for x in range(0, len(removed_code)):
                        if removed_code[x] in variables.keys():
                            removed_code[x] = int(variables[removed_code[x]])
                        else:
                            removed_code[x] = int(removed_code[x])
                    print(sum(removed_code))

                elif "-" in removed_code:
                    removed_code = removed_code.split("-")

                    for x in range(0, len(removed_code)):
                        if removed_code[x] in variables.keys():
                            removed_code[x] = int(variables[removed_code[x]])
                        else:
                            removed_code[x] = int(removed_code[x])
                    
                    max_num = max(removed_code)
                    removed_code.pop(removed_code.index(max_num))

                    for j in range(0, len(removed_code)):
                        min_total = max_num - removed_code[j]

                    print(min_total)

                elif "*" in removed_code:
                    removed_code = removed_code.split("*")

                    for x in range(0, len(removed_code)):
                        if removed_code[x] in variables.keys():
                            removed_code[x] = int(variables[removed_code[x]])
                        else:
                            removed_code[x] = int(removed_code[x])
                    
                    product = 1
                    for j in range(0, len(removed_code)):
                        product *= removed_code[j]

                    print(product)

                elif "/" in removed_code:
                    removed_code = removed_code.split("/")

                    for x in range(0, len(removed_code)):
                        if removed_code[x] in variables.keys():
                            removed_code[x] = int(variables[removed_code[x]])
                        else:
                            removed_code[x] = int(removed_code[x])
                    
                    product = max(removed_code)
                    removed_code.pop(removed_code.index(product))
                    for j in range(0, len(removed_code)):
                        product = product / removed_code[j]

                    print(product)

            if code[j].startswith("%"):
                continue
            
            if code[j].startswith("4"):
                re_code = code[j].replace("4", "", 1)
                print(Checker(re_code, variables))
            
            if code[j].startswith("?"):
                re_code = code[j].replace("?", "", 1)
                statements = re_code.split(":")
                if Checker(statements[0], variables):
                    self.interpret(Interpreter, statements[1])
                else:
                    self.interpret(Interpreter, statements[2])

            if code[j] in variables.keys():
                print(variables[code[j]])