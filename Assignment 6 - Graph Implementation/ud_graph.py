# Course: CS 261 - OSU
# Author: Leonel Garay
# Assignment: Assignment 6: Graph Implementation
# Description: Implement the Undirected Graph class by completing provided skeleton code.


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Adds a new vertex to the graph. If vertex already in list, return.
        """
        if v not in self.adj_list:
            self.adj_list[v] = []
        else:
            return

    def add_edge(self, u: str, v: str) -> None:
        """
        Adds a new edge to the graph.
        """
        if u == v:  # Do nothing if u and v are the same.
            return
        # If vertex names do not exist in the graph, it creates them.
        if u not in self.adj_list:
            self.adj_list[u] = [v]
        if v not in self.adj_list:
            self.adj_list[v] = [u]
        # Append edges to the graph.
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Removes an edge between two vertices with provided names.
        """
        if v in self.adj_list and u in self.adj_list:  # Check to make sure both exist.
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)  # Remove v from u.
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)  # Remove u from v.
        else:  # Else do nothing, return.
            return

    def remove_vertex(self, v: str) -> None:
        """
        Removes a vertex with a given name and all edges incident to it from the graph.
        """
        if v in self.adj_list:  # If v exist it completely removes it from dictionary.
            self.adj_list.pop(v)
        for i in self.adj_list:  # Iterates through list removing instances of v.
            if v in self.adj_list[i]:
                self.adj_list[i].remove(v)
            else:
                continue

    def get_vertices(self) -> []:
        """
        Returns a list of vertices of the graph.
        """
        vertices_list = []
        for i in self.adj_list:
            vertices_list.append(i)
        return vertices_list

    def get_edges(self) -> []:
        """
        Returns a list of edges in the graph. Each edge is returned as a tuple of two incidents vertex names.
        """
        vertices_list = []  # Creates a new list.
        for i, j in self.adj_list.items():
            position = 0  # Sets position to zero.
            while position < len(j):  # Iterates through dictionary.
                new_tuple = (i, j[position])  # Creates a new tuple.
                new_tuple2 = (j[position], i)
                if new_tuple not in vertices_list and new_tuple2 not in vertices_list :  # Sorts the position and ensure it is not on list.
                    vertices_list.append(new_tuple)
                position += 1  # Moves position by one.
        return vertices_list

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex names and returns True if sequence of vertices represents a valid path in the graph.
        """
        if len(path) == 0:  # When path is just empty.
            return True
        if len(path) == 1:  # When path is just one.
            if path[0] in self.adj_list:
                return True
            else:
                return False
        new = UndirectedGraph()  # Create new undirected graph.
        for i in path:  # Adds edges
            new.add_edge(path[0], i)
        new_edges = new.get_edges()
        old_edges = self.get_edges()
        sort_test = sorted(set(new_edges) - set(sorted(old_edges)))
        # Compares the results stored in sort_test to new_edges.
        if len(sort_test) != len(new_edges):
            return True
        if len(sort_test) == len(new_edges):
            return False

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs a depth-first search in the graph and returns a list of vertices visited during the search.
        """

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """

    def count_connected_components(self):
        """
        TODO: Write this implementation
        """

    def has_cycle(self):
        """
        TODO: Write this implementation
        """


if __name__ == '__main__':

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
