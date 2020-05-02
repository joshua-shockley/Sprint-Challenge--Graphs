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
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
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

# pick a number between 0-3 for picking directional movement
directions = ['n', 's', 'w', 'e']
# below picks a random number to pic a random direction


def get_rand_dir(list):
    d_index = random.randint(0, len(list)-1)
    # print("random direction pick: ", directions[d_index])
    return directions[d_index]


def get_good_dir(c_room):
    # print('in get_good_dir(), the current room id: ', c_room)
    possible_d = player.current_room.get_exits()
    print(possible_d)
    print(len(possible_d)-1)
    if len(possible_d)-1 > 0:
        dir = get_rand_dir(possible_d)
        print('in the if when list of directions is more than 1/index[0]', dir)
        next = player.current_room.get_room_in_direction(dir)
        if next.id in visited:
            print('we been there')
    else:
        dir = possible_d[0]
        print('in the else', dir)
    # print(dir)
    return dir


# using dft(depth)/use stack for main traversal
# then bft(breadth)/ use queue to find next "neighbor" with ? as direction value
# put that shit ino the graph and use dft
g = Graph()
g.add_vertex(current_R.id)
# find what neighbors are available by random number pick and have a fail safe conditional setup
starting_vertex = current_R.id
plan_to_visit = Stack()
plan_to_visit.push(starting_vertex)
print(g.vertices[starting_vertex])
visited = set()
# start the DFT part
while plan_to_visit.size() > 0:
    current_room = plan_to_visit.pop()
    if current_room not in visited:
        print(f"current room: {current_room}")
        # now lets find a direct to move in
        rand_dir = get_good_dir(current_room)
        print(
            f"found a random direction based of what's available in list: {rand_dir}")
        visited.add((current_room))
        next = player.current_room.get_room_in_direction(rand_dir)
        print(f"next one is: {next.id}")
        g.add_vertex(next.id)
        g.add_edge(current_room, rand_dir, next.id)
        # the current location added to the visited list above
        print(f"print visited list: {visited}")
        print(g.vertices)
        if next not in visited:
            plan_to_visit.push(next.id)
            player.travel(rand_dir)

    # now we add to the stack the next id in the direction randomly picked

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
