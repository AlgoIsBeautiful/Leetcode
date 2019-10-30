# class AdjNode:
#     def __init__(self, data):
#         self.vertex = data
#         self.next = None
#
# class Graph:
#
#     def __init__(self, V):
#         self.vertices = [x for x in range(V)]
#         self.edges = {}
#
#     def add_edge(self, src, dest):
#         node = AdjNode(dest)
#         node.next = self.edges[src]
#         self.edges[src] = node
#
#         node = AdjNode(src)
#         node.next = self.edges[dest]
#         self.edges[dest] = node
#
#     def print_graph(self):
#         for i in range(self.vertices):
#             temp = self.edges[i]
#             while temp:
#                 temp = temp.next
#             print("\n")
from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def detect_cycle(self, v, visited):
        # step 1: mark the current node as visited
        visited[v] = True
        print(v, end=' ')
        for node in self.graph[v]:
            if visited[node] == False:
                self.detect_cycle(node, visited)
            else:
                continue

    def DFS(self, v): # iterative
        visited = [False]*len(self.graph)
        self.detect_cycle(v, visited)


    def BFS(self, v):
        visited = [False] * len(self.graph)
        queue = deque([v])
        visited[v] = True
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for ele in self.graph[node]:
                if visited[ele] == False:
                    queue.append(ele)
                    visited[ele] = True
                else:
                    continue

    def DFS_new(self, s): # recursive
        visited = [False] * len(self.graph)
        stack = []
        stack.append(s)
        while stack:
            # pop a vertext from stack and print it
            s = stack[-1]
            stack.pop()
            if not visited[s]:
                visited[s] = True
            for node in self.graph[s]:
                if not visited[node]:
                    stack.append(node)
'''
The above code traverses only the vertices reachable from a given source vertex;
All the vertices may not be reachable from a given vertex (example disconnected graph)
To do complete DFS traversal of such graphs, we must call DFSutil for every vertex.
'''
if __name__ == '__main__':
    V = 5
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print("The following is DFS from starting point")
    graph.DFS(2)
    graph.BFS(2)
