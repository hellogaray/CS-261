# Course: CS 261 - OSU
# Author: Leonel Garay
# Assignment: Assignment 6: Graph Implementation
# Description: Implement the Direct Graph class by completing provided skeleton code.


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a new vertex to the graph. Vertex name does not need to be provided.
        """
        self.v_count += 1  # Increases count.
        tracker = [0] * self.v_count  # Tracker to use in append.
        self.adj_matrix.append(tracker)  # Appends tracker.
        for i in range(self.v_count - 1):
            self.adj_matrix[i].append(0)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds a new edge to the graph, connection two vertices with provided indices.
        """
        # If either (or both) vertex indices do not exist in the graph.
        if src >= self.v_count or dst >= self.v_count:
            return
        # I f the weight is not a positive integer or if src and dst refer to the same vertex, the method does nothing.
        if weight < -1 or src == dst:
            return
        else:
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes and edge between two vertices with provided names.
        """
        if src >= self.v_count or src < 0:  # If vertex indices do not exist in the graph, return.
            return
        if dst >= self.v_count or dst < 0:  # If there is no edge between them, return.
            return
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns a list of vertices of the graph. Order of the vertices in the list does not matter.
        """
        list_results = list(range(len(self.adj_matrix)))
        return list_results

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        # result_list = []
        # for i in self.adj_matrix:
        #     counter = 0
        #     while counter < len(self.adj_matrix):
        #         item = [sub_list[counter] for sub_list in self.adj_matrix]
        #         coun_zero = 0
        #         store_number = 0
        #         for i in item:
        #             if i == 0:
        #                 count_zero += 1
        #             if i != 0:
        #                 store_number = i
        #         result_list[counter] = [counter]
        #         result_list[counter].append(store_number)
        #         counter += 1
        #     result_list[counter].append(coun_zero)
        # return result_list

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex names and returns True if the sequence of vertices represents a valid path.
        """
        for i in range(len(path) - 1):
            if self.adj_matrix[path[i]][path[i + 1]] == 0:
                return False
        return True


    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
       



if __name__ == '__main__':
    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
