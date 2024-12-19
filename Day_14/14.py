import time, os
from PIL import Image
def robot_move(p, v, n):
    return (p[0]+n*v[0])%HEIGHT, (p[1]+n*v[1])%WIDTH

def display_robots(l_r, n, m):
    image = Image.new("RGB", (WIDTH*m, (HEIGHT)*n))
    for i in range(n):
        for j in range(m):
            l = [[0 for h in range(WIDTH)] for k in range(HEIGHT)]
            for robot in l_r:
                l[robot[0][0]][robot[0][1]] = 1
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    image.putpixel((x+j*(WIDTH), y+i*(HEIGHT)), (255,255,255) if l[y][x] == 1 else 0)
            robot_move_once(l_r)
    image.save("robots.png")

def robot_move_once(l_r):
    for index, robot in enumerate(l_r):
        l_r[index] = [((robot[0][0]+robot[1][0])%HEIGHT, (robot[0][1]+robot[1][1])%WIDTH), robot[1]]

def cut_half(l):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for i in range(HEIGHT//2):
        for j in range(WIDTH//2):
            s1 += l[i][j]
            s2 += l[HEIGHT//2+i+(HEIGHT%2)][j]
            s3 += l[i][WIDTH//2+j+(WIDTH%2)]
            s4 += l[HEIGHT//2+i+(HEIGHT%2)][WIDTH//2+j+(WIDTH%2)]
    return s1*s2*s3*s4

# with open("input.txt", "r") as file:
#     liste = file.read().splitlines()
#     WIDTH = 101
#     HEIGHT = 103
#     l_r = []
#     condition = True
#     for value in liste:
#         l1 = value.split(" ")
#         pos = l1[0].removeprefix("p=").split(",")
#         v = l1[1].removeprefix("v=").split(",")
#         pos = (int(pos[1]), int(pos[0]))
#         v = (int(v[1]), int(v[0]))
#         l_r.append([pos, v])
#     gen = 0
#     while True:
#         display_robots(l_r, 100, 100)
#         if input(f"Is this it (Gen. {gen})? Nothing for no, 1 for yes: ") != "":
#             break
#         time.sleep(0.1)
#         gen+=1
#         os.system("clear")

with open("input.txt", "r") as file:
    liste = file.read().splitlines()
    WIDTH = 101
    HEIGHT = 103
    l = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
    for value in liste:
        l1 = value.split(" ")
        pos = l1[0].removeprefix("p=").split(",")
        v = l1[1].removeprefix("v=").split(",")
        pos = (int(pos[1]), int(pos[0]))
        v = (int(v[1]), int(v[0]))
        y_f, x_f = robot_move(pos, v, 100)
        l[y_f][x_f] += 1
    print(cut_half(l))

