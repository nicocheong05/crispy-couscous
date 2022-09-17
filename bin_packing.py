import math
from BubbleSort_Answers import bubbleSort

data = [8,7,3,9,6,9,5,5,6,7,7]
fixed_length = float(input("Size of bin: "))

def optimal_results():
    total = 0
    for index in range(len(data)):
        total = total + data[index]
    lower_bound = math.ceil(total/fixed_length)
    print("Optimal solution will have use " + str(lower_bound) + " units.\n")

def first_fit_alg(list):
    count = 1
    remainder = fixed_length
    wastage = 0
    for i in range(len(list)):
        if remainder < list[i]:
            count = count + 1
            wastage = wastage + remainder
            remainder = fixed_length
        remainder = remainder - list[i]
    wastage = wastage + remainder #unused length in final bin
    print("Wastage: " + str(wastage))
    print("Total units used: " + str(count))

def first_fit_decreasing(set):
    sorted_data = bubbleSort(set)
    remainder = fixed_length
    wastage = 0
    count = 1
    while len(sorted_data) != 0:
        fit = False
        j = 0
        while fit == False and j < len(sorted_data):
            if remainder >= sorted_data[j]:
                remainder = remainder - sorted_data[j]
                sorted_data.remove(sorted_data[j])
                fit = True
            else:
                j = j +1
        if j >= len(sorted_data) and fit == False:
            wastage = wastage + remainder
            remainder = fixed_length
            count = count + 1
    wastage = wastage + remainder #unused length in final bin
    print("\nWastage: " + str(wastage))
    print("Total units used: " + str(count))

def full_bin(this_list):
    count = 0
    while len(this_list) != 0:

optimal_results()

print("First Fit Algorithm")
first_fit_alg(data)

print("Decreasing First Fit Algorithm")
first_fit_decreasing(data)
