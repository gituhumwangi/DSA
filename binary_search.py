def binary_search(list, target):
    #intialization of the indexes
    first = 0
    last = len(list) - 1
# Using a while loop t loop through the list untill the condition is false
    while first <= last:

        midpoint = (first + last)//2
#Comparision of the midpoint to see if it matches the target
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first=midpoint + 1
        else: 
            last = midpoint - 1

    return None

def verify (index):
    if index is not None: 
        print("Target at index:", index)
    else: print("Not found")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)

results = binary_search(numbers, 8)

verify(result)
verify(results)
