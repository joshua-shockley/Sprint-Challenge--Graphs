
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

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # this should be the room id in our case here and should be a dict
        # LOOK AT NEXT LINE TO FIX ONE ISSUE
        # this should not be a preset list... should be added from get_exits()
        self.vertices[vertex_id] = {}

    def init_R_edges(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1][v2] = '?'

    def add_edge(self, v1, v2, v3):
        """
        Add a directed edge to the graph.

        v1 = the current_room/room
        v2 = the direction in get_exits()
        v3 = is what room is in dir v2
        """

        if v1 in self.vertices and v3 in self.vertices:
            self.vertices[v1][v2] = v3
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def get_room_Q(self, vertex_id):
        the_Qs = []
        for key, value in self.vertices[vertex_id].items():
            if value == '?':
                # print(f"this one has a ? {key, value}")
                the_Qs.append(key)
        if len(the_Qs) == 0:
            return None
        else:
            return the_Qs
