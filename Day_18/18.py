import queue
def ta(t1, t2):
    return [t1[i]+t2[i] for i in range(len(t1))]

def calculate_shortest_path(start, end, positions):
    Queue = queue.PriorityQueue()
    Queue.put((0, start))
    seen = []
    while not Queue.empty():
        current = Queue.get()
        if current[1] == end:
            return current[0]
        for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = ta(current[1], (y, x))
            if new_pos in positions and new_pos not in seen:
                seen.append(new_pos)
                Queue.put((current[0]+1, new_pos))

def print_place(positions, n):
    liste = [["." if [y, x] in positions else "#" for x in range(n)] for y in range(n)]
    for val in liste:
        print("".join(val))

with open("input.txt", "r") as file:
    liste = file.read().splitlines()
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    a = 1024
    b = len(liste)
    if not boolean:
        positions = [[index, index1] for index in range(71) for index1 in range(71)]
        for i in range(a):
            y, x = liste[i].split(",")
            y = int(y)
            x = int(x)
            positions.remove([x, y])
        print(calculate_shortest_path([0,0],[70,70],positions))
    else:
        while b-a > 1:
            positions = [[index, index1] for index in range(71) for index1 in range(71)]
            m = (a+b)//2
            for i in range(m):
                y, x = liste[i].split(",")
                y = int(y)
                x = int(x)
                positions.remove([x, y])
            if calculate_shortest_path([0,0], [70,70], positions) == None:
                b = m
            else:
                a = m
        print(liste[a].split(",")[0]+","+liste[a].split(",")[1])