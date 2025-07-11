def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            results.append(str(result).rjust(width))

    arranged = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(results)

    return arranged
problems=[]
number=int(input("Enter the number of problems:"))
for n in range(number):
    values=input("Enter the problems:")
    problems.append(values)

print(arithmetic_arranger(problems,True))