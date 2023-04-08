def rpn_calculator(expression, stack=[]):
    if len(expression) == 1 and expression[0].isdigit():
        return expression[0]
    elif len(expression) == 0:
        ans = stack[0]
        return ans

    x = expression.pop(0)
    if x.isdigit():
        stack.append(x)
        return rpn_calculator(expression, stack)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if x == '+':
            y = a + b
        elif x == '-':
            y = a - b
        elif x == '*':
            y = a * b
        elif x == '/':
            y = a/b
        stack.append(y)
        return rpn_calculator(expression, stack)


mylist = ['8', '2', '/', '3', '+', '6', '*']
final_ans = rpn_calculator(mylist)
print(final_ans)