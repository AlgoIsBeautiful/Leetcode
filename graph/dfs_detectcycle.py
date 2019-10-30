# 0 -> 2 -> 0 
# 0 -> 1 -> 2 -> 0 
# DFS for a connected graph produces a tree
# A back edge is an edge that is from a node to itself (self-loop) or one of its ancestor
# For a disconnected graph, we get the DFS forest as output. To detect cycle, we can check for a cycle in individual trees by checking back edges.

from collections import defaultdict

class Graph():

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def graph_contain_cycle(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCycle(node, visited, recStack):
                    return True
        return False 

    def isCycle(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCycle(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False
        
    # A recursive function that uses visited[] and parent to detect 
    # cycle in subgraph reachable from vertex v. 
    def isCyclicUtil(self,v,visited,parent): 
  
        #Mark the current node as visited  
        visited[v]= True
  
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            # If the node is not visited then recurse on it 
            if  visited[i]==False :  
                if(self.isCyclicUtil(i,visited,v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=i: 
                return True
          
        return False
           
   
    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self): 
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
        for i in range(self.V): 
            if visited[i] ==False: #Don't recur for u if it is already visited 
                if(self.isCyclicUtil(i,visited,-1))== True: 
                    return True
          
        return False
if __name__ == '__main__':
    g = Graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    if g.graph_contain_cycle(): 
        print ("Graph has a cycle")
    else: 
        print ("Graph has no cycle")