liste = []

carac = {"^":(-1,0), ">":(0,1), "<":(0,-1), "v":(1,0)}

def turn_right(liste:list[list], pos):
    if liste[pos[0]][pos[1]] == "^":
        liste[pos[0]][pos[1]] = ">"
    if liste[pos[0]][pos[1]] == ">":
        liste[pos[0]][pos[1]] = "v"
    if liste[pos[0]][pos[1]] == "v":
        liste[pos[0]][pos[1]] = "<"
    if liste[pos[0]][pos[1]] == "<":
        liste[pos[0]][pos[1]] = "^"
    return liste

def ge(lis, pos):
    return lis[pos[0]][pos[1]]

def se(lis, pos, value):
    lis[pos[0]][pos[1]] = value

def out_of_bounds(liste, pos):
    return pos[0] >= len(liste) or pos[0] < 0 or pos[1] >= len(liste[0]) or pos[1] < 0

def copy_2d(liste):
    l = []
    for i in range(len(liste)):
        l.append([liste[i][j] for j in range(len(liste[i]))])
    return l

with open("input.txt", "r") as file:
    string = file.read()
    liste = string.splitlines()
    pos = []
    for i in range(len(liste)):
        if liste[i].count("^") != 0:
            pos = [i, liste[i].find("^")]
        if liste[i].count("<") != 0:
            pos = [i, liste[i].find("<")]
        if liste[i].count(">") != 0:
            pos = [i, liste[i].find(">")]
        if liste[i].count("v") != 0:
            pos = [i, liste[i].find("v")]
        liste[i] = [liste[i][j] for j in range(len(liste[i]))]
    original = copy_2d(liste)
    somme = 0
    original_pos = pos.copy()
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if [i, j] != original_pos:
                liste[i][j] = "#"
            condition = True
            index = 0
            while condition and index < 20000:
                try:
                    new_pos = [pos[0]+carac[ge(liste, pos)][0], pos[1]+carac[ge(liste, pos)][1]]
                except:
                    exit()

                if out_of_bounds(liste, new_pos):
                    condition = False
                    continue
                if ge(liste, new_pos) == "#":
                    if liste[pos[0]][pos[1]] == "^":
                        liste[pos[0]][pos[1]] = ">"
                    elif liste[pos[0]][pos[1]] == ">":
                        liste[pos[0]][pos[1]] = "v"
                    elif liste[pos[0]][pos[1]] == "v":
                        liste[pos[0]][pos[1]] = "<"
                    elif liste[pos[0]][pos[1]] == "<":
                        liste[pos[0]][pos[1]] = "^"
                else:
                    se(liste, new_pos, ge(liste, pos))
                    se(liste, pos, ".")
                    pos = new_pos
                index += 1
            if index >= 20000:
                somme += 1
            liste = copy_2d(original)
            pos = original_pos.copy()
            print(f"{j+len(liste[0])*i}/{len(liste)*len(liste[0])}")
print(somme)