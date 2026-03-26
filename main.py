from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random, time

dataSize = [5000, 50000, 100000, 150000, 1000000]

for N in dataSize:
    SumRBS = SumIBS = SumSeqS = 0
    
    for _ in range(10):
        arr = sorted([random.randint(1,1000000) for _ in range(N)])
        target = random.choice(arr) if random.random() < 0.5 else 999 # 50% of failure
        
        #recursive binary search timing
        start = time.perf_counter()
        indexRBS = recursive_binary_search(arr, target, 0, len(arr) - 1)
        SumRBS += (time.perf_counter() - start) * 1000000
       
        # iterative binary search timing 
        start = time.perf_counter()
        indexIBS = iterative_binary_search(arr, target)
        SumIBS += (time.perf_counter() - start) * 1000000
        
        # sequential search timing
        start = time.perf_counter()
        indexSeqS = sequential_search(arr, target)
        SumSeqS += (time.perf_counter() - start) * 1000000
    print(f"Data Size: {N}")
    print(f"Average Time for Recursive Binary Search: {SumRBS / 10:.2f} microseconds")
    print(f"Average Time for Iterative Binary Search: {SumIBS / 10:.2f} microseconds")
    print(f"Average Time for Sequential Search: {SumSeqS / 10:.2f} microseconds")
        

# index = recursive_binary_search(arr, target, 0, len(arr) - 1)
# index1 = iterative_binary_search(arr, target)
# index2 = sequential_search(arr, target)

# print(f"{target} found at index: {index}" if index != -1 else f"{target} not found")


# print(f"{target} found at index: {index}" if index1 != -1 else f"{target} not found")
      

# print(f"{target} found at index: {index}" if index2 != -1 else f"{target} not found")