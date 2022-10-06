import math

print("Enter your list directly into 'given_list' in the text editor")
print("Disclaimer: This will not perform a full quick sort. It will find you the median, the elements smaller than the pivot, "
      "and the elements larger than the pivot. ")
print("You will likely have to run the program multiple times.\n")
given_list = ['M','V','C','A','D','B','K','S']

median = (len(given_list)+1)/2
if not median.is_integer():
    median = math.ceil(median) -1
    median_element = given_list[median]
    print('Median is ' + str(median) + ", rounding up gives element " + str(median_element))
else:
    median = int(median) - 1
    median_element = given_list[median]
    print("Median is " + str(median_element))

def quick_sort(median, median_element):
    smaller_than = []
    larger_than = []
    same_as = [median_element]
    for i in range(len(given_list)-1):
        if i != median:
            if given_list[i] < median_element:
                smaller_than.append(given_list[i])
            elif given_list[i] >= median_element:
                larger_than.append(given_list[i])
    print("Smaller than pivot:")
    print(smaller_than)
    print("Pivot:")
    print(same_as)
    print("Larger than pivot:")
    print(larger_than)

quick_sort(median, median_element)

