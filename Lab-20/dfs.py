# Function to perform DFS traversal
def dfs(graph, start_node):
    # Stack to keep track of nodes to visit (LIFO order for DFS)
    stack = [start_node]
    
    # Set to keep track of visited nodes
    visited = set()
    
    # List to store the order of traversal
    traversal_order = []
    
    # Continue until all nodes in the stack are processed
    while stack:
        # Pop the last node from the stack
        current_node = stack.pop()
        
        # Process the node if it hasn't been visited
        if current_node not in visited:
            # Mark the node as visited
            visited.add(current_node)
            # Add the node to the traversal order
            traversal_order.append(current_node)
            
            # Add all unvisited neighbors to the stack
            # (Reversed to maintain order)
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    # Return the list with the order of visited nodes
    return traversal_order

# Main function to drive the program
def main():
    # Input the number of nodes and edges
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    num_edges = int(input("Enter the number of edges: "))
    
    # Initialize the graph as an empty dictionary
    graph = {i: [] for i in range(num_nodes)}
    
    # Input edges
    print("Enter the edges in the format (node1 node2):")
    for _ in range(num_edges):
        node1, node2 = map(int, input().split())
        # Add each edge to the graph (undirected graph)
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    # Input the starting node for DFS
    start_node = int(input("Enter the starting node for DFS: "))
    
    # Perform DFS and print the traversal order
    result = dfs(graph, start_node)
    print(f"DFS Traversal Order: {result}")

# Run the main function if this file is executed directly
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
Enter the starting node for DFS: 0

"""