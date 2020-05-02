"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # this should be the room id in our case here and should be a dict
        self.vertices[vertex_id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

    def add_edge(self, v1, v2, v3):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices[v1]:
            self.vertices[v1][v2] = v3
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    # def bft(self, starting_vertex):
    #     """
    #     Print each vertex in breadth-first order
    #     beginning from starting_vertex.
    #     """
    #     # create a plan_to_visit queue and add starting_vertex to it
    #     plan_to_visit = Queue()
    #     plan_to_visit.enqueue(starting_vertex)
    #     # create a Set for visited_vertices
    #     visited_vertices = set()
    #     # while the plan_to_visit queue is not Empty:
    #     while plan_to_visit.size() > 0:
    #         # dequeue the first vertex on the queue
    #         current_vertex = plan_to_visit.dequeue()
    #         # if its not been visited
    #         if current_vertex not in visited_vertices:
    #             # print the vertex
    #             print(current_vertex)
    #             # mark it as visited, (add it to visited_vertices)
    #             visited_vertices.add(current_vertex)
    #             # add all unvisited neighbors to the queue
    #             for neighbor in self.get_neighbors(current_vertex):
    #                 if neighbor not in visited_vertices:
    #                     plan_to_visit.enqueue(neighbor)

    # def dft(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     """
    #     # create a plan_to_visit stack and add starting_vertex to it
    #     plan_to_visit = Stack()
    #     plan_to_visit.push(starting_vertex)
    #     # create a Set for visited_vertices
    #     visited_vertices = set()
    #     # while the plan_to_visit stack is not Empty:
    #     while plan_to_visit.size() > 0:
    #         # pop the first vertex from the stack
    #         current_vertex = plan_to_visit.pop()
    #         # if its not been visited
    #         if current_vertex not in visited_vertices:
    #             # print the vertex
    #             print(current_vertex)
    #             # mark it as visited, (add it to visited_vertices)
    #             visited_vertices.add(current_vertex)
    #             # add all unvisited neighbors to the stack
    #             for neighbor in self.get_neighbors(current_vertex):
    #                 if neighbor not in visited_vertices:
    #                     plan_to_visit.push(neighbor)

    # def bfs(self, starting_vertex, destination_vertex):
    #     """
    #         Return a list containing the shortest path from
    #         starting_vertex to destination_vertex in
    #         breath-first order.
    #         """
    #     # create a empty queue, and enqueue a PATH to the starting vertex
    #     # create a set for visited vertices
    #     visited_vertices = set()

    #     neighbors_to_visit = Queue()
    #     neighbors_to_visit.enqueue([starting_vertex])
    #     # while the queue is not empty
    #     while neighbors_to_visit.size() > 0:
    #         # dequeue the first PATH in the queue
    #         current_path = neighbors_to_visit.dequeue()
    #         print(f"current_path: {current_path}")
    #         # grab the last vertex in the path
    #         current_vertex = current_path[-1]
    #         # if it hasn't been visited
    #         if current_vertex not in visited_vertices:
    #             # check if its the target
    #             if current_vertex == destination_vertex:
    #                 return current_path
    #                 # Return the path
    #             # mark it as visited
    #             visited_vertices.add(current_vertex)
    #             # make new versions of the current path, with each neighbor added to them
    #             for next_vertex in self.get_neighbors(current_vertex):
    #                 # duplicate the path
    #                 new_path = list(current_path)
    #                 # add the neighbor
    #                 new_path.append(next_vertex)
    #                 # add the new path to the queue
    #                 neighbors_to_visit.enqueue(new_path)
    # pass  # TODO

    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #         Return a list containing a path from
    #         starting_vertex to destination_vertex in
    #         depth-first order.
    #         """
    #     # This solution takes a slightly different approach as to how we are storing the path
    #     # Now, we always queue up the next vertex we want to see, and a list of all the vertices we looked at to get here
    #     # so if we are queueing up vertex 3 from our example, the tuple we create will be (3, [1,2])
    #     # because we had to go through 1 and 2 to get here
    #     visited_vertices = set()

    #     neighbors_to_visit = Stack()
    #     # add the first vertex, and an empty list indicating that we have not been to any other vertices yet
    #     neighbors_to_visit.push((starting_vertex, []))
    #     # loop through the stack
    #     while neighbors_to_visit.size() > 0:
    #         # This will have (current_vertex, path)
    #         current_vertex_plus_path = neighbors_to_visit.pop()
    #         # pull out the current vertex so its easier to read
    #         current_vertex = current_vertex_plus_path[0]
    #         # pull out the path so its easier to read
    #         current_path = current_vertex_plus_path[1]
    #         # make sure the vertex isnt something we have seen already
    #         if current_vertex not in visited_vertices:

    #             # if the vertex is the destination return it plus the path we took to get here
    #             if current_vertex == destination_vertex:
    #                 # eg: if the vertex was 6, and we went through 1, 2, 4 to get here, add that to complete the full path
    #                 updated_path = current_path + [current_vertex]
    #                 return updated_path

    #             # mark the vertex as visited
    #             visited_vertices.add(current_vertex)
    #             # add neighbors to the stack
    #             for neighbor in self.get_neighbors(current_vertex):
    #                 updated_path = current_path + [current_vertex]
    #                 neighbors_to_visit.push((neighbor, updated_path))


g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_vertex(8)
g.add_vertex(9)
print(g.vertices)

g.add_edge(0, 'n', 5)
print(g.vertices)
print(g.get_neighbors(0))
