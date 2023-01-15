def sortStack(values):
    if not values:
        return []
    minVal = min(values)
    values.remove(minVal)
    return sortStack(values) + [minVal]


unsorted_stack = [0, 99, 45, 12, 3, 78]
print(sortStack(unsorted_stack))

# sortStack(list) function sorts all the elements present in the stack
# problem: unsorted_stack = [11, 2, 32, 3, 41]
# sub problem: unsorted_stack = [11, 32, 3, 41]
# sortStack(problem) = sortStack(sub problem) + minimum value
