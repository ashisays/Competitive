"""
You are required to cross a river to reach your destination. The streamflow of the river was fast, therefore, you cannot cross the river by swimming.

The river is available at the X-axis and its boundary is marked by Y coordinates, from  to .

---------------------------------------------------------------------------------

..................................................................................................

..................................................................................................

..................................................................................................

----------------------------------------------------------------------------------

You are provided with some rocks along with their centers and radius respectively. Currently, you are standing on the shore . You cannot jump between rocks but can move from one rock to another if both rocks overlap at some point. You are required to determine whether you will be able to cross the river by using rocks or not. If you can cross the river, then print the minimum number of rocks that are required to cross the river. Otherwise, print .

Input format

First line:  denoting the number of test cases
For each of the test case:
First line:  denoting the number of rocks
Second line:  lines containing three integers  where  denotes the coordinates of the center of that rocks and  denotes its radius
Third line: Two integers  and  denoting the upper and lower boundary of the river respectively
Output format

Print the required answer in a separate line for each of the test case.

"""

class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
        # function to add an edge to graph

    def add_edge(self, u, w, v):
        self.graph.append([u, v, w])

        # utility function used to print the solution

    def print_arr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        # print all distance
        self.print_arr(dist)

