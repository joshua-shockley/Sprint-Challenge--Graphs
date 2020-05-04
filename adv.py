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

# pick a number between 0-3 for picking directional movement
directions = ['n', 's', 'w', 'e']
# below picks a random number to pic a random direction

# inputing a list for it to check across and pick a random direction
# there is not check here for whether it


def make_opposite_dir(dir):
    if dir == 'n':
        s = 's'
        return s
    elif dir == 's':
        n = 'n'
        return n
    elif dir == 'e':
        w = 'w'
        return w
    elif dir == 'w':
        e = 'e'
        return e


def get_good_dir(c_room):
    out = ''
    exit_list = player.current_room.get_exits()
    print(f"prints the exit list for curent room: ", exit_list)
    if len(exit_list) == 1:
        next = player.current_room.get_room_in_direction(exit_list[-1])
        if next.id not in visited:
            out = exit_list[-1]
            return out
        else:
            print(
                'should be at end of line... this is where the bft goes to find room with exits to use')
            out = None
            return out
    if len(exit_list) == 2:
        index = random.randint(0, len(exit_list)-1)
        print(
            f"length of exit_list: {len(exit_list)}\n index picked at random: {index}")
        print(exit_list[index])
        out = exit_list[index]
        next = player.current_room.get_room_in_direction(out)
        print(f"visited at this point: ", visited)
        print(f" {next.id} is the next room to look at")
        if next.id in visited:
            exit_list.remove(out)
            print(
                f"new exit_list after removing what's in visited: {exit_list}")
            out = exit_list[-1]
            return out
    if len(exit_list) >= 3:
        print('there are more in here')
        index = random.randint(0, len(exit_list)-1)
        print(
            f"length of exit_list: {len(exit_list)}\n index picked at random: {index}")
        print(exit_list[index])
        out = exit_list[index]

    return out


# using dft(depth)/use stack for main traversal
# then bft(breadth)/ use queue to find next "neighbor" with ? as direction value
# put that shit ino the graph and use dft
g = Graph()
g.add_vertex(current_R.id)
# find what neighbors are available by random number pick and have a fail safe conditional setup
starting_vertex = current_R.id
plan_to_visit = Stack()
plan_to_visit.push(starting_vertex)
print(f"the vertices: {g.vertices[starting_vertex]}")
visited = {}
# start the DFT part
while plan_to_visit.size() > 0:
    print(''*3)
    current_room = plan_to_visit.pop()
    # will need to do a bft part for when current is in visited and check for routes == '?'
    if current_room not in visited:

        print(f"current room: {current_room}")
        # now lets find a direct to move in
        rand_dir = get_good_dir(current_room)
        print(
            f"found a random direction based of what's available in list: {rand_dir}")
        if rand_dir != None:
            next = player.current_room.get_room_in_direction(rand_dir)
            print(f"next one is: {next.id}")
            # below adds the direction we took at each step
            traversal_path.append(rand_dir)
            # visited.add((current_room))
            # changed to dict
            visited[current_room] = {rand_dir: next.id}

            g.add_vertex(next.id)

            print('vertices after adding the next one', g.vertices)
            print(
                f"current_room: {current_room}, rand_dir: {rand_dir}, next.id: {next.id}")
            g.add_edge(current_room, rand_dir, next.id,
                       make_opposite_dir(rand_dir))
            # AT EACH STEP SHOULD ALSO ADD THE CURRENT ROOM'S PREIOUS ROOM DIR
            # AS WELL AS THE NEXT SO IT MARKS WHERE IT CAME FROM

            # the current location added to the visited list above
            print(f"print visited list: {visited}")
            print(g.vertices)
            if next.id not in visited:
                print(f"{next.id} not in {visited}")
                # now we add to the stack the next id in the direction randomly picked
                plan_to_visit.push(next.id)
                # now we actually travel
                player.travel(rand_dir)
            elif next.id in visited:
                print(f"it's in the visited list already")
        if rand_dir == None:
            print("rand_dir == None")
    print(player.current_room.id)
    # this is where i put the bft part now until find a room with an exit that isnt used yet
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
