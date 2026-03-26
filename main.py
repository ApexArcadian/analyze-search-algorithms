from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random

arr = [random.randint(1, 100) for _ in range(20)]
sorted = arr.sort()
target = random.choice(arr) if random.random() < 0.5 else 999 # 50% of failure
index = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"{target} found at index: {index}" if index != -1 else f"{target} not found")

index1 = iterative_binary_search(arr, target)
print(f"{target} found at index: {index}" if index1 != -1 else f"{target} not found")
      
index2 = sequential_search(arr, target)
print(f"{target} found at index: {index}" if index2 != -1 else f"{target} not found")