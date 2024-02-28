def arithmetic_arranger(problems,result=False):
    linea_1=[]
    linea_2=[]
    separador=[]
    resultado=[]
    if len(problems) >5:
        return "Error: Too many problems."
    for problem in problems:
        if "+" in problem or "-" in problem:
            if "+" in problem:
                problem=problem.split(" + ")
                if len(problem[0]) > 4 or len(problem[1])> 4:
                    return "Error: Numbers cannot be more than four digits."
                if not problem[0].isdigit()  or not problem[1].isdigit():
                    return "Error: Numbers must only contain digits."
                max_len=max(len(problem[0]),len(problem[1]))
                linea_1.append(problem[0].rjust(max_len+2, ' '))
                linea_2.append("+ "+problem[1].rjust(max_len, ' '))
                separador.append("-"*(max_len+2))
                resultado.append(str(int(problem[0])+int(problem[1])).rjust(max_len+2," "))
            else:
                problem=problem.split(" - ")
                if len(problem[0]) > 4 or len(problem[1])> 4:
                    return "Error: Numbers cannot be more than four digits."
                if not problem[0].isdigit()  or not problem[1].isdigit():
                    return "Error: Numbers must only contain digits."
                max_len=max(len(problem[0]),len(problem[1]))
                linea_1.append(problem[0].rjust(max_len+2, ' '))
                linea_2.append("- "+problem[1].rjust(max_len, ' '))
                separador.append("-"*(max_len+2))
                resultado.append(str(int(problem[0])-int(problem[1])).rjust(max_len+2," "))  
        else:
            return "Error: Operator must be '+' or '-'."
    if result:
        return f'{"    ".join(linea_1)}\n{"    ".join(linea_2)}\n{"    ".join(separador)}\n{"    ".join(resultado)}'
    else:
        return f'{"    ".join(linea_1)}\n{"    ".join(linea_2)}\n{"    ".join(separador)}'
if __name__=="__main__":
    print(arithmetic_arranger(["4 + 6","89 - 5"]))
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))