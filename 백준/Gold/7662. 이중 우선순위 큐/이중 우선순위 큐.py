import heapq

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    seen = {}
    for _ in range(int(input())):
        cmd, num = list(input().split())
        num = int(num)
        
        if cmd == "I":
            seen[num] = seen.get(num, 0) + 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif cmd == "D":
            v = 0
            if num == -1:
                while min_heap and seen[min_heap[0]] <= 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    v = heapq.heappop(min_heap)
            elif num == 1:
                while max_heap and seen[-max_heap[0]] <= 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    v = -heapq.heappop(max_heap)
            if v != 0:
                seen[v] -= 1
    while min_heap and seen[min_heap[0]] <= 0:
        heapq.heappop(min_heap)
    while max_heap and seen[-max_heap[0]] <= 0:
        heapq.heappop(max_heap)
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print( -max_heap[0], min_heap[0])