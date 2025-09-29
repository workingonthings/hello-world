array  = [x for x in range(1000000000)]
jumps = 0

def binary_search(target,array):
    global jumps
    low = 0 
    high = len(array) - 1
    while low <= high:
        jumps += 1 
        mid = (high + low) // 2
        if target == array[mid]:
            return array[mid]
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1  
    return None
    
answer = binary_search(7891,array)

print(answer)
print(jumps)

   
    







