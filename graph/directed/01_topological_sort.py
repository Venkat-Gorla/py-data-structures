
# find the topological sort order for a directed acyclic graph (DAG)
# formal definition: find a linear ordering of the graph vertices such that for every directed edge (u, v), vertex u comes before v in the output ordering
# it is mainly used for ordering a list of tasks based on their dependency, if A depends on B, then the order of execution will be BA;
# naturally if you have a circular dependency, then topological sort is Not possible
# Note: for unrelated tasks, you can have multiple topological sorts

class DirectedGraph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._connections = [[] for _ in range(vertices)]

    def add_edge(self, source, dest):
        self._connections[source].append(dest)

    def __get_topo_util(self, current, visited, output):
        """
        private utility function to get the topological sort
        """
        visited[current] = True

        for neighbor in self._connections[current]:
            if not visited[neighbor]:
                self.__get_topo_util(neighbor, visited, output)

        output.append(current)

    def get_topological_sort(self):
        """
        Get the topological sort for a directed acyclic graph, caller should 
        ensure there are no cycles in the graph.

        Returns:
        List of graph vertices that represents a topological sort
        """
        visited = [False] * self._vertices
        output = []

        for current in range(self._vertices):
            if not visited[current]:
                self.__get_topo_util(current, visited, output)

        # The output should be considered a stack, so we will reverse the list before returning
        output.reverse()
        return output

def main():
    g = DirectedGraph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    topo_sort = g.get_topological_sort()
    print(f"Topological sort of the given graph is: {topo_sort}")

if __name__ == "__main__":
    main()

# output:
# Topological sort of the given graph is: [5, 4, 2, 3, 1, 0]

