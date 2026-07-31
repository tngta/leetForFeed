time = [[0, 30], [5, 10], [15, 20]]

import heapq
# sort the intervals based on the start time
sorted_time = sorted(time)
h = []

for start, end in sorted_time:
    if h and h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)

print(len(h))