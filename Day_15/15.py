def copy2d(liste):
    r_l = []
    for value in liste:
        l = []
        for val in value:
            l.append(val)
        r_l.append(l)
    return r_l

def ta(t1, t2):
    assert len(t1)==len(t2)
    return [t1[i]+t2[i] for i in range(len(t1))]

def tm(lb, t1):
    return [lb*t1[i] for i in range(len(t1))]

def wall_behind(pos_from, pos_to, boxes, walls):
    vector = (pos_to[0]-pos_from[0], pos_to[1]-pos_from[1])
    n_pos = ta(pos_to, vector)
    if (n_pos[0], n_pos[1]) in walls:
        return True
    elif n_pos in boxes:
        return wall_behind(pos_to, n_pos, boxes, walls)
    return False

def push_boxes(pos_from, pos_to, boxes):
    vector = (pos_to[0]-pos_from[0], pos_to[1]-pos_from[1])
    n_pos = ta(pos_to, vector)
    if n_pos in boxes:
        push_boxes(pos_to, n_pos, boxes)
    for index, box in enumerate(boxes):
        if box == pos_to:
            boxes[index] = n_pos


def print_warehouse(pos, boxes, walls, width, height):
    l = [[" " for j in range(2*width)] for i in range(height)]
    l[pos[0]][pos[1]] = "@"
    for box in boxes:
        l[box[0]][box[1]] = "["
        l[box[0]][box[1]+1] = "]"
    for wall in walls:
        l[wall[0]][wall[1]] = "#"
        l[wall[0]][wall[1]+1] = "#"
    for val in l:
        print("".join(val))

def stuck_behind(box_first_bracket, direction, boxes, walls):
    if direction in [(0, 1), (0, -1)]:
        d_1 = ta(box_first_bracket, tm(2,direction))
        if tuple(d_1) in walls:
            return True
        if d_1 in boxes:
            return stuck_behind(d_1, direction, boxes, walls)
        return False
    elif direction in [(1, 0), (-1, 0)]:
        d_1, d_2, d_3 = ta(box_first_bracket, direction), ta(box_first_bracket, tm(direction[0], (1, -1))), ta(box_first_bracket, tm(direction[0], (1, 1)))
        if tuple(d_1) in walls or tuple(d_2) in walls or tuple(d_3) in walls:
            return True
        if d_1 in boxes:
            return stuck_behind(d_1, direction, boxes, walls)
        if d_2 in boxes and d_3 in boxes:
            return stuck_behind(d_2, direction, boxes, walls) or stuck_behind(d_3, direction, boxes, walls)
        if d_2 in boxes:
            return stuck_behind(d_2, direction, boxes, walls)
        if d_3 in boxes:
            return stuck_behind(d_3, direction, boxes, walls)
        return False


def push_boxes2(box_first_bracket, direction, boxes):
    if direction in [(0, 1), (0, -1)]:
        d_1 = ta(box_first_bracket, tm(2,direction))
        if d_1 in boxes:
            push_boxes2(d_1, direction, boxes)
    elif direction in [(1, 0), (-1, 0)]:
        d_1, d_2, d_3 = ta(box_first_bracket, direction), ta(box_first_bracket, tm(direction[0], (1, -1))), ta(box_first_bracket, tm(direction[0], (1, 1)))
        if d_1 in boxes:
            push_boxes2(d_1, direction, boxes)
        if d_2 in boxes:
            push_boxes2(d_2, direction, boxes)
        if d_3 in boxes:
            push_boxes2(d_3, direction, boxes)
        
    for index, box in enumerate(boxes):
        if box == box_first_bracket:
            boxes[index] = ta(box_first_bracket, direction)
    

with open("input.txt", "r") as file:
    second_star = bool(int(input("First star (1) or Second star (2) : "))-1)
    big_liste = file.read().split("\n\n")
    caracters = {"^":(-1,0), ">":(0,1),"<":(0,-1),"v":(1,0)}
    liste = big_liste[0].splitlines()
    og_walls = []
    og_boxes = []
    commands = big_liste[1].splitlines()
    if not second_star:
        for y in range(len(liste)):
            for x in range(len(liste[y])):
                if liste[y][x] == "#":
                    og_walls.append((y, x))
                elif liste[y][x] == "O":
                    og_boxes.append([y, x])
                elif liste[y][x] == "@":
                    og_pos = [y, x]
        boxes = copy2d(og_boxes)
        walls = og_walls
        pos = og_pos
        for i in range(len(commands)):
            command_line = commands[i]
            for command in command_line:
                new_pos = ta(caracters[command], pos)
                if new_pos in boxes:
                    if not wall_behind(pos, new_pos, boxes, walls):
                        push_boxes(pos, new_pos, boxes)
                        pos = new_pos
                elif not (new_pos[0], new_pos[1]) in walls:
                    pos = new_pos
    else:
        for y in range(len(liste)):
            for x in range(len(liste[y])):
                if liste[y][x] == "#":
                    og_walls.append((y, 2*x))
                elif liste[y][x] == "O":
                    og_boxes.append([y, 2*x])
                elif liste[y][x] == "@":
                    og_pos = [y, 2*x]
        boxes = copy2d(og_boxes)
        walls = og_walls
        pos = og_pos
        for i in range(len(commands)):
            command_line = commands[i]
            for command in command_line:
                direction = caracters[command]
                new_pos = ta(pos, direction)
                if direction == (0,1):
                    if new_pos in boxes:
                        if not stuck_behind(new_pos, direction, boxes, walls):
                            push_boxes2(new_pos, direction, boxes)
                            pos = new_pos
                    elif not tuple(new_pos) in walls:
                        pos = new_pos
                elif direction == (0, -1):
                    d_1 = ta(pos, tm(2, direction))
                    if d_1 in boxes:
                        if not stuck_behind(d_1, direction, boxes, walls):
                            push_boxes2(d_1, direction, boxes)
                            pos = new_pos
                    elif not tuple(d_1) in walls:
                        pos = new_pos
                elif direction in [(1, 0), (-1, 0)]:
                    d_1, d_2 = new_pos, ta(new_pos, (0, -1))
                    if d_1 in boxes:
                        if not stuck_behind(d_1, direction, boxes, walls):
                            push_boxes2(d_1, direction, boxes)
                            pos = new_pos
                    elif d_2 in boxes:
                        if not stuck_behind(d_2, direction, boxes, walls):
                            push_boxes2(d_2, direction, boxes)
                            pos = new_pos
                    elif not tuple(d_1) in walls and not tuple(d_2) in walls:
                        pos = new_pos
    somme = 0
    for box in boxes:
        somme += box[0]*100 + box[1]
    print(somme)