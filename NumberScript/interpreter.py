from functools import reduce
from operator import mod
from random import randint

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

    def interpret(self, code: str, variables_dict: dict = {}, function_dict: dict = {}) -> str:
        """Interprets the code"""
        code = code.split(" ")
        variables = variables_dict
        functions = function_dict
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
                elif code[j][1:].startswith("@"):
                    recode = code[j][1:].replace("@", "", 1)
                    recode = recode.split(".", 1)
                    if recode[0] in variables.keys():
                        recode[0] = variables[recode[0]]
                    if recode[1] in variables.keys():
                        recode[1] = variables[recode[1]]
                    try:
                        recode = recode[0][int(recode[1])]
                        print(recode)
                    except IndexError:
                        return print("Error: Index Out Of Range")
                    except ValueError:
                        return print("Error: Index Not A Number")
                else:
                    print(code[j][1:])

            if code[j].startswith("3"):
                vars = code[j].replace("3", "", 1).split(":")
                try:
                    var_name = vars[0]
                except:
                    return print("Error: Variable name not defined")
                try:
                    var_content = vars[1]
                except:
                    return print("Error: Variable content not defined")
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
                elif var_content.startswith("*"):
                    var_content = var_content.replace("*", "", 1).split("!", 1)
                    random_num = randint(int(var_content[0]), int(var_content[1]))
                    var_content = random_num
                elif var_content.startswith("@"):
                    var_content = var_content.replace("@", "", 1)
                    var_content = var_content.split(".", 1)
                    if var_content[0] in variables.keys():
                        var_content[0] = variables[var_content[0]]
                    if var_content[1] in variables.keys():
                        var_content[1] = variables[var_content[1]]
                    try:
                        var_content = var_content[0][int(var_content[1])]
                    except IndexError:
                        return print("Error: Index Out Of Range")
                    except ValueError:
                        return print("Error: Index Not A Number")
                    
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
                statements = re_code.split("|", 2)
                if Checker(statements[0], variables):
                    try:
                        true_statements = statements[1].replace(":", " ")
                    except:
                        true_statements = statements[1]
                    self.interpret(Interpreter, true_statements, variables)
                else:
                    try:
                        false_statements = statements[2].replace(":", " ")
                    except:
                        false_statements = statements[2]
                    self.interpret(Interpreter, false_statements, variables)

            if code[j] in variables.keys():
                print(variables[code[j]])

            if code[j].startswith("5"):
                pass

            if code[j].startswith("6"):
                recode = code[j].replace("6", "", 1).split("\\", 2)
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

            if code[j].startswith("7"):
                recode = code[j].replace("7", "", 1).split("$", 2)
                function_name = recode[0]
                function_parameters = recode[1].split(",")
                function_code = recode[2].split("|")
                functions[function_name] = [function_parameters, function_code]

            if code[j].startswith("*"):
                recode = code[j].replace("*", "", 1).split("!", 1)
                random_num = randint(recode[0], recode[1])
                print(int(random_num))


            if any(str(key) in code[j] for key in functions.keys()) and not code[j].startswith("7"):
                recode = code[j].split("$", 1)
                func_name = functions[recode[0]]
                func_params = recode[1].split(",")
                for x in range(0, len(func_params)):
                    if func_params[x] in variables.keys():
                        variables[func_name[0][x]] = variables[func_params[x]]
                    elif func_params[x].isdigit():
                        variables[func_name[0][x]] = int(func_params[x])
                    elif func_params[x].startswith("^"):
                        cal = func_params[x].replace("^", "", 1)
                        variables[func_name[0][x]] = Calculate(cal, variables)
                    elif func_params[x].startswith("~"):
                        inp = func_params[x].replace("~", "", 1)
                        variables[func_name[0][x]] = input(inp)
                        if variables[func_name[0][x]].isdigit():
                            variables[func_name[0][x]] = int(variables[func_name[0][x]])
                    elif code[j].startswith("*"):
                        recode = code[j].replace("*", "", 1).split("!", 1)
                        random_num = randint(recode[0], recode[1])
                        variables[func_name[0][x]] = int(random_num)
                    else:
                        variables[func_name[0][x]] = func_params[x]
                func_code = ""
                for j in range(0, len(func_name[1])):
                    func_code += func_name[1][j] + " "
                self.interpret(Interpreter, func_code, variables, functions)
                