from collections import deque

# BFS function to perform breadth-first search on a graph
def bfs(graph, start_node):
    visited = set()  
    queue = deque([start_node])  
    visited.add(start_node)  
    bfs_order = []  
    
    # Perform BFS
    while queue:
        current_node = queue.popleft()  # Dequeue a node
        bfs_order.append(current_node)  # Add to visited order
        
        # Check all neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)  # Enqueue unvisited neighbors
                visited.add(neighbor)  # Mark as visited
                
    return bfs_order  # Return the order of nodes visited in BFS

# Function to input the graph from the user
def input_graph():
    graph = {}
    
    # Get number of nodes
    n = int(input("Enter the number of nodes: "))
    
    # Initialize the graph
    for i in range(n):
        graph[i] = []
    
    # Get edges from the user
    m = int(input("Enter the number of edges: "))
    print("Enter the edges (e.g., '0 1' for an edge between node 0 and node 1):")
    
    for _ in range(m):
        u, v = map(int, input().split())  # Read an edge
        graph[u].append(v)  # Add the edge u -> v
        graph[v].append(u)  # Add the edge v -> u (since the graph is undirected)
    
    return graph

# Main program to take input and run BFS
def main():
    # Input graph from the user
    graph = input_graph()
    
    # Input the starting node for BFS
    start_node = int(input("Enter the starting node for BFS: "))
    
    # Ensure the start node is valid
    if start_node not in graph:
        print("Invalid starting node!")
        return
    
    # Perform BFS and print the result
    result = bfs(graph, start_node)
    print("BFS traversal order starting from node", start_node, ":", result)

# Run the program
if __name__ == "__main__":
    main()

# Output
"""
Enter the number of nodes: 5
Enter the number of edges: 4
Enter the edges (e.g., '0 1' for an edge between node 0 and node 1):
0 1
0 2
1 3
1 4
Enter the starting node for BFS: 0

"""