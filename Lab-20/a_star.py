import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic estimate to goal node
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def a_star(grid, start, end):
    open_list = []
    closed_list = set()
    
    start_node = Node(start)
    end_node = Node(end)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.position)
        
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])
            
            if (0 <= node_position[0] < len(grid) and
                0 <= node_position[1] < len(grid[0]) and
                grid[node_position[0]][node_position[1]] == 0):
                
                if node_position in closed_list:
                    continue
                
                child = Node(node_position, current_node)
                child.g = current_node.g + 1
                child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
                child.f = child.g + child.h
                
                if any(open_node.position == child.position and open_node.f <= child.f for open_node in open_list):
                    continue
                
                heapq.heappush(open_list, child)

    return None

# Take user inputs for grid, start, and end points
rows = int(input("Enter the number of rows in the grid: "))
cols = int(input("Enter the number of columns in the grid: "))

print("Enter the grid (0 for path, 1 for obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    grid.append(row)

start = tuple(map(int, input("Enter the start position as 'row col': ").split()))
end = tuple(map(int, input("Enter the end position as 'row col': ").split()))

# Run A* algorithm
path = a_star(grid, start, end)

# Display the result
if path:
    print("Path from start to end:")
    for step in path:
        print(step)
else:
    print("No path found.")

"""
Enter the number of rows in the grid: 5
Enter the number of columns in the grid: 5
Enter the grid (0 for path, 1 for obstacle):
Row 1: 0 1 0 0 0
Row 2: 0 1 0 1 0
Row 3: 0 0 0 1 0
Row 4: 0 1 0 0 0
Row 5: 0 0 0 1 0
Enter the start position as 'row col': 0 0
Enter the end position as 'row col': 4 4
"""