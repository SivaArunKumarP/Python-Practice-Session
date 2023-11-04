v = 6
I = 999
def floyd(G):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    prnt(G)
def prnt(distance):
    for i in range(v):
        for j in range(v):
            print(distance[i][j], end="  ")
        print(" ")


G =[[0,4,I,2,I,I],
    [4,0,1,6,3,I],
    [I,1,0,I,I,1],
    [2,6,I,0,3,I],
    [I,3,I,3,0,2],
    [I,I,1,I,2,0]]
floyd(G)