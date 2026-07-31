pts = [[3,3],[5,-1],[-2,4]]
k =2

# => [[3,3],[-2,4]]



import heapq

h= []
for x, y in pts:
    dist= x*x + y*y
    heapq.heappush(h, (-dist, [x,y]))

    if len(h) > k:
        heapq.heappop(h)

res = []
for el in h:
    res.append(el[1])
print(res)

    

