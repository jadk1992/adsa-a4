import heapq

# Convert letters into their respective numbers
def letter_to_number(letter):
    if letter.isupper():
        return ord(letter) - ord("A")
    else:
        return ord(letter) - ord("a") + 26

# Create nodes 
class Graph:
    def __init__(self,country,build,destroy,vertices):
        self.V = vertices # Vertices as each country/buil/destroy will be a square
        self.totalcost = 0 # Init final cost that will be
        self.startingcost = 0 # Init cost for new graph  
        self.graph = [[] for _ in range(vertices)] # Init a graph that is empty for the mst

        for i in range(vertices):
            for j in range(i, vertices):
                if country[i][j] == 0:
                    self.edge(i,j,build[i][j])
                else:
                    self.edge(i,j, -destroy[i][j])
                    self.startingcost += destroy[i][j]

    def edge(self, startingnode, node, cost):
        self.graph[startingnode].append((node,cost))    
        self.graph[node].append((startingnode,cost))    

    def prim_alg(self):
        pQueue = [] # init a priority queue that will store the edge costs of the surrounding nodes
        srcCity = 0 # init a inital node/source node that will act as the starting point for the MST

        travelled = [] # (mst set) init a set that will store all the nodes that have been visited

        cost = [float('inf')] * self.V # init a "cost" list and all inital costs are infinty ('inf')

        heapq.heappush(pQueue, (0, srcCity))
        cost[srcCity] = 0

        while pQueue: # While the priority queue is not empty
            # add the current node stored in pQueue to the current city
            currentCost, currentCity = heapq.heappop(pQueue)

            if currentCity in travelled: # check if the currentCity has already been visited
                continue
            
            travelled.append(currentCity) # add the currentCity to the list of travelled city
            
            self.totalcost += currentCost

            for node,node_cost in self.graph[currentCity]:
                
                if node not in travelled and cost[node] > node_cost:
                    cost[node] = node_cost
                    heapq.heappush(pQueue, (cost[node], node))

        self.totalcost = self.startingcost + self.totalcost

        return self.totalcost
      

# Taking in inputs
input = input()

country_str, build_str, destroy_str = input.split()

# Splitting inputs into the 3 matrices
country = [[int(x) for x in str(part)] for part in country_str.split(",")]
build = [[letter_to_number(x) for x in part] for part in build_str.split(",")]
destroy = [[letter_to_number(x) for x in part] for part in destroy_str.split(",")]


vertices = len(country)

g = Graph(country, build, destroy, vertices)
g.prim_alg()
print(g.totalcost)

# 011,101,110 ABD,BAC,DCA ABD,BAC,DCA