"""
Transitive Closure of a Graph using DFS
Given a directed graph, find out if a vertex v is reachable from another vertex u
for all vertex pairs (u, v) in the given graph. Here reachable mean that there is
a path from vertex u to v. The reachability matrix is called transitive closure
of a graph.

Transitive closure of above graphs is
     1 1 1 1
     1 1 1 1
     1 1 1 1
     0 0 0 1

We have discussed a O(V3) solution for this here. The solution was based
Floyd Warshall Algorithm. In this post a O(V2) algorithm for the same is
discussed.

Below are abstract steps of algorithm.


Create a matrix tc[V][V] that would finally have transitive closure of given
graph. Initialize all entries of tc[][] as 0.
Call DFS for every node of graph to mark reachable vertices in tc[][]. In
recursive calls to DFS, we don’t call DFS for an adjacent vertex if it is already
marked as reachable in tc[][].

Below is implementation of the above idea. The code uses adjacency list
representation of input graph and builds a matrix tc[V][V] such that tc[u][v]
would be true if v is reachable from u.
"""
# Python program to print transitive closure of a graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # To store transitive closure
        self.tc = [[0 for j in range(self.V)]for i in range(self.V)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive DFS traversal function that finds all reachable vertices for s
    def DFSUtil(self, s, v):
        # Mark reachability  from s to v as true.
        self.tc[s][v] = 1

        # Find all the vertices reachable through v
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s, i)

    # The function to find transitive closure. It uses
    # recursive DFSUtil()
    def transitiveClosure(self):
        # Call the recursive helper function to print DFS
        # traversal string from all vertices one by one
        for i in range(self.V):
            self.DFSUtil(i, i)
        print(self.tc)


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Transitive closure matrix is")
g.transitiveClosure()


















