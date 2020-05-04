# def get_rand_dir():
#     list = player.current_room.get_exits()
#     print(list)
#     d_index = random.randint(0, len(list)-1)
#     print("in get_rand_dir() picks random number in range from 0-(len-1 of list of exits):\n ",
#           directions[d_index])
#     return d_index


# def init_edge(c_room):
#     print('in init_edge up top   \n')
#     dir = player.current_room.get_exits()
#     print('dir in init_edge:  ', dir)
#     g.add_init_edge(c_room, dir)
#     print(" init_edge ran for current_room: ", g.vertices[c_room])


# def get_good_dir(c_room):
#     # print('in get_good_dir(), the current room id: ', c_room)
#     possible_d = player.current_room.get_exits()
#     print('possible_d:', possible_d)
#     print(len(possible_d))
#     if len(possible_d) > 1:  # WHEN THE LENGTH OF THE LIST OF POSSIBLE DIRECTIONS IS MORE THAN 1
#         dir = get_rand_dir()
#         print('current room vertices: ', g.vertices[c_room])
#         print('in the if when list of directions is more than 1/index[0]', dir)
#         next = player.current_room.get_room_in_direction(possible_d[dir])
#         print('in get_good_dir: ', next.id, possible_d[dir])
#         if next.id not in visited:
#             print('we not been there yet')
#             dir = possible_d[dir]
#         if next.id in visited:
#             print('been here lets see if way we can go')
#             secondary_dir = []
#             been = []
#             for sdir in possible_d:
#                 if sdir not in visited[next.id]:
#                     # this appends all directions not taken before
#                     secondary_dir.append(sdir)
#                     print("other options to move in next room:", secondary_dir)
#                     if len(secondary_dir) > 1:
#                         print('oh, shit!')
#                     elif len(secondary_dir) == 1:

#                         return secondary_dir[0]
#                     else:
#                         print(
#                             'made it to the else in  get_good_dir with list 0 after pickout out the ? from copied over')
#                         return None
#                 else:
#                     print(f"the only direction is: {sdir}")
#                     been.append(sdir)
#                     print('been: ', been)
#                     return None

#             print(
#                 'secondary_dir  after running through looking for non assigned directions', secondary_dir)
#     else:  # WHEN THE LIST IS ONLY ONE DIRECTION.. NO CHECKS YET AT THIS POINT
#         dir = possible_d[0]
#         print('in the else', dir)
#         if c_room in visited:
#             print(visited[c_room])
#             return None

#         print(dir)
#         return dir

#     print("just before return in get_good_dir():", dir)
#     return dir


# def make_opposite_dir(dir):
#     if dir == 'n':
#         s = 's'
#         return s
#     elif dir == 's':
#         n = 'n'
#         return n
#     elif dir == 'e':
#         w = 'w'
#         return w
#     elif dir == 'w':
#         e = 'e'
#         return e
