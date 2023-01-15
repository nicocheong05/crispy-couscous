def reverse(s):
    if s == "":
        return ""
    new_string = slice(1, len(s))
    return reverse(s[new_string]) + s[0]


answer = reverse("python pycharm")
print(answer)


# reverse(s) function reverses a string
# original problem: Hello
# subproblem: ello
# original problem = reverse(subproblem) + 'H' = 'olle' + H
# reverse('Hello') = reverse('ello') + H = 'olleH'


