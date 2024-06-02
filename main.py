import heapq

# Convert letters into their respective numbers
def letter_to_number(letter):
    if letter.isupper():
        return ord(letter) - ord("A")
    else:
        return ord(letter) - ord("a") + 26

# Create nodes 
class Graph:
    def _init_(self,country,build,destroy,vertices):
        self.V = vertices # Vertices as each country/buil/destroy will be a square
        self.finalcost = 0
        self.graph = [[] for _ in range(vertices)]

        

# Taking in inputs
input = input()

country_str, build_str, destroy_str = input.split()

# Splitting inputs into the 3 matrices
country = [[int(x) for x in str(part)] for part in country_str.split(",")]
build = [[letter_to_number(x) for x in part] for part in build_str.split(",")]
destroy = [[letter_to_number(x) for x in part] for part in destroy_str.split(",")]

vertices = len(country)

g = Graph(country,build,destroy,vertices)

print()

# 111,111,111 ABC,ABC,ABC abc,abc,abc