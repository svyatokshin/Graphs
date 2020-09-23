"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        # self.vertices ={
        #     A: set(E, B),
        #     B: set(C, D, A F),
        #     C: set(B),
        #     D: set(B),
        #     F: set(B),
        #     E: set(E)
        # }

        # self.vertices = [

        # ]

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

        # for node in self.vertices:
        #     node.append(0)

        # new_node_row = [0] * len(self.vertices)
        # self.vertices.append(new_node_row)

    # def delete_vertex(self, vertex_id):
        # if vertex_id not in self.vertices:
        #     self.vertices[vertex_id] = 0
        # delete the key-value pair
        # find all references to this vertex

    # def delete_edge(self, v1, v2):
        # access v1, remove v2
        # access v2, remove v1

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return None

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # prime the pump with the first node
        q.enqueue(starting_vertex)
        # make a set to track visited nodes
        visited = set()
        # while the queue isn't empty:
        while q.size() > 0:
            # dequeue from front of queue, this is our current node
            current_node = q.dequeue()
        # if we have not visited, let's:
            if current_node not in visited:
                print(current_node)
                # mark as visited
                visited.add(current_node)
        # get the vertex's neighbors
                neighbors = self.get_neighbors(current_node)
        # put them in the queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current_node = stack.pop()

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    stack.push(neighbor)

    # Base case
    # Call Itself
    # Progress toward the base case

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if visited is None:
        #     visited = set()
        # print(starting_vertex)

        # neighbors = self.get_neighbors(starting_vertex)
        # visited.add(starting_vertex)

        # for vertex in neighbors:
        #     if vertex not in visited:
        #         self.dft_recursive(vertex, visited)

        if starting_vertex in visited:
            return
        else:
            visited.add(starting_vertex)
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)

            if len(neighbors) == 0:
                return None

            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        while queue.size() > 0:
            curr = queue.dequeue()
            curr_path = curr['path']
            current_vertex = curr['current_vertex']

            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return curr_path

                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(curr_path)
                    new_path.append(vertex)
                    queue.enqueue({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        while stack.size() > 0:
            current_node = stack.pop()
            curr_path = current_node['path']
            current_vertex = current_node['current_vertex']

            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return curr_path

                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(curr_path)
                    new_path.append(vertex)
                    stack.push({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            path.append(starting_vertex)
        # base case?
        # In a search, when are we done searching?
        if starting_vertex == destination_vertex:
            return path

        visited.add(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        if len(neighbors) == 0:
            return None

        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)

                if result is not None:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
