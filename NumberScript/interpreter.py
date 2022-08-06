from functools import reduce
from operator import mod

def Calculate(removed_code: str, variables: dict) -> int:
    """Calculator"""
    if "+" in removed_code:
        removed_code = removed_code.split("+")
        for x in range(0, len(removed_code)):
            if removed_code[x] in variables.keys():
                removed_code[x] = int(variables[removed_code[x]])
            else:
                removed_code[x] = int(removed_code[x])
        return sum(removed_code)

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

        return min_total

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

        return product

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

        return product

    elif "#" in removed_code:
        removed_code = removed_code.split("#")

        for x in range(0, len(removed_code)):
            if removed_code[x] in variables.keys():
                removed_code[x] = int(variables[removed_code[x]])
            else:
                removed_code[x] = int(removed_code[x])

        product = reduce(mod, removed_code)
        return product

def Checker(re_code: str, variables: dict) -> bool:
    """Boolean Checker"""
    if "=" in re_code:
        code = re_code.split("=")
        if code[0] in variables:
            code[0] = variables[code[0]]
        elif code[0].isdigit():
            code[0] = int(code[0])
        elif code[0].startswith("^"):
            recode = code[0].replace("^", "", 1)
            code[0] = Calculate(recode, variables)

        if code [1] in  variables:
            code[1] = variables[code[1]]
        elif code[1].isdigit():
            code[1] = int(code[1])
        elif code[1].startswith("^"):
            recode = code[1].replace("^", "", 1)
            code[1] = Calculate(recode, variables)
        
        return code[0] == code[1]

    elif "!" in re_code:
        code = re_code.split("!")
        if code[0] in variables:
            code[0] = variables[code[0]]
        elif code[0].isdigit():
            code[0] = int(code[0])
        elif code[0].startswith("^"):
            recode = code[0].replace("^", "", 1)
            code[0] = Calculate(recode, variables)
        
        if code [1] in  variables:
            code[1] = variables[code[1]]
        elif code[1].isdigit():
            code[1] = int(code[1])
        elif code[1].startswith("^"):
            recode = code[1].replace("^", "", 1)
            code[1] = Calculate(recode, variables)

        return code[0] != code[1]

    elif "<" in re_code:
        code = re_code.split("<")
        if code[0] in variables:
            code[0] = variables[code[0]]
        elif code[0].isdigit():
            code[0] = int(code[0])
        elif code[0].startswith("^"):
            recode = code[0].replace("^", "", 1)
            code[0] = Calculate(recode, variables)

        if code [1] in  variables:
            code[1] = variables[code[1]]
        elif code[1].isdigit():
            code[1] = int(code[1])
        elif code[1].startswith("^"):
            recode = code[1].replace("^", "", 1)
            code[1] = Calculate(recode, variables)
        
        return code[0] < code[1]

    elif ">" in re_code:
        code = re_code.split(">")
        if code[0] in variables:
            code[0] = variables[code[0]]
        elif code[0].isdigit():
            code[0] = int(code[0])
        elif code[0].startswith("^"):
            recode = code[0].replace("^", "", 1)
            code[0] = Calculate(recode, variables)
        
        if code [1] in  variables:
            code[1] = variables[code[1]]
        elif code[1].isdigit():
            code[1] = int(code[1])
        elif code[1].startswith("^"):
            recode = code[1].replace("^", "", 1)
            code[1] = Calculate(recode, variables)

        return code[0] > code[1]

class Interpreter():
    """Main Interpreter class"""

    def __init__(self):
        """Initialize the interpreter"""
        pass

    def interpret(self, code: str, variables_dict: dict = {}) -> str:
        """Interprets the code"""
        code = code.split(" ")
        variables = variables_dict
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
                if var_content in variables.keys():
                    var_content = variables[var_content]
                elif var_content.isdigit():
                    var_content = int(var_content)
                elif var_content.startswith("^"):
                    var_content = var_content.replace("^", "", 1)
                    var_content = Calculate(var_content, variables)
                elif var_content.startswith("~"):
                    var_content = var_content.replace("~", "", 1)
                    var_content = input(var_content)
                    if var_content.isdigit():
                        var_content = int(var_content)
                variables[var_name] = var_content

            if code[j].startswith("^"):
                removed_code = code[j].replace("^", "")
                print(Calculate(removed_code, variables))

            if code[j].startswith("%"):
                continue
            
            if code[j].startswith("4"):
                re_code = code[j].replace("4", "", 1)
                print(Checker(re_code, variables))
            
            if code[j].startswith("?"):
                re_code = code[j].replace("?", "", 1)
                statements = re_code.split(":")
                if Checker(statements[0], variables):
                    if "|" in statements[1]:
                        true_statements = statements[1].replace("|", " ")
                    else:
                        true_statements = statements[1]
                    self.interpret(Interpreter, true_statements, variables)
                else:
                    if "|" in statements[2]:
                        false_statements = statements[2].replace("|", " ")
                    else:
                        false_statements = statements[2]
                    self.interpret(Interpreter, false_statements, variables)

            if code[j] in variables.keys():
                print(variables[code[j]])

            if code[j].startswith("5"):
                pass

            if code[j].startswith("6"):
                recode = code[j].replace("6", "", 1).split("\\")
                repeat_name = variables[recode[0]] if recode[0] in variables.keys() else recode[0]
                repeat_times = int(variables[recode[1]]) if recode[1] in variables.keys() else int(recode[1])
                repeat_code = recode[2].replace(";", " ")
                variables[repeat_name] = 0
                variabless = variables
                for x in range(0, repeat_times):
                    self.interpret(Interpreter, repeat_code, variabless)
                    variabless[repeat_name] += 1

            if code[j].startswith("~"):
                recode = code[j].replace("~", "", 1)
                input(recode)