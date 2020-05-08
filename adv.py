from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
# from graph import Graph
from util import Queue, Stack, Graph
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
# start by adding the vertexes from the list of rooms in world.rooms.value
# that way all ther vertices are already existing and we don't have to worry about making that as we go
# make dft that creates the edges as it goes.. dont use a visited in the main dft....
# when looking for what room to do next at a junction point look for what has a value == '?'
# start out with grabing the starting location
g = Graph()
current_R = player.current_room
print(f"starting_room: {current_R.id}")

# this creates the graph with neighbors (key being direction) with the neighboring rooms (as the value )
for each in world.rooms:
    g.add_vertex(each)
    for exit in world.rooms[each].get_exits():
        g.vertices[each][exit] = '?'


print(g.vertices)

# this looks at entire graph and looks for values with "?"


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
print(the_q_list)
# g.get_room_Q(g.vertices[player.current_room.id])
# will get you either None if empty or a list of
# the directions for that room with value == '?'


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
