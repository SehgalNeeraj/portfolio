from os import error

MAX_PROBLEMS = 5
MAX_DIGITS = 4
OPERATORS = ["+", "-"]
EMPTY_STRING = ""


def error_description(code):
    error_codes = {
        "ERR00": "Error: Too many problems.",
        "ERR01": "Error: Operator must be '+' or '-'.",
        "ERR02": "Error: Numbers must only contain digits.",
        "ERR03": "Error: Numbers cannot be more than four digits."
    }

    return error_codes[code]


def hasCorrectOperator(problem, operators):
    """[summary]

    Args:
        problem ([type]): [description]
    """
    correct_operator = False

    for operator in OPERATORS:
        opIndex = problem.find(operator)
        if opIndex != -1:
            correct_operator = True

    return correct_operator


def parseInput(problem, problem_parts):
    """[summary]

    Args:
        problems ([type]): [description]
    """
    if not hasCorrectOperator(problem, OPERATORS):
        return error_description("ERR01")

    for operator in OPERATORS:
        opIndex = problem.find(operator)
        if (opIndex != -1):
            problem_parts.append(list(problem.partition(operator)))

    return EMPTY_STRING


def compute(problem_parts):
    """[summary]

    Args:
        problem_parts ([type]): [description]
    """
    for part in problem_parts:
        try:
            op1 = int(part[0])
            op2 = int(part[2])
        except:
            return error_description("ERR02")

        if ((len(part[0]) > MAX_DIGITS) or (len(part[2]) > MAX_DIGITS)):
            return error_description("ERR03")

        operator = part[1]
        if (operator == "+"):
            solution = op1+op2
            part.append(str(solution))
        else:
            solution = op1-op2
            part.append(str(solution))

    return EMPTY_STRING


def display(self):
    return EMPTY_STRING


def arithmetic_arranger(problems, displayAnswer=False):
    """[summary]

    Args:
        maths_problems ([type]): [description]
        displayAnswer (bool, optional): [description]. Defaults to False.
    """
    response = ""
    parts = []

    if len(problems) > MAX_PROBLEMS:
        return error_description("ERR00")

    for problem in problems:
        problem = problem.replace(" ", "")

        returnCode = parseInput(problem, parts)
        if returnCode != EMPTY_STRING:
            return returnCode

        returnCode = compute(parts)
        if returnCode != EMPTY_STRING:
            return returnCode

        response += display(parts)

    return response
