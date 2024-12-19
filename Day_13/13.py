import re

with open("input.txt", "r") as file:
    second_star = bool(int(input("First star (1) or Second star (2) : "))-1)
    liste = file.read().split("\n\n")
    somme = 0
    for index in range(len(liste)):
        liste[index] = liste[index].splitlines()
        match_A = re.search(r"\d+, Y\+\d+", liste[index][0])
        A_x, A_y = (re.findall("\d+", match_A.string))
        match_B = re.search(r"\d+, Y\+\d+", liste[index][1])
        B_x, B_y = (re.findall("\d+", match_B.string))
        match_goal = re.search(r"\d+, Y\=\d+", liste[index][2])
        g_x, g_y = (re.findall("\d+", match_goal.string))
        A_x = int(A_x)
        A_y = int(A_y)
        B_x = int(B_x)
        B_y = int(B_y)
        g_x = int(g_x) + (10000000000000 if second_star else 0) 
        g_y = int(g_y) + (10000000000000 if second_star else 0)
        A = (g_x*B_y-B_x*g_y)/(A_x*B_y-B_x*A_y)
        B = (g_y*A_x-A_y*g_x)/(A_x*B_y-B_x*A_y)
        if abs(int(A)-A)<0.0001 and abs(int(B)-B)<0.0001:
            somme += 3*int(A)+int(B)
print(somme)