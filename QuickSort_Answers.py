array = [11, 9, 4, 13, 5, 1, 7, 12, 8]
order = input("'asc' or 'desc'?")

def duplicateArray():
    newArray = []
    for num in range(len(array)):
        newArray.append(array[num])
    return newArray

def newQuickSort():
    print(array)
    pivotIndex = round((len(array)+1)/2) - 1
    pivot = array[pivotIndex]
    print("Pivot: " + str(pivot))
    newArray = duplicateArray()
    for i in range(len(array)):
        print("Comparing element " + str(i+1))
        currentPivotPosition = newArray.index(pivot)
        currentTermPosition = newArray.index(array[i])
        if order == "asc":
            if i < pivotIndex and array[i] > pivot:
                for j in range(currentTermPosition+1, currentPivotPosition+1):
                    newArray[j] = newArray[j+1]
                newArray[pivotIndex] = array[i]
                print(newArray)
            elif i > pivotIndex and array[i] < pivot:
                for j in range(currentTermPosition-1, currentPosition-1, -1):
                    newArray[j+1] = newArray[j]
                newArray[currentPivotPosition] = array[i]
                print(newArray)
        if order == "desc":
            if i < pivotIndex and array[i] < pivot:
                for j in range(currentTermPosition+1, currentPivotPosition+1):
                    newArray[j] = newArray[j+1]
                newArray[pivotIndex] = array[i]
                print(newArray)
            elif i > pivotIndex and array[i] > pivot:
                for j in range(currentTermPosition-1, currentPosition-1, -1):
                    newArray[j+1] = newArray[j]
                newArray[currentPivotPosition] = array[i]
                print(newArray)
newQuickSort()
