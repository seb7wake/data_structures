import random
from random import randint, choice
import math

#vertex class
class Vertex: 
    #initializes vertex node with a key and any adjacent vertices
    def __init__(self, key):
        self.key = key
        self.adjacent = {}

    # adds an edge from one vertex to another at a certain weight
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    #returns all vertices connected to acertain vertex
    def get_connections(self):
        return self.adjacent.keys()  

    # return the weight of the edge between 2 vertices
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    # gets the integer representation of a vertex object
    def get_key(self):
        return self.key

#Graph class
class Graph:

    #initializes graph with a dictionary of connected 
    # vertices and a number of vertices
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    #adds a vertex to the graph
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1 #increment number of vertices
        new_vertex = Vertex(node) #initialize new vertex node
        self.vert_dict[node] = new_vertex #adding vertex node into the vert_dict dictionary
        return new_vertex

    #adds an adge between 2 vertices. If vertices
    #do not exist then create them
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm) #creates vertex if not in the graph
        if to not in self.vert_dict:
            self.add_vertex(to) #creates vertex if not in the graph
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost) #connects one vertex to another
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost) #connects one vertex to another in reverse order
    
    #breadth-first search function (part 2)
    def BFS(self):
        s = choice(list(self.vert_dict))
        s = self.vert_dict[s]
        # Mark all the vertices as not visited
        visited = []
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        total = 0
        while len(queue) != 0:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            visited.append(s)
            for i in list(s.get_connections()):
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    # add weight of two vertices to the total after deciding to take that edge
                    total += s.get_weight(i) 
        return total  

    # Prim's algorithm (part 3)
    def primMST(self, v):
        graph1 = self
        n = len(graph1.vert_dict)
        con =[v] # start vertex for prim's algorithm
        total = 0 
        while len(con) < n:
            min = math.inf #setting the minimum value to an infinite number
            for i in con:
                #gets all the connections of i
                for j in self.vert_dict[i].get_connections(): 
                    #if j is unique and the weight of the edge between i and j is less than the current min value
                    if j.get_key() not in con and self.vert_dict[i].get_weight(j) < min:
                        #set min vertices and min weight
                        minV1 = j.get_key()
                        minV2 = i
                        min = self.vert_dict[i].get_weight(j)
            con.append(minV1) #add new vertex
            total += self.vert_dict[minV2].get_weight(self.vert_dict[minV1]) #add to the total weight
        return total

    #function to create a random connected graph with n vertices (part 1)
    def initialize_graph(self, n):
        for i in range(2, n+1):
            x =  randint(1, i-1) 
            s=[]
            for k in range(x):
                s.append(randint(1, i-1))
            for n in s:
                w = randint(10, 100)
                self.add_edge(i, n, w) #adds an edge between i and n with weight w
        return self

# Function to compare value of BST and prim's total weight calculations (part 4).
# Input variable k specifies how many times to generate a graph.
def compare(k):
    diffs = {20: [], 40: [], 60: []} #dictionary for different sizes of graph
    for i in diffs.keys():
        for m in range(k):
            g = Graph() #make new graph
            g = g.initialize_graph(i) #populate graph with i vertices
            bfs = g.BFS() #run BFS 
            prim = g.primMST(1) # run prim's with start vertex 1
            diff = (bfs-prim)/prim * 100 #calculate teh percentage difference between the two algorithms
            diffs[i].append(diff) # append this difference to the diffs dict
    for v in diffs.keys(): 
        diffs[v] = sum(diffs[v]) / len(diffs[v]) #get the average difference
    return diffs

if __name__ == '__main__': 
    g = Graph()
    # create random graph with 5 vertices (part 1)
    n = 5
    g = g.initialize_graph(n)
       
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0, 1, 15)
    graph.add_edge(0, 3, 7)
    graph.add_edge(0, 4, 10)
    graph.add_edge(1, 2, 9)
    graph.add_edge(1, 3, 11)
    graph.add_edge(1, 5, 9)
    graph.add_edge(2, 4, 12)
    graph.add_edge(2, 5, 7)
    graph.add_edge(3, 4, 8)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 8)
    print('BFS function total weight (part 2):')
    print(graph.BFS()) #prints total weight for the above graph using breadth-first search
    print("Prim's Algorithm total weight (part 3):")
    print(graph.primMST(0)) #prints total weight using prim's algorithm on the above graph 
    print("Compare Prim's Algoritm with BFS for randomly generated graphs (part 4):")
    val =compare(100)
    print("for n = 20 & k = 100:",  val[20],"% difference")
    print("for n = 40 & k = 100:",  val[40], "% difference")
    print("for n = 60 & k = 100:",  val[60], "% difference")
