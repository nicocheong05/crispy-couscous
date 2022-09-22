import random
import string

type = input("Generate numbers or letters? Type num or let\n")
question_length = int(input("How many elements would you like?\n"))
order = input("asc or desc?\n")

def question_generator():
    this_question = []
    for i in range(question_length):
        if type == "num":
            this_question.append(random.randint(0,101))
        elif type == "let":
            this_letter = random.choice(string.ascii_uppercase)
            this_question.append(this_letter)
    print("Use a bubble sort to arrange this list into " + order + "ending order:")
    print(this_question)
    return(this_question)

def bubbleSort(array):
    Pass = 0
    swapped = True
    while swapped == True:
        Pass = Pass + 1
        swapped = False
        print("\nPass " + str(Pass))
        for i in range(len(array)-Pass):
            if order == "asc":
                if array[i] > array[i+1]:
                    if Pass == 1:
                        print("Swapping elements " + str(i+1) + " & " + str(i+2))
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swapped = True
                    if Pass == 1:
                        print(array)
            if order == "desc":
                if array[i] < array[i+1]:
                    if Pass == 1:
                        print("Swapping elements " + str(i+1) + " & " + str(i+2))
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swapped = True
                    if Pass == 1:
                        print(array)
        if Pass > 1:
            print(array)
    print("\nPass Count : " + str(Pass))
    return array

array = question_generator()
check_answers = input("\nWould you like to view the answers? y/n\n")

if check_answers == "y":
    bubbleSort(array)
