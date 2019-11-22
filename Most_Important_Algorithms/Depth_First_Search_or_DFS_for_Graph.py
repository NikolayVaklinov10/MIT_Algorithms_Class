"""
Depth First Search or DFS for a Graph:
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal
of a tree. The only catch here is, unlike trees, graphs may contain cycles so we
may come to the same node again. To avoid processing a node more than once, we
use a boolean visited array.
For example, in the following graph, we start traversal from vertex 2. When we
come to vertex 0, we look for all adjacent vertices of it. 2 is also an adjacent
 vertex of 0. If we don't mark visited vertices, then 2 will be processed again
 and it will become a non-terminating process. A depth First Traversal of the
 following graph is 2, 0, 1, 3.

 See this post for all applications of Depth First Traversal.
 Following are implementations of simple Depth First Traversal.
"""
# Python 3 program to print DFS traversal
# from a given graph
from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited[v] = True
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


# Driver code

# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)










































