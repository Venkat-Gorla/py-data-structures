
# directed graph DFS without recursion

from directed_graph import DirectedGraph

class DFS:
    def __init__(self, graph):
        self.graph = graph

    def dfs_iterative(self, start):
        """
        Perform Depth-First Search (DFS) from a given start vertex
        """
        visited = [False] * self.graph._vertices
        result = []
        node_stack = [start]

        while node_stack:
            current = node_stack.pop()
            visited[current] = True
            result.append(current)

            for neighbor in reversed(self.graph._connections[current]):
                if not visited[neighbor]:
                    node_stack.append(neighbor)

        return result

if __name__ == "__main__":
    graph = DirectedGraph(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)

    dfs_instance = DFS(graph)

    # Expected output: DFS from node 0: [0, 1, 3, 4, 5, 2]
    print("DFS from node 0:", dfs_instance.dfs_iterative(0))

    # some additional test cases for completeness
    assert dfs_instance.dfs_iterative(0) == [0, 1, 3, 4, 5, 2]
    assert dfs_instance.dfs_iterative(3) == [3, 4, 5] # Start from node 3
    assert dfs_instance.dfs_iterative(5) == [5]

    print("All test cases passed!")

# output
# DFS from node 0: [0, 1, 3, 4, 5, 2]
# All test cases passed!

