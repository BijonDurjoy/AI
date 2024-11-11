from collections import deque

# Function to perform BFS traversal
def bfs(graph, start_node):
    # Create a queue to manage the nodes to visit
    queue = deque([start_node])
    
    # Set to track visited nodes to avoid revisiting them
    visited = set()
    
    # Mark the starting node as visited
    visited.add(start_node)
    
    # List to keep track of the BFS traversal order
    traversal_order = []
    
    # Loop until there are nodes in the queue
    while queue:
        # Pop the first node in the queue
        current_node = queue.popleft()
        
        # Add the current node to the traversal order list
        traversal_order.append(current_node)
        
        # Explore all the neighbors of the current node
        for neighbor in graph[current_node]:
            # If the neighbor has not been visited yet
            if neighbor not in visited:
                # Mark it as visited and add it to the queue
                visited.add(neighbor)
                queue.append(neighbor)
    
    # Return the BFS traversal order
    return traversal_order

# Main function to drive the program
def main():
    # Input the number of nodes and edges
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    num_edges = int(input("Enter the number of edges: "))
    
    # Initialize an empty graph as a dictionary
    graph = {i: [] for i in range(num_nodes)}
    
    # Input the edges of the graph
    print("Enter the edges in the format (node1 node2):")
    for _ in range(num_edges):
        node1, node2 = map(int, input().split())
        # Add an edge in both directions (undirected graph)
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    # Input the starting node for BFS
    start_node = int(input("Enter the starting node for BFS: "))
    
    # Perform BFS and print the result
    result = bfs(graph, start_node)
    print(f"BFS Traversal Order: {result}")

# Run the main function if this is the main module
if __name__ == "__main__":
    main()


"""
Enter the number of nodes in the graph: 6
Enter the number of edges: 7
Enter the edges in the format (node1 node2):
0 1
0 2
1 3
1 4
2 5
3 5
4 5
Enter the starting node for BFS: 0
"""