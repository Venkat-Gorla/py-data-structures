
# undirected graph class representation and cycle detection
# similar to what we do in C++, vector<vector> becomes nested list [[]]
class UndirectedGraph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._connections = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self._connections[u].append(v)
        self._connections[v].append(u)

    def is_cycle_util(self, current, visited, parent):
        visited[current] = True

        for neighbor in self._connections[current]:
            if not visited[neighbor]:
                if self.is_cycle_util(neighbor, visited, current):
                    return True
            elif neighbor != parent:
                return True

        return False

    def is_cycle(self):
        visited = [False] * self._vertices

        for current in range(self._vertices):
            if not visited[current]:
                if self.is_cycle_util(current, visited, -1):
                    return True

        return False

def test_negative():
    g2 = UndirectedGraph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(0, 3)

    if g2.is_cycle():
        print("Graph g2 contains cycle")
    else:
        print("Graph g2 does Not contain cycle")

def main():
    # create a graph with 5 vertices and a cycle
    graph = UndirectedGraph(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 0)

    if graph.is_cycle():
        print("Graph contains cycle")
    else:
        print("Graph does Not contain cycle")

    test_negative()

main()

# output
# Graph contains cycle
# Graph g2 does Not contain cycle

