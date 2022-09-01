array = [ 8,
7,
3,
9,
6,
9,
5,
5,
6,
7,
7
]
order = input("Is it 'asc' or 'desc'?\n")

def bubbleSort():
    Pass = 0
    print(array)
    swapped = True
    while swapped == True:
        Pass = Pass + 1
        swapped = False
        print("Pass " + str(Pass))
        for i in range(len(array)-Pass):
            if order == "asc":
                if array[i] > array[i+1]:
                    if Pass == 1:
                        print("Swapping elements " + str(i+1) + " & " + str(i+2))
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swapped = True
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
        print(array)
    print("Pass Count : " + str(Pass))

bubbleSort()



