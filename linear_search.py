def linear_search(list, target):
    # Returns the position of the target if found, else returns none
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify (index):
    if index is not None: 
        print("Target at index:", index)
    else: print("Not found")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)

results = linear_search(numbers, 8)

verify(result)
verify(results)

