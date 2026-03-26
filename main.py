from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random

arr = [random.randint(1, 100) for _ in range(20)]
arr = arr.sort()
target = random.choice(arr) if random.random() < 0.5 else 999 # 50% of failure
index0 = recursive_binary_search(arr, target1, 0, len(arr) - 1)
print(f"{target1} found at index: {index0}" if index0 != -1 else f"{target1} not found")

index1 = iterative_binary_search(arr, target1)
print(f"{target1} found at index: {index1}" if index1 != -1 else f"{target1} not found")
      
index2 = sequential_search(arr, target1)
print(f"{target1} found at index: {index2}" if index2 != -1 else f"{target1} not found")