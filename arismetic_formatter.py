def arithmetic_arranger(problems, show_answers=False):
    #build up the 4-row structure for the result
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    #check if there are more than  problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
    #Using for loop to split operation elements
        for x in problems:
            left, op, right = x.split()

        #Checck if exist / or * operation
            if '*' in x or '/' in x:
                return "Error: Operator must be '+' or '-'." 
        #Checck if each operand is digit
            elif left.isdigit() == 0 or right.isdigit() == 0:
                return 'Error: Numbers must only contain digits.'
        #Checck if each operand is more than 4 digits
            elif len(left) > 4 or len(right) > 4:
                return 'Error: Numbers cannot be more than four digits.'
        #when problems are in the right format, show the result
            else:
            #decide the width of the answer
                width = max(len(left), len(right)) + 2
            #the first row
                row1.append(f'{left:>{width}s}')
            #the second row
                width2 = width - 1
                row2.append(op + f'{right:>{width2}s}')
            #the third row
                row3.append('-' * width)
            #the fourth row
                answer = str(eval(left + op + right))
                row4.append(f'{answer:>{width}s}')
        #Now 4 rows are ready to be arranged
        arranged = '    '.join(row1) + '\n' + \
                    '    '.join(row2) + '\n' + \
                    '    '.join(row3)
        if show_answers:
            arranged += '\n' + '    '.join(row4)
    
        return arranged

print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
