
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
        self.visited = []

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
        return list(self.vertices[vertex_id].keys()
                    )

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

    # def bfs_to_another_hallway(self, visited, currentV, Qpath, old_path, plan_to_visit):
    #     q = Queue()
    #     q.enqueue([currentV])
    #     # visited is being used from
    #     # adding to path needs to be the 'next_room'
    #     # adding current on the way back adds
    #     # the ending of the hallway 2x's

    #     while q.size() > 0:
    #         current_path = q.dequeue()
    #         current_room = current_path[-1]
    #         any = self.get_room_Q(current_room)
    #         print(
    #             f"any from bfs at current_room: {current_room}, exits: {any}")
    #         if any == None:
    #             print('means no room is unused at this loc')
    #             # add directions and save a path then return it
    #             visited.add(current_room)
    #             next_rooms = self.get_neighbors(current_room)
    #             for dir in next_rooms:
    #                 print(f"direction avail: {dir}")
    #                 print(
    #                     f"next room would be: {self.vertices[current_room][dir]}")
    #                 if self.vertices[current_room][dir] != '?' and self.vertices[current_room][dir] not in visited:
    #                     Qpath.append(self.vertices[current_room][dir])
    #                     new_path = Qpath.copy()
    #                     q.enqueue(new_path)
    #         else:
    #             print(f"found a room {current_room} with exits{any}")
    #     print(f"current_path outside bfs: {old_path}")
    #     print(f"path: {Qpath}")
