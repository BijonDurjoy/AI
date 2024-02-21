# Defining adjacency matrix
a = [[] for _ in range(100)]
visited = [0] * 20


def IDS(p, limit):
    global visited

    # If current node is the source, print and return true
    if p + 1 == source:
        print(p + 1)
        return True

    # If node is not visited, mark it visited and print
    if visited[p] == 0:
        visited[p] = 1
        print(p + 1, "==>", end=" ")

    # If limit allows, explore neighbors
    if limit > 0:
        for k in a[p]:
            if visited[k] == 0:
                if IDS(k, limit - 1):
                    return True

    return False


if __name__ == "__main__":
    # Getting number of edges and vertices
    print("\t\t\tGraphs")
    Y = int(input("Enter the required number of edges: "))
    X = int(input("Enter the required number of vertices: "))

    # Creating edges
    for _ in range(Y):
        x1, x2 = map(int, input("Enter the format of the edges (format: x1 x2) : ").split())
        a[x1 - 1].append(x2 - 1)
        a[x2 - 1].append(x1 - 1)

    # Getting the goal
    source = int(input("Enter the goal: "))

    # Iterative deepening loop
    for i in range(10):
        for j in range(20):
            visited[j] = 0
        print("Level:", i + 1, "->", end=" ")
        if IDS(0, i):
            print("\nNode found")
            break
        else:
            print()

#Output
"""
Enter the required number of edges: 5
Enter the required number of vertices: 5
Enter the format of the edges (format: x1 x2) : 1 2
Enter the format of the edges (format: x1 x2) : 2 3
Enter the format of the edges (format: x1 x2) : 1 4
Enter the format of the edges (format: x1 x2) : 4 5
Enter the format of the edges (format: x1 x2) : 4 6
Enter the goal: 5
Level: 1 -> 1 ==> 
Level: 2 -> 1 ==> 2 ==> 4 ==> 
Level: 3 -> 1 ==> 2 ==> 3 ==> 4 ==> 5

Node found
"""