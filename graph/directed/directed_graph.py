
# basic functionality for directed graph that can be reused in other places

class DirectedGraph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._connections = [[] for _ in range(vertices)]

    def add_edge(self, source, dest):
        self._connections[source].append(dest)

