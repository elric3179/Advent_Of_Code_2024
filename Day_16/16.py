import queue, time

def tm(lamb, t_1):
    return [lamb*t_1[i] for i in range(len(t_1))]

def turn_clockwise(dir):
    return (dir[1], -dir[0])

def turn_ccw(dir):
    return (-dir[1], dir[0])

def ta(t_1, t_2):
    return [t_1[i]+t_2[i] for i in range(len(t_1))]

def dir_value(direction1, direction2):
    if direction1==direction2:
        return 0
    return 1000

def move_through(start, end, direction, graph):
    come_from = {tuple(start): []}
    cost = {tuple(start): 0}
    Queue = queue.SimpleQueue()
    Queue.put((start, direction))
    
    while not Queue.empty():
        current = Queue.get()
        pos = current[0]
        dir = current[1]
        for new_pos in graph[tuple(pos)]:
            new_dir = (new_pos[0]-pos[0], new_pos[1]-pos[1])
            new_cost = 1 + dir_value(new_dir, dir) + cost[tuple(pos)]
            if tuple(new_pos) not in cost or new_cost < cost[tuple(new_pos)]:
                cost[tuple(new_pos)] = new_cost
                come_from[tuple(new_pos)] = [tuple(pos)]
                Queue.put((new_pos, new_dir))

            elif new_cost == cost[tuple(new_pos)]:
                if tuple(pos) not in come_from[tuple(new_pos)]:
                    come_from[tuple(new_pos)].append(tuple(pos))

    return come_from, cost

memo = {}

def search_path(start, direction, value, end, goal, graph):
    liste = [start]
    if start == end and value == goal:
        return liste
    if tuple(start) in memo and memo[tuple(start)] < value:
        return None
    if value >= goal:
        return None
    condition = False
    for new_pos in graph[tuple(start)]:
        y, x = (new_pos[0]-start[0], new_pos[1]-start[1])
        if y!=-direction[0] or x!=-direction[1]:
            new_cost = 1+dir_value(direction, (y, x))+value
            res = search_path(new_pos, (y, x), new_cost, end, goal, graph)
            if res != None:
                liste = liste + res
                condition = True
    if condition:
        return liste
    else:
        memo[tuple(start)] = value

with open("input.txt", "r") as file:
    liste = file.read().splitlines()
    walls = []
    positions = []
    for index in range(len(liste)):
        for index1 in range(len(liste[index])):
            if liste[index][index1] == "#":
                walls.append([index, index1])
            else:
                positions.append([index, index1])
            if liste[index][index1] == "E":
                end = [index, index1]
            if liste[index][index1] == "S":
                start = [index, index1]
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    graph:dict[tuple:list] = {}
    for position in positions:
        graph[tuple(position)] = []
        for y, x in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if ta(position, (y, x)) in positions:
                graph[tuple(position)].append(ta(position, (y, x)))
    come_from, cost = (move_through(start, end, (0, 1), positions))
    if not boolean:
        print(cost[tuple(end)])
    else:
        l = search_path(start, (0, 1), 0, end, cost[tuple(end)], graph)
        l = [tuple(v) for v in l]
        print(len(set(l)))