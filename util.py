
# Note: This Queue class is sub-optimal. Why?
# answer: it isn't using an actual linked list for either... less efficient  time/space complexity


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.verts = {}

    # def add_vertex(self, vertex_id):
    #     """
    #     Add a vertex to the graph.
    #     """
    #     # this should be the room id in our case here and should be a dict
    #     # LOOK AT NEXT LINE TO FIX ONE ISSUE
    #     # this should not be a preset list... should be added from get_exits()
    #     self.vertices[vertex_id] = {}
    def addV(self, vertex_id):
        self.vertices[vertex_id] = set()
        self.verts[vertex_id]= set()

    # def init_R_edges(self, v1, v2):
    #     if v1 in self.vertices:
    #         self.vertices[v1][v2] = '?'

    # def add_edge(self, v1, v2, v3):
    #     """
    #     Add a directed edge to the graph.

    #     v1 = the current_room/room
    #     v2 = the direction in get_exits()
    #     v3 = is what room is in dir v2
    #     """

    #     if v1 in self.vertices and v3 in self.vertices:
    #         self.vertices[v1][v2] = v3
    #     else:
    #         raise IndexError("That vertex does not exist!")
    def addEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.verts[v1].add(v2)
    # def deleteEgde(self, v1,v2):
    #     if v2 in self.vert[v1]:
    #         pass

    def get_neighbors(self, vertex_id):#for self.vertices
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def get_Nbors(self, vertex_id):
        return self.verts[vertex_id]
                
    def dft(self, starting_vertex, all):
        """
        this should travel down one hallway and end at the end just fine.. 
        returns a path to end of a hallway        
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push((starting_vertex, []))
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex from the stack
            current_path_and_V = plan_to_visit.pop()
            current_vertex = current_path_and_V[0]
            current_path = current_path_and_V[1]
            # if its not been visited
            if current_vertex not in visited_vertices: #and current_vertex not in all:
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited ( on this move) neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices and neighbor not in all:
                        new_path = current_path.copy() + [current_vertex]
                        plan_to_visit.push((neighbor, new_path))
                    #if the neighbor at the end of the hallway AND has only one neighbor
                    elif neighbor in visited_vertices and len(self.get_neighbors(current_vertex)) <= 1:
                        the_path = current_path + [current_vertex]
                        return the_path
                # return current_path.copy() + [current_vertex]

    def bfs(self, path):
        """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex(vertex with options left to pick) in
            breath-first order.
            """
        # create a empty queue, and enqueue a PATH to the starting vertex
        # create a set for visited vertices
        visited_vertices = set()

        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([path[-1]])
        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH in the queue
            current_path = neighbors_to_visit.dequeue()
            # print(f"current_path: {current_path}")
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if its the target
                # if len(self.get_neighbors(current_vertex)) > 1 :
                if len(self.get_neighbors(current_vertex)) >= 3:
                    return current_path[1:]
                    # Return the path
                visited_vertices.add(current_vertex)
                # mark it as visited
                # make new versions of the current path, with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(current_path)
                    # add the neighbor
                    new_path.append(next_vertex)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)
            # if current_vertex == None:
            #     print('here it is')
    def bfs_all(self, starting_vertex, target_rooms):
        """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex(vertex with options left to pick) in
            breath-first order.
            """
        # create a empty queue, and enqueue a PATH to the starting vertex
        # create a set for visited vertices
        visited_vertices = set()

        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([starting_vertex])
        print(f"target_rooms: {target_rooms}\nstarting_room: {starting_vertex}")
        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH in the queue
            current_path = neighbors_to_visit.dequeue()
            # print(f"current_path: {current_path}")
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if its the target
                if current_vertex in target_rooms:
                    # print(f"current: {current_vertex}\ntarget_rooms: {target_rooms}\npath from bfs_all: {current_path}")
                    return current_path
                    # Return the path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # print(f"testing what neighbors are seen: ",self.get_neighbors(current_vertex))
                # make new versions of the current path, with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    if next_vertex not in visited_vertices:
                        # duplicate the path
                        new_path = list(current_path)
                        # add the neighbor
                        new_path.append(next_vertex)
                        # add the new path to the queue
                        neighbors_to_visit.enqueue(new_path)
           
            