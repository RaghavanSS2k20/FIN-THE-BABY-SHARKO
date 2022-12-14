import sys

ROUTERS = 9
NETWORK = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
class Graph():
    def __init__(self,routers):
        self.routers=routers
        self.network=[]
        self.distance=[sys.maxsize]*self.routers
        self.nextHop = [0 for _ in range(routers)]
    
    def minDistance(self,distance,visited):
        min=sys.maxsize
        for i in range(routers):
            if distance[i]<min and visited[i]==False:
                min=distance[i]
                minIndex = i
        return minIndex
    
    def dijikstra(self,src):
        self.distance=[sys.maxsize]*self.routers
        self.distance[src]=0
        self.nextHop[src]=src
        visited = [False] * self.routers

        for i in range(self.routers):
            if self.network[index][j]>0 and visited[j] == False and self.distance[j]>self.distance[index]+self.network[index][j]:
                self.distance[j] =self.distance[index]+self.network[index][j]
                if self.distance[index]==0:
                    self.nextHop[j] = j
                else:
                    hop=index
                    temp=src
                    while(True):
                        
    