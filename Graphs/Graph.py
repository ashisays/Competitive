from collections import  defaultdict
class AdjNode:
        def __init__(self,data):
            self.vertex = data
            self.next = None

class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph= [None] * self.V

    def add_edge(self,src,dst):
        node = AdjNode(dst)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dst]
        self.graph[dst] = node


    def show(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


    def dfsVisit(self, v, visited):
        # Mark the current node as visited
        # and print it
        visited[v] = True
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i,_ in enumerate(self.graph):
            if visited[i] == False:
                self.dfsVisit(i, visited)

    def dfs(self, v):
        print("starting DFS visiting graph Node")
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        # Call the recursive helper function
        # to print DFS traversal
        self.dfsVisit(v, visited)
        print("\n")
V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.show()
graph.dfs(1)
graph.dfs(0)

