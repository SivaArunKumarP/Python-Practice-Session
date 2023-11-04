v = 6
I = 999
distance = []
for i in range(v):
    distance.append([])
    for j in range(v):
        distance[i].append(I)
      
def dijkstra(G):
    for k in range(v):
        distance[k][k] = 0
        visited = set([k])
        
        for i in range(v):
            u = k
            minDist = I
            
            for j in range(v):
                if distance[k][j] < minDist and j not in visited:
                    minDist = distance[k][j]
                    u = j
            
            visited.add(u)
            for j in range(v):
                if j not in visited:
                    distance[k][j] = min(distance[k][u] + G[u][j], distance[k][j])
    prnt(distance)

def prnt(distance):
    for i in range(v):
        for j in range(v):
            print(distance[i][j], end="  ")
        print(" ")

G = [[0,4,I,2,I,I],
    [4,0,1,6,3,I],
    [I,1,0,I,I,1],
    [2,6,I,0,3,I],
    [I,3,I,3,0,2],
    [I,I,1,I,2,0]]

dijkstra(G)

