
# Given an undirected graph and a number m, determine if the graph can be 
# colored with at most m colors such that no two adjacent vertices of the graph are 
# colored with the same color. Here coloring of a graph means assignment of colors to all vertices.

# The graph is represented using adjacency matrix, graph[i][j] will be 1 if there is
# a direct connection between vertices i and j; 0 otherwise

# sample graph:
# (3)---(2)
#  |   / |
#  |  /  |
#  | /   |
# (0)---(1)

# returns True if "color" can be assigned to current_vertex; False otherwise
def can_assign_color(graph, current_vertex, color, assigned_colors):
    for neighbor in range(len(graph)):
        if graph[current_vertex][neighbor] == 1:
            if neighbor < len(assigned_colors) and color == assigned_colors[neighbor]:
                return False

    return True

# this is the function that will be called by the client, for backtracking
# you typically write a recursive function that will be called from here;
# in python, you can have the recursive function nested inside the client facing
# function
def graph_coloring(graph, m):
    """
    Check if the input graph can be "m" colored
    graph: adjacency matrix representing the graph
    m: number of colors

    Returns: tuple (can_color, assigned_colors)
    can_color: True if graph can be colored with at most m colors; False otherwise
    assigned_colors: list of colors assigned to each vertex; empty list if can_color is False
    """
    
    def coloring_helper(graph, m, assigned_colors):
        if len(graph) == len(assigned_colors):
            return True

        current_vertex = len(assigned_colors)

        for color in range(1, m+1):
            if can_assign_color(graph, current_vertex, color, assigned_colors):
                assigned_colors.append(color)
                if coloring_helper(graph, m, assigned_colors):
                    return True
                assigned_colors.pop()

        return False

    assigned_colors = []
    if coloring_helper(graph, m, assigned_colors):
        return True, assigned_colors
    else:
        return False, []

def main():
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    m = 3

    can_color, assigned_colors = graph_coloring(graph, m)
    if can_color:
        print(f"Graph can be colored with at most {m} colors")
        print(assigned_colors)
    else:
        print(f"Graph cannot be colored with at most {m} colors")

if __name__ == "__main__":
    main()

# output
# Graph can be colored with at most 3 colors
# [1, 2, 3, 2]

