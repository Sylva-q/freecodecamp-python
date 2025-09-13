def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        left, op, right = problem.split()

        # 检查运算符
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # 检查是不是数字
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        # 检查位数
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # 确定宽度
        width = max(len(left), len(right)) + 2

        # 构造各行
        first_line.append(left.rjust(width))
        second_line.append(op + right.rjust(width - 1))
        dashes.append('-' * width)

        result = eval(left + op + right)
            results.append(result.rjust(width))

    # 组装输出
    arranged = '    '.join(first_line) + '\n' + \
               '    '.join(second_line) + '\n' + \
               '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(results)

    return arranged

