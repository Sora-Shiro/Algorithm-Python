'''
The labyrinth has no walls, but bushes surround the path on each side.
If a players move into a bush, they lose.
The labyrinth is presented as a matrix (a list of lists): 1 is a bush and 0 is part of the path.
The labyrinth's size is 12 x 12 and the outer cells are also bushes. Players start at cell (1,1).
The exit is at cell (10,10). You need to find a route through the labyrinth.
Players can move in only four directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]),
West (left [0, -1]). The route is described as a string consisting of different characters: "S"=South,
"N"=North, "E"=East, and "W"=West.
Input: A labyrinth map as a list of lists with 1 and 0.
Output: The route as a string that contains "W", "E", "N" and "S".
Precondition: Outer cells are pits.
len(labyrinth) == 12
all(len(row) == 12 for row in labyrinth)
'''
#Your code here
#You can import some modules or create additional functions

ori_right = ['N', 'W', 'S', 'E']
ori_left = ['N', 'E', 'S', 'W']

def turn_right(ori):
    return ori_right[ori_right.index(ori) - 1]

def turn_left(ori):
    return ori_left[ori_left.index(ori) - 1]

def front_watch(maze_map, ori, px, py):
    if ori == 'N':
        px -= 1
    if ori == 'E':
        py += 1
    if ori == 'S':
        px += 1
    if ori == 'W':
        py -= 1
    return maze_map[px][py]

def real_walk(ori, px, py):
    if ori == 'N':
        px -= 1
    if ori == 'E':
        py += 1
    if ori == 'S':
        px += 1
    if ori == 'W':
        py -= 1
    return px, py

def left_watch(maze_map, ori, px, py):
    ori = turn_left(ori)
    return front_watch(maze_map, ori, px, py)

def right_watch(maze_map, ori, px, py):
    ori = turn_right(ori)
    return front_watch(maze_map, ori, px, py)

def walk(maze_map, ori, px, py, result):
    if left_watch(maze_map, ori, px, py) == 0:
        ori = turn_left(ori)
    if front_watch(maze_map, ori, px, py) == 0:
        result += ori
        px, py = real_walk(ori, px, py)
        return [result, ori, px, py]
    else:
        ori = turn_right(ori)
        return walk(maze_map, ori, px, py, result)

def checkio(maze_map):
    orientation = 'E'
    position = [1, 1]
    result = ''
    while 1:
        result, orientation, position[0], position[1] = walk(maze_map, orientation, position[0], position[1], result)
        if position[0] == 10 and position[1] == 10:
            break
    return result


# def checkio(maze_map):
#     def canwalk(come, px, py):
#         out = ''
#         if maze_map[px-1][py] == 0:
#             out += 'N'
#         if maze_map[px][py+1] == 0:
#             out += 'E'
#         if maze_map[px+1][py] == 0:
#             out += 'S'
#         if maze_map[px][py-1] == 0:
#             out += 'W'
#         if come == 'N':
#             come = 'S'
#         elif come == 'S':
#             come = 'N'
#         elif come == 'W':
#             come = 'E'
#         elif come == 'E':
#             come = 'W'
#         out = out.replace(come, '')
#         return out
#     def walk(orientation, px, py):
#         if orientation == 'N':
#             px -= 1
#         if orientation == 'E':
#             py += 1
#         if orientation == 'S':
#             px += 1
#         if orientation == 'W':
#             py -= 1
#         return [px, py]
#     def load(save_p, save_choose, save_result):
#         position = save_p[-1]
#         del save_p[-1]
#         choose = save_choose[-1]
#         del save_choose[-1]
#         result = save_result[-1]
#         del save_result[-1]
#         return [position, choose, result]
#     def save(position, choose, result, save_p, save_choose, save_result):
#         save_p.append(position)
#         save_choose.append(choose)
#         save_result.append(result)
#     position = [1, 1]
#     choose = canwalk('', position[0], position[1])
#     result = ''
#     save_p = []
#     save_choose = []
#     save_result = []
#     while 1:
#         if len(choose) == 0:
#             if len(save_p) > 0:
#                 position, choose, result = load(save_p, save_choose, save_result)
#                 continue
#         orientation = choose[0]
#         if len(choose) > 1:
#             if position in save_p:
#                 if position == save_p[-1]:
#                     del save_p[-1]
#                     del save_choose[-1]
#                     del save_result[-1]
#                 position, choose, result = load(save_p, save_choose, save_result)
#                 continue
#             save(position, choose.replace(orientation, ''), result, save_p, save_choose, save_result)
#         position = walk(orientation, position[0], position[1])
#         result += orientation
#         if position[0] == 10 and position[1] == 10:
#             return result
#         choose = canwalk(orientation, position[0], position[1])


if __name__ == '__main__':
    #This code using only for self-checking and not necessary for auto-testing
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        #copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False

    # These assert are using only for self-testing as examples.
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
    print("The local tests are done.")
