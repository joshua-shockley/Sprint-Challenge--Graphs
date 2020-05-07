from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from graph import Graph
from util import Queue, Stack
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"  # this one passes currently
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# THIS IS MY CODE BELOW.... WATCH IT DO WHAT IT DO BABY!
# start out with grabing the starting location
current_R = player.current_room


def get_opposite(dir):
    directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    return directions[dir]


def get_dir(cur_room, dir_list):
    print(f"what exists in the vertices?  {g.vertices}")
    if len(dir_list) == 1:
        dir = dir_list[-1]
        # print(f"only one direction to go from here, {dir}")
        return dir
    elif len(dir_list) > 1:
        dirs = dir_list.copy()
        print(f"the list {dirs}")
        print(f"the current room {cur_room}")
        print(
            f"visited: {visited}, g.vertices[current_room]: {g.vertices[player.current_room.id]}")
        for dir in g.vertices[cur_room].keys():
            print(f"for dir in vertices current room keys: ", dir)
            room = player.current_room.get_room_in_direction(dir)
            if room.id in visited:
                # print(
                #     "yuppppppppers it's in there all right... let's remove it", room.id, dir)
                dirs.remove(dir)
        # print(f"length of dirs {len(dirs)}")
        index = random.randint(0, len(dirs)-1)
        dir = dirs[index]
        print(
            f"after removing what's been visited and picking random leftover: {dir}")
        return dir
    # else:
    #     return None


def init_g_dirs(c_room, list):
    for direction in list:
        g.init_R_edges(c_room, direction)
    # print(f"in init_g_dirs : {g.vertices}")


# using dft(depth)/use stack for main traversal
# then bft(breadth)/ use queue to find next "neighbor" with ? as direction value
# maybe need to switch to adding to visited for current and previous for 2 way edges
# put that shit ino the graph and use dft
g = Graph()
# find what neighbors are available by random number pick and have a fail safe conditional setup
starting_vertex = current_R.id
plan_to_visit = Stack()  # for dft
plan_to_visit.push(starting_vertex)
g.add_vertex(starting_vertex)
print(f"before the while loop for dft: {g.vertices}")
visited = []  # will store ({room})
previous = ['', '']
next = []
# start the DFT part
while plan_to_visit.size() > 0:
    print(''*3)
    # will need to do a bft part for when current is in visited and check for routes == '?'
    c_room = plan_to_visit.pop()
    # should skip the first move will need to reassign again to none for bft
    if len(visited) >= 1:
        previous[0] = visited[-1]
        print(f"assigned to previous room id, {previous[0]} current: {c_room}")
    # should stop the loop when the visited list matches the length of the maze_room's length

    if c_room not in visited:  # do if the room from the stack now the current room is not in the visited list
        # g.add_vertex(c_room)
        visited.append((c_room))
        pos_exits = player.current_room.get_exits()
        print(f"possible exits: {pos_exits}")
        init_g_dirs(c_room, pos_exits)
        print(
            f"now lets look at graph after adding all possible edges and before assigning a dir to go in: {g.vertices}")
        dir = get_dir(player.current_room.id, player.current_room.get_exits())
        print(f"printing the dir when current room not in visited {dir}")
        print(g.vertices)
        next_room = player.current_room.get_room_in_direction(dir)
        next = next_room.id
        if next not in g.vertices:
            g.add_vertex(next)
            g.add_edge(c_room, dir, next)

        if previous[0] != '' and previous[1] != '':
            print(
                f"printing previous near top to see what's going on {previous} \n c_room: {c_room}")
            g.add_edge(previous[0], previous[1], c_room)
            g.add_edge(c_room, get_opposite(previous[1]), previous[0])
        print(f"the next room based on the decision: {next_room.id}")
        print(f"visited just befor moving to next: {visited}")
        if len(visited) == len(room_graph):
            print("visited length matches room-graph length")
            print(
                f"current room is: {player.current_room.id}, next is {next}, dir is {dir} \n previous is {previous}")
        if next not in visited:
            previous[0] = c_room
            previous[1] = dir
            g.add_edge(c_room, dir, next)
            traversal_path.append(dir)
            plan_to_visit.push(next)
            player.travel(dir)
        print(
            f"previous room: {previous[0]}, previous dir: {previous[1]}, c_room: {c_room}, current dir: {dir}")
        print(f"before going into bft part: {g.vertices}")
        print(
            f"current room {player.current_room.id} aka c_room now in visited {visited}")
        for spot in g.vertices:
            print(g.vertices[spot])
            if len(g.vertices[spot]) > 2:
                print(spot)
                get_to = spot
        # this is the bfs
        visited_vertices = set()
        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([player.current_room.id])
        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH in the queue
            current_path = neighbors_to_visit.dequeue()
            print(f"current_path: {current_path}")
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if its the target
                if current_vertex == get_to:
                    after_Q = current_path
                    print(f"after_Q", after_Q)
                    print(
                        f"current_certex: {current_vertex}, player.current_room.id: {player.current_room.id}")
                    print(f"traversal_path,: {traversal_path}")
                    next_dir_list = player.current_room.get_exits()
                    next_dir = get_dir(current_vertex, next_dir_list)
                    previous[0] = current_vertex
                    previous[1] = next_dir
                    room = player.current_room.get_room_in_direction(next_dir)
                    next_room = room.id
                    g.add_vertex(next_room)
                    # g.add_edge(current_vertex, next_dir, next_room)
                    traversal_path.append(next_dir)
                    plan_to_visit.push(next_room)
                    player.travel(next_dir)

                    print(f"printing next_dir: {next_dir}")

                    # break
                    # this is where i add current index into stack
                    # this is also most likely where i need to make this a fn above
                    # so that i can return and
                # mark it as visited
                else:
                    visited_vertices.add(current_vertex)
                    print(f"visited_vertices: {visited_vertices}")
                    the_n = g.get_neighbors(current_vertex)
                    print(the_n)
                    if len(the_n) <= 2:
                        for key, value in the_n.items():
                            print(value)
                            if value not in visited_vertices:
                                print(f"value: ", value)
                                new_path = list(current_path)
                                new_path.append(value)
                                traversal_path.append(key)
                                player.travel(key)
                                neighbors_to_visit.enqueue(new_path)
    if c_room in visited:
        print(f"after everything at if current_room in visited...{visited}")
        print(f"graph: {g.vertices}, current_room: {player.current_room.id}")


####

# NOW BACK TO PREVIOUSLY WRITTEN CODE (NOT MINE BELOW)... ITS THE TEST TRAVERSAL

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)

# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
