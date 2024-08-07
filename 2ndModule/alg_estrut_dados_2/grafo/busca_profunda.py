class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex, edge):
        if vertex in self.adjacency_list:
            self.adjacency_list[vertex].append(edge)
        else:
            self.adjacency_list[vertex] = [edge]

    def remove_edge(self, vertex, edge):
        if vertex in self.adjacency_list:
            if edge in self.adjacency_list[vertex]:
                self.adjacency_list[vertex].remove(edge)
                if len(self.adjacency_list[vertex]) == 0:
                    del self.adjacency_list[vertex]

    def dfs(self, start_vertex):
        visited = set()

        def dfs_recursive(vertex):
            visited.add(vertex)
            print(vertex)

            if vertex in self.adjacency_list:
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start_vertex)

    def search_node(self, value):
        for vertex in self.adjacency_list:
            if value in self.adjacency_list[vertex]:
                return vertex
        return None


graph = Graph()

while True:
    print("1. Add an edge")
    print("2. Remove an edge")
    print("3. Search for a node")
    print("4. Perform DFS")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        vertex = input("Enter the vertex: ")
        edge = input("Enter the edge: ")
        graph.add_edge(vertex, edge)
    elif choice == "2":
        vertex = input("Enter the vertex: ")
        edge = input("Enter the edge: ")
        graph.remove_edge(vertex, edge)
    elif choice == "3":
        value = input("Enter the value to search: ")
        vertex = graph.search_node(value)
        if vertex:
            print("Node found in vertex:", vertex)
        else:
            print("Node not found")
    elif choice == "4":
        start_vertex = input("Enter the starting vertex for DFS: ")
        graph.dfs(start_vertex)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
