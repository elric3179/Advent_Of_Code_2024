somme = 0

def is_increasing(liste:list):
    for i in range(len(liste)-1):
        if liste[i] >= liste[i+1] or (liste[i+1]-liste[i] > 3 or liste[i+1]-liste[i] < 1):
            return False
    return True

def is_decreasing(liste:list):
    for i in range(len(liste)-1):
        if liste[i] <= liste[i+1] or (liste[i]-liste[i+1] > 3 or liste[i]-liste[i+1] < 1):
            return False
    return True

def is_sorted(liste:list):
    return is_increasing(liste) or is_decreasing(liste)

with open("input.txt", "r") as file:
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    string = ""
    string = file.read()
    l = string.split("\n")
    l = l[:-1]
    for i in range(1000):
        l[i] = l[i].split(" ")
        for j in range(len(l[i])):
            l[i][j] = int(l[i][j])
        if not is_sorted(l[i]):
            condition = False
            if boolean:
                for j in range(len(l[i])):
                    temp = l[i].copy()
                    temp.pop(j)
                    if is_sorted(temp):
                        condition = True
            if condition == False:
                continue
            
        somme += 1
print(somme)