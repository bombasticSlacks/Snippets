import random

def roll(a, i):
    return random.randint(1,6) + random.randint(1,6) + a + i
    
def rollSmall(x):
    return random.randint(1,6) + x

dist = []
for i in range(2,20):
    dist.append([i,0])
for i in range(1,4):
    temp = (roll(2,2))
    dist[temp-2][1] = dist[temp-2][1]+1

for i in range(1,4):
    temp = (roll(3,2))
    dist[temp-2][1] = dist[temp-2][1]+1
    
for i in range(1,4):
    temp = (roll(3,3))
    dist[temp-2][1] = dist[temp-2][1]+1
    
for i in range(1,4):
    temp = (roll(4,3))
    dist[temp-2][1] = dist[temp-2][1]+1
print(dist)

dist2 = []

for i in range(1,13):
    dist2.append([i,0])
for i in range(1,4):
    temp = (rollSmall(2))
    dist2[temp-1][1] = dist2[temp-1][1]+1

for i in range(1,4):
    temp = (rollSmall(3))
    dist2[temp-1][1] = dist2[temp-1][1]+1
    
for i in range(1,4):
    temp = (rollSmall(4))
    dist2[temp-1][1] = dist2[temp-1][1]+1
    
for i in range(1,4):
    temp = (rollSmall(5))
    dist2[temp-1][1] = dist2[temp-1][1]+1
print(dist2)
