from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random

arr = sorted([random.randint(1, 1000000) for _ in range(20)])

target = random.choice(arr) if random.random() < 0.5 else 999 # 50% of failure

index = recursive_binary_search(arr, target, 0, len(arr) - 1)
index1 = iterative_binary_search(arr, target)
index2 = sequential_search(arr, target)

print(f"{target} found at index: {index}" if index != -1 else f"{target} not found")


print(f"{target} found at index: {index}" if index1 != -1 else f"{target} not found")
      

print(f"{target} found at index: {index}" if index2 != -1 else f"{target} not found")