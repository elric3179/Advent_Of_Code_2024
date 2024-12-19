def in_bounds(liste, pos):
    return len(liste) > pos[0] and pos[0] >= 0 and len(liste[0]) > pos[1] and pos[1] >= 0

def get_area(liste, position, found_positions:list):
    y, x = position
    value = liste[y][x]
    if (y, x) not in found_positions:
        found_positions.append((y, x))
    new = found_positions.copy()
    for y2, x2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if not (y+y2, x+x2) in new and in_bounds(liste, (y+y2, x+x2)) and value == liste[y+y2][x+x2]:
            new.append((y+y2, x+x2))
            for pos in get_area(liste, (y+y2, x+x2), new):
                if pos not in new:
                    new.append(pos)
    return new

def get_perimeter(position_liste):
    t_sum = 0
    for pos in position_liste:
        somme = 4
        y, x = pos
        for y2, x2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (y+y2, x+x2) in position_liste:
                somme -= 1
        t_sum += somme
    return t_sum


with open("input.txt", "r") as file:
    liste = file.read().splitlines()
    for i in range(len(liste)):
        liste[i] = [j for j in liste[i]]
    positions = []
    somme = 0
    for y in range(len(liste)):
        for x in range(len(liste[y])):
            if not (y, x) in positions:
                region_pos = get_area(liste, (y, x), [])
                print(liste[region_pos[0][0]][region_pos[0][1]], len(region_pos), get_perimeter(region_pos))
                somme += len(region_pos) * get_perimeter(region_pos)
                positions += region_pos
    print(somme)