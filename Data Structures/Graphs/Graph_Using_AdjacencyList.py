class Graph:
    def __init__(self,graph_dict):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph_dict.keys():
            self.graph_dict[vertex] = []
        else:
            print("Vertex with identity "+vertex+" already exists. Please Create Vertex with ther name.")

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.graph_dict.keys() and vertex2 in self.graph_dict.keys():
            self.graph_dict[vertex1].append(vertex2)
            self.graph_dict[vertex2].append(vertex1)
        else:
            print("The specified vertices are not present in Graph. Please create a vertex and then create a edge.")

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.graph_dict.keys() and vertex2 in self.graph_dict.keys():
            try:
                self.graph_dict[vertex1].remove(vertex2)
                self.graph_dict[vertex2].remove(vertex1)
            except ValueError:
                print("Edge Does Not Exists Between the 2 specified vertices "+vertex1+ " and "+vertex2+".")

        else:
            print("The specified vertices are not present in Graph. Please select proper vertices and then remove a edge.")

    def remove_vertex(self,vertex):
        if vertex in self.graph_dict.keys():
            for vertices in self.graph_dict[vertex]:
                self.graph_dict[vertices].remove(vertex)
            del self.graph_dict[vertex]
            

        else:
            print("The specified vertex is not present in Graph. Please select proper vertex to delete.")

    
    def breadth_first_search(self,vertex):
        """
        Time Complexity is O(V+E), V - no.of vertices & E - no.of edges
        Space Complexity is O(V)

        """
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        print("The result of BFS of the graph is ")
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.graph_dict[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
    
    def depth_first_search(self,vertex):
        """
        Time Complexity is O(V+E), V - no.of vertices & E - no.of edges
        Space Complexity is O(V)

        """
        visited = set()
        visited.add(vertex)
        stack = [vertex]
        print("The result of DFS of the graph is ")
        print(vertex)
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.graph_dict[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)

    def breadth_first_search(self,vertex):
        """
        Time Complexity is O(V+E), V - no.of vertices & E - no.of edges
        Space Complexity is O(V)

        """
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        print("The result of BFS of the graph is ")
        print(vertex)
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.graph_dict[current_vertex]:
                if adjacent_vertex not in visited:
                    
                    queue.append(adjacent_vertex)
        

    def print_graph(self):
        if self.graph_dict:
            for key,value in self.graph_dict.items():
                print(key,value,sep=" : ")

graph = Graph({})
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
# graph.print_graph()
# print("Graph After Adding the Edge")
graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","D")
graph.add_edge("B","G")
graph.add_edge("C","D")
graph.add_edge("C","E")
graph.add_edge("D","F")
graph.add_edge("E","F")
graph.add_edge("F","G")

graph.breadth_first_search("A")
graph.depth_first_search("A")
# graph.print_graph()
# print("Graph After Removing the Edge")
# graph.remove_edge("C","B")
# graph.print_graph()
# print("Graph After Removing the Vertex")
# graph.remove_vertex("D")
# graph.print_graph()


# graph.breadth_first_search("A")
