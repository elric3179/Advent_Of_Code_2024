somme = 0

def check(liste:list[list[str]], t1, t2, t3, t4):
    if liste[t1[0]][t1[1]] == "X" and liste[t2[0]][t2[1]]=="M" and liste[t3[0]][t3[1]]=="A" and liste[t4[0]][t4[1]] == "S":
        return True
    return False

def for_bac(liste:list[list[str]]):
    global somme
    for i in range(len(liste)):
        for j in range(len(liste[0])-3):
            if check(liste, (i, j), (i, j+1), (i, j+2), (i, j+3)):
                somme += 1
            if check(liste, (i, len(liste[0])-1-j), (i, len(liste[0])-2-j), (i, len(liste[0])-3-j), (i, len(liste[0])-4-j)):
                somme += 1

def up_down(liste:list[list[str]]):
    global somme
    for i in range(len(liste[0])):
        for j in range(len(liste)-3):
            if check(liste, (j, i), (j+1, i), (j+2, i), (j+3, i)):
                somme += 1
            if check(liste, (len(liste[0])-1-j, i), (len(liste[0])-2-j, i), (len(liste[0])-3-j, i), (len(liste[0])-4-j, i)):
                somme += 1
def one_dia(liste:list[list[str]]):
    global somme
    for i in range(len(liste)-3):
        for j in range(len(liste[0])-3):
            if check(liste, (i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3)):
                somme += 1
            if check(liste, (i+3, j+3), (i+2, j+2), (i+1, j+1), (i, j)):
                somme += 1
            
def two_dia(liste:list[list[str]]):
    global somme
    for i in range(len(liste)-3):
        for j in range(len(liste[0])-3):
            if check(liste, (i+3, j), (i+2, j+1), (i+1, j+2), (i, j+3)):
                somme += 1
            if check(liste, (i, j+3), (i+1, j+2), (i+2, j+1), (i+3, j)):
                somme += 1
                
def check_x(liste, t1, t2, t3, t4, t5):
    if liste[t3[0]][t3[1]] != "A":
        return False
    if liste[t1[0]][t1[1]] == liste[t5[0]][t5[1]]:
        return False
    if liste[t2[0]][t2[1]] == liste[t4[0]][t4[1]]:
        return False
    if liste[t3[0]][t3[1]] != "X" and liste[t1[0]][t1[1]] != "X" and liste[t2[0]][t2[1]] != "X" and liste[t5[0]][t5[1]] != "X" and liste[t4[0]][t4[1]] != "X" and liste[t2[0]][t2[1]] != "A" and liste[t1[0]][t1[1]] != "A" and liste[t4[0]][t4[1]] != "A" and liste[t5[0]][t5[1]] != "A":
        return True

def pattern(liste):
    global somme
    for i in range(len(liste)-2):
        for j in range(len(liste)-2):
            if check_x(liste, (i, j), (i+2, j), (i+1, j+1), (i, j+2), (i+2, j+2)):
                somme += 1
with open("input_4.txt", "r") as file:
    liste = file.read().split("\n")
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    if (boolean):
        pattern(liste)
    else:
        for_bac(liste)
        up_down(liste)
        one_dia(liste)
        two_dia(liste)
    print(somme)