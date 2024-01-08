def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        first = 0
        last = len(list) - 1
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return True
        else: 
            if list[midpoint] < target:
               return recursive_binary_search(list[midpoint + 1:], target)
            else: 
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found:", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 7)
marks = recursive_binary_search(numbers, 3)

verify(result)
verify(marks)



