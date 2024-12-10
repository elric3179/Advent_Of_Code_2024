def in_bounds(liste, pos):
    if len(liste) > pos[0] and pos[0] >= 0 and len(liste[0]) > pos[1] and pos[1] >= 0:
        return True
    return False

def check(liste, pos1, val):
    positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return_pos = []
    y = pos1[0]
    x = pos1[1]
    for i in range(len(positions)):
        y1 = positions[i][0]
        x1 = positions[i][1]
        if in_bounds(liste, (y+y1, x+x1)) and liste[y+y1][x+x1] == val + 1:
            return_pos.append((y+y1, x+x1))
    return return_pos

def find_paths1(liste, last_val, pos, val=0):
    y = pos[0]
    x = pos[1]
    return_pos = []
    if last_val == 8 and liste[y][x] == 9:
        return [pos]
    positions = check(liste, pos, val)
    for pos in positions:
        return_pos += find_paths1(liste, val, pos, liste[pos[0]][pos[1]])
    if val==0:
        return [return_pos]
    return return_pos
    
with open("input.txt", "r") as file:
    liste = file.read().splitlines()
    for i in range(len(liste)):
        liste[i] = [int(liste[i][j]) for j in range(len(liste[i]))]
    somme = []
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == 0:
                somme += find_paths1(liste, 0, (i, j))
    t_s = 0
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    for heads in somme:
        if not boolean:
            l = []
            for pos in heads:
                if not pos in l:
                    l.append(pos)
            t_s += len(l)
        else:
            t_s += len(heads)
print(t_s)