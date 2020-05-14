from room import Room
from player import Player
from world import World

import random
from random import choice
from ast import literal_eval
# from graph import Graph
from util import Queue, Stack, Graph
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"  # this one passes currently
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"
#
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
# start by adding the vertexes from the list of rooms in world.rooms.value
# that way all ther vertices are already existing and we don't have to worry about making that as we go
# make dft that creates the edges as it goes.. dont use a visited in the main dft....
# when looking for what room to do next at a junction point look for what has a value == '?'
# start out with grabing the starting location
g = Graph()
current_R = player.current_room
print(f"starting_room: {current_R.id}")
starting_room = current_R.id
# this creates the graph with neighbors (key being direction) with the neighboring rooms (as the value )
for each in world.rooms:
    g.add_vertex(each)
    for exit in world.rooms[each].get_exits():
        g.vertices[each][exit] = '?'
# print(g.vertices)
# this looks at entire graph and looks for values with "?"


def get_opposite(dir):
    direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    return direction[dir]


def pick_room(list):
    if len(list) >= 1:
        dir = random.choice(list)
        return dir
    else:
        return None


def find_all_Qs():
    qs = {}
    for each in g.vertices:
        # print(f"room: ", each)
        if g.get_room_Q(each) != None:
            qs[each] = g.get_room_Q(each)
    if len(qs) == 0:
        return None
    return qs


the_q_list = find_all_Qs()
# print(f"the_q_list: {the_q_list}, len(the_q_list): {len(the_q_list)}")
# g.get_room_Q(g.vertices[player.current_room.id])
# will get you either None if empty or a list of
# the directions for that room with value == '?'


def bfs_to_another_hallway(visited, currentV, Qpath, old_path, plan_to_visit, pathDirs):
    q = Queue()
    q.enqueue([currentV])
    # visited is being used from
    # adding to path needs to be the 'next_room'
    # adding current on the way back adds
    # the ending of the hallway 2x's
    q_list = find_all_Qs()

    together_now = ''
    while q.size() > 0 and len(q_list) > 0:
        q_list = find_all_Qs()
        # print(f"list of the dirs with '?' {q_list}")
        current_path = q.dequeue()
        current_room = current_path[-1]
        any = g.get_room_Q(current_room)
        # print(
        #     f"any from bfs at current_room: {current_room}, exits: {any}")
        if any == None:
            # print('means no room is unused at this loc')
            # add directions and save a path then return it
            visited.add(current_room)
            next_rooms = g.get_neighbors(current_room)
            for dir in next_rooms:
                # print(f"direction avail: {dir}")
                # print(
                #     f"next room would be: {g.vertices[current_room][dir]}")
                if g.vertices[current_room][dir] != '?' and g.vertices[current_room][dir] not in visited:
                    Qpath.append(g.vertices[current_room][dir])
                    new_path = Qpath.copy()
                    pathDirs.append(dir)
                    # hopefully this puts the dir in the right spot... we'll see
                    traversal_path.append(dir)
                    q.enqueue(new_path)
                    player.travel(dir)
        else:
            # print(f"found a room {current_room} with exits{any}")
            # print(f"current_path outside bfs: {old_path}")
            # print(f"path: {Qpath}")
            # print(f"player current location: {player.current_room.id}")
            # now need to push current room to stack to continue the
            together_now = old_path + Qpath
            # print(
            #     f"together_now-putting traversal path together: {together_now}")
    return together_now


def get_to_all_room():
    starting_room = current_R.id
    plan_to_visit = Stack()
    plan_to_visit.push([starting_room])
    # mainly for the breadth first back to find next crosspoint with unused exits
    Qpath = []
    # try to use this to collect the dirs along the way of traversal, at the point of traversal
    pathDirs = []
    visited = set()
    # now start the loop for the dft whileloop

    been_to = False
    # maybe need to add condition to look for all room to have no '?'
    while plan_to_visit.size() > 0 and been_to == False:
        current_path = plan_to_visit.pop()
        current = current_path[-1]
        # print(
        #     f"at top of while loop, current room: {current}, current path: {current_path}")
        # current_dir_list = g.get_room_Q(current)
        current_dir_list = g.get_neighbors(current)
        if current_dir_list == None:
            # this means that the current room has no other directions to choose from not already seen
            # print(
            #     f"current room has no unused directions\nAlso may be the end of a hallway\n current room: {current}")
            # print(f"{current_path}")

            path = bfs_to_another_hallway(
                visited, current, Qpath, current_path, plan_to_visit, pathDirs)
            plan_to_visit.push(path)
            # at end of hallway this is where we bfs back to

            # head back to find room with unexplored exits
        # current_N = g.get_neighbors(current)
        # print(f"current_dir_list: {current_dir_list}\ncurrent_N: {current_N}")
        next_dir = pick_room(current_dir_list)
        if next_dir == None:
            return f"its at the end of this line {current_path},  current loc: {current}"
        # print(f"next_dir: ", next_dir)
        next_room = player.current_room.get_room_in_direction(next_dir)
        next_room = next_room.id
        # print(f"next_room: {next_room}")
        g.add_edge(current, next_dir, next_room)
        g.add_edge(next_room, get_opposite(next_dir), current)
        # print(g.vertices)
        # now we travel down the hallway
        current_path.append(next_room)
        copy_path = current_path.copy()
        pathDirs.append(next_dir)
        # adding to the traversal_path
        traversal_path.append(next_dir)
        # print(f"copy_path: {copy_path}, pathDirs: {pathDirs}")
        the_q_list = find_all_Qs()
        if the_q_list == None:
            been_to = True
        # print(f"the_q_list: {the_q_list}")
        player.travel(next_dir)
        plan_to_visit.push(copy_path)


get_to_all_room()
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
