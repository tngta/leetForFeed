nums = [1,1,1,2,2,3]
k =2

import heapq
from collections import Counter

h = []
freq = Counter(nums)
print(freq)
print(freq.items())

for num, count in freq.items():
    heapq.heappush(h, (count, num))

    if len(h) > k:
        heapq.heappop(h)

res = []
for count, num in h:
    res.append(num)
print (res)

