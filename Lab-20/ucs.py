import heapq

class UCS:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))
    
    def ucs(self, start, goal):
        # Priority Queue to store (cost, node)
        frontier = []
        heapq.heappush(frontier, (0, start))  # (cost, node)
        
        # Dictionary to store the shortest path to each node
        came_from = {start: None}
        cost_so_far = {start: 0}
        
        while frontier:
            current_cost, current_node = heapq.heappop(frontier)
            
            # If we reached the goal, reconstruct the path
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                return path[::-1], current_cost
            
            # Expand neighbors
            for neighbor, travel_cost in self.graph.get(current_node, []):
                new_cost = current_cost + travel_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    heapq.heappush(frontier, (new_cost, neighbor))
        
        return None, float('inf')  # If there's no path to the goal


# Function to take user input for the graph and run UCS
def main():
    ucs_algorithm = UCS()
    
    # Get the number of edges
    n = int(input("Enter the number of edges in the graph: "))
    
    # Get the edges from the user
    for _ in range(n):
        start, end, cost = input("Enter edge (start, end, cost): ").split()
        start, end, cost = start.strip(), end.strip(), int(cost)
        ucs_algorithm.add_edge(start, end, cost)
    
    # Get the start and goal nodes
    start_node = input("Enter the start node: ").strip()
    goal_node = input("Enter the goal node: ").strip()
    
    # Run UCS algorithm to find the shortest path
    path, total_cost = ucs_algorithm.ucs(start_node, goal_node)
    
    if path:
        print(f"Shortest path: {' -> '.join(path)}")
        print(f"Total cost: {total_cost}")
    else:
        print("No path found between the start and goal nodes.")

# Example Test Case:
if __name__ == "__main__":
    main()

"""
Enter the number of edges in the graph: 5
Enter edge (start, end, cost): A B 1
Enter edge (start, end, cost): B C 2
Enter edge (start, end, cost): A C 4
Enter edge (start, end, cost): C D 1
Enter edge (start, end, cost): B D 5
Enter the start node: A
Enter the goal node: D

"""