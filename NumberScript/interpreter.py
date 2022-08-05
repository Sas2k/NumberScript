class Interpreter():
    def __init__(self):
        pass

    def interpret(code: str) -> str:
        code = code.split(" ")
        if "\n" in code:
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
                if "=" in re_code[0]:
                    req_code = re_code[0].split("=")
                    if req_code[0] in variables.keys():
                        val1 = variables[req_code[0]]
                    else:
                        val1 = req_code[0]

                    if req_code[1] in variables.keys():
                        val2 = variables[req_code[1]]
                    else:
                        val2 = req_code[1]

                    return val1 == val2

                elif "!" in re_code[0]:
                    req_code = re_code[0].split("!")
                    if req_code[0] in variables.keys():
                        val1 = variables[req_code[0]]
                    else:
                        val1 = req_code[0]
                    
                    if req_code[1] in variables.keys():
                        val2 = variables[req_code[1]]
                    else:
                        val2 = req_code[1]
                    
                    return val1!=val2

                elif ">" in re_code[0]:
                    req_code = re_code[0].split(">")
                    if req_code[0] in variables.keys():
                        val1 = int(variables[req_code[0]])
                    else:
                        val1 = int(req_code[0])

                    if req_code[1] in variables.keys():
                        val2 = int(variables[req_code[1]])
                    else:
                        val2 = int(req_code[1])
                    
                    return val1 > val2

                elif "<" in re_code[0]:
                    req_code = re_code[0].split("<")
                    if req_code[0] in variables.keys():
                        val1 = int(variables[req_code[0]])
                    else:
                        val1 = int(req_code[0])

                    if req_code[1] in variables.keys():
                        val2 = int(variables[req_code[1]])
                    else:
                        val2 = int(req_code[1])
                    
                    return val1 < val2

            if code[j] in variables.keys():
                print(variables[code[j]])