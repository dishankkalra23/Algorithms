import sys


class AdjacentMatrix:

    def __init__(self, routers):
        self.AdjacentMatrix = None
        self.vertices = routers

    def algorithmShortPath(self, source_router):

        distanceMatrix = [sys.maxsize] * self.vertices
        distanceMatrix[source_router] = 0
        shortestPath = [False] * self.vertices

        for i in range(self.vertices):
            minimumValue = sys.maxsize
            for j in range(self.vertices):
                if distanceMatrix[j] < minimumValue and shortestPath[j] == False:
                    minimumValue = distanceMatrix[j]
                    smallestVertices = j
            finalSmall = smallestVertices

            shortestPath[finalSmall] = True

            for k in range(self.vertices):
                if (self.AdjacentMatrix[finalSmall][k] > 0) and (
                        distanceMatrix[k] > distanceMatrix[finalSmall] + self.AdjacentMatrix[finalSmall][k]) and \
                        shortestPath[
                            k] == False:
                    distanceMatrix[k] = distanceMatrix[finalSmall] + self.AdjacentMatrix[finalSmall][k]

        self.pathFromSource(distanceMatrix)

    def pathFromSource(self, distanceMatrix):
        print("Shortest Path from source", source, "and all other vertices - ")
        print("Vertices(Routers) \tDistance from Source", source)
        for node in range(self.vertices):
            print(node, "\t\t\t\t\t\t", distanceMatrix[node])


v = 9
g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]
     ]
objectMatrix = AdjacentMatrix(v)
objectMatrix.AdjacentMatrix = g
for source in range(v):
    objectMatrix.algorithmShortPath(source)
    print()
