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
map_file = "maps/test_line.txt"  # this one passes currently
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


def get_opposite(dir):
    directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    return directions[dir]


def get_dir(cur_room, dir_list):
    if len(dir_list) == 1:
        dir = dir_list[-1]
        print(f"only one direction to go from here, {dir}")
        return dir
    elif len(dir_list) > 1:
        dirs = dir_list.copy()
        print(f"the list {dirs}")
        print(f"the current room {cur_room}")
        print(
            f"visited: {visited}, g.vertices[current_room]: {g.vertices[player.current_room.id]}")
        for dir in g.vertices[cur_room].keys():
            print(dir)
            room = player.current_room.get_room_in_direction(dir)
            if room.id in visited:
                print("yuppppppppers", room.id, dir)
                dirs.remove(dir)
                print(f"length of dirs {len(dirs)}")
        if len(dirs) == 1:
            dir = dirs[-1]
            return dir
        print(f"after removing what's been visited")

       # return dir


# using dft(depth)/use stack for main traversal
# then bft(breadth)/ use queue to find next "neighbor" with ? as direction value
# maybe need to switch to adding to visited for current and previous for 2 way edges
# put that shit ino the graph and use dft
g = Graph()
# find what neighbors are available by random number pick and have a fail safe conditional setup
starting_vertex = current_R.id
plan_to_visit = Stack()  # for dft
p_to_v = Queue()  # for bft
plan_to_visit.push(starting_vertex)
print(f"before the while loop for dft: {g.vertices}")
visited = []  # will store ({room})
# start the DFT part
while plan_to_visit.size() > 0:
    print(''*3)
    # will need to do a bft part for when current is in visited and check for routes == '?'
    c_room = plan_to_visit.pop()
    if c_room not in visited:
        visited.append((c_room))
        # we here now let's add to visited already
        g.add_vertex(c_room)

        # now need to do the things before checking for neighbors
        print(
            f"c_room: {c_room}, player.current_room.id {player.current_room.id}")
        the_next = player.current_room.get_exits()
        print(f"printing the_next: ", the_next)
        for nxt_dir in the_next:
            next = player.current_room.get_room_in_direction(nxt_dir)
            print(f"printing next: {next.id}")
            g.add_vertex(next.id)
            g.add_edge(c_room, nxt_dir, next.id)
            print(f"the g.vertices: ", g.vertices)
            dir = get_dir(player.current_room.id, the_next)
            if dir != None and next.id not in visited:
                plan_to_visit.push(next.id)
                player.travel(dir)

            if dir == None:
                print("what the frick")
                print(f"at the dir of None: ", g.vertices)
                # continue
            print(f"the dir picked: {dir}")

            print("time to switch")

        print(f"looking at what is in visited, {visited}")

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
