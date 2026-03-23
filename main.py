from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
# import search_algorithms and create test list
arr = [3, 5, 8, 12, 14, 18, 21]
arr.sort()
target1 = 12  # Present
target2 = 9   # Not present

index0 = recursive_binary_search(arr, target1, 0, len(arr) - 1)
print(f"{target1} found at index: {index0}" if index0 != -1 else f"{target1} not found")

index1 = iterative_binary_search(arr, target1)
print(f"{target1} found at index: {index1}" if index1 != -1 else f"{target1} not found")
      
index2 = sequential_search(arr, target1)
print(f"{target1} found at index: {index2}" if index2 != -1 else f"{target1} not found")