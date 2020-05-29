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
map_file = "maps/test_loop_fork.txt"
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
starting_room = current_R.id
# this creates the graph with neighbors (key being direction) with the neighboring rooms (as the value )
for each in world.rooms:
    g.addV(each)


print(f"printing room_graph ", room_graph)
for item in room_graph:
    for key, values in room_graph[item][1].items():
        g.addEdge(item, values)
print(f"my graph: {g.vertices}")
print(f"copy of g.vertices: {g.verts}")
keep_G = True
#this is about where the while loop should be to look to see if all rooms show up in path
#to then be adapted outside of this to directions to be saved to the traversal_path.
total_path=[]
all = set()
def any_left(all, keep_G):#this takes the rooms keeping what hasn't been seen yet
    new_list =[]
    for each in g.vertices.keys():
        if each not in all:
            new_list.append(each)
    print(f"any_left fn made above loop: {new_list}")
    if len(new_list) > 0:
        return new_list
    else:
        print(f"print out that nothing in the list for what's left")
        return False
        

while True:
    vertices = g.vertices
    verts = g.verts
    dft_path = g.dft(starting_room, all)
    print(f"depth path taken: {dft_path}")
    #do dft down one hallway to the end
    #should only have one way to go at the end of hallway
    #len(options)==1 at that point
    print(f"any left: ",any_left(all, keep_G))

    if dft_path != None:
        for each in dft_path:
            total_path.append(each)
            if each not in all:
                all.add(each)
        print(f"added after dft is not None: {all}")
        bfs_path = g.bfs(dft_path)
        print(f"breadth seach to spot with 3 or more options: {bfs_path}")
    elif dft_path == None:
        print(f"something went wrong or needs a condition ========>")
    if bfs_path !=None:
        for each in bfs_path:
            total_path.append(each)
            if each not in all:
                all.add(each)
        print(f"added after bfs is not None: {all}")        
        current = bfs_path[-1]
        possible = g.get_neighbors(current)
        print(f"current room before pick: {current}\npossible: {possible}")
        new_possible = [each for each in possible if each not in all]
        print(f"new_possible: {new_possible}")
        print(f"total_path so far: {total_path}")
        print(f"any left: ",any_left(all, keep_G))
        what_left = any_left(all, keep_G)
        if what_left == False:
            break
        elif len(new_possible) == 0 and len(what_left) > 0:
            #do the bfs version looking for target room in the list
            #then assign the path taken to get there to total_path
            #then assign the last in that path which has options to starting room
            #to kick off the traversals again
            print(f"total_path before adding get_more: {total_path}")
            get_more = g.bfs_all(current, what_left)
            print(f"the get more to find what's left: {get_more}")
            if get_more != None:
                for each in get_more:
                    total_path.append(each)
                    if each not in all:
                        all.add(each)
                break #here it starts to repeat and build instead of just passing the last
            # starting_room = total_path[-1]

        # elif len(new_possible)>0:        
            # possible = new_possible
            # next_room = random.choice(possible)
            # print(f"the next option chosen: {next_room}")
            # starting_room = current
    starting_room = total_path[-1]
    #then need to bfs to point where there are options that we havent just done
    #maybe this needs to take or look at what is in the path already
    #and look for spot that first comes up that has options that we didnt use yet

    #then before picking new direction add that path to the total_path to be converted to traversal_path

print(f"after running function.. total_path: {total_path}")
# for each in range(0,len(total_path)-1):
#     if total_path[each] == total_path[each+1]:
#         total_path.remove(total_path[each])
# print(f"slimmed down list: {total_path}")


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
