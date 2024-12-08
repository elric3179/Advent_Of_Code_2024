frequencies = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def distance(t1, t2):
    return (t2[0]-t1[0], t2[1]-t1[1])

def in_bounds(liste, pos):
    return len(liste) > pos[0] and pos[0] >= 0 and len(liste[0]) > pos[1] and pos[1] >= 0

with open("input.txt", "r") as file:
    second_star = bool(int(input("First star (1) or Second star (2) : "))-1)
    liste = file.read().splitlines()
    for i in range(len(liste)):
        liste[i] = [liste[i][j] for j in range(len(liste[i]))]
    antinodes = []
    for character in frequencies:
        pos = []
        for y in range(len(liste)):
            for x in range(len(liste[0])):
                if liste[y][x] == character:
                    pos.append((y, x))
        for index1 in range(len(pos)):
            for index2 in range(index1+1, len(pos)):
                dist = distance(pos[index1], pos[index2])
                k_1, k_2 = 1, 1
                if second_star:
                    k_1, k_2 = 0, 0
                    pos_1 = (pos[index1][0] - k_1 * dist[0], pos[index1][1] - k_1 * dist[1])
                    pos_2 = (pos[index2][0] + k_2 * dist[0], pos[index2][1] + k_2 * dist[1])
                    while in_bounds(liste, pos_1):
                        if not pos_1 in antinodes:
                            antinodes.append(pos_1)
                        k_1 += 1
                        pos_1 = (pos[index1][0] - k_1 * dist[0], pos[index1][1] - k_1 * dist[1])
                    while in_bounds(liste, pos_2):
                        if not pos_2 in antinodes:
                            antinodes.append(pos_2)
                        k_2 += 1
                        pos_2 = (pos[index2][0] + k_2 * dist[0], pos[index2][1] + k_2 * dist[1])
                else:
                    pos_1 = (pos[index1][0] - k_1 * dist[0], pos[index1][1] - k_1 * dist[1])
                    pos_2 = (pos[index2][0] + k_2 * dist[0], pos[index2][1] + k_2 * dist[1])
                    if in_bounds(liste, pos_1) and not pos_1 in antinodes:
                        antinodes.append(pos_1)
                    if in_bounds(liste, pos_2) and not pos_2 in antinodes:
                        antinodes.append(pos_2)

print(len(antinodes))