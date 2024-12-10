def is_sorted(liste):
    l = len(liste) -1
    for i in range(len(liste)-1):
        if liste[l - i - 1] == -1 and liste[l - i] != -1:
            return False        
    return True

def get_last(liste, i_2):
    for i in range(i_2):
        if liste[len(liste)-1-i] != -1:
            return len(liste)-1-i

def get_first1(liste, i_1):
    for i in range(i_1, len(liste)):
        if liste[i] == -1:
            return i
    return len(liste)

def swap(liste, i_1, i_2):
    temp = liste[i_2]
    liste[i_2] = liste[i_1]
    liste[i_1] = temp 

def check_sum(liste):
    somme = 0
    for index, value in enumerate(liste):
        if value != -1:
            somme += index*value
    return somme

def find_first(liste, length):
    for i in range(len(liste)):
        if liste[i][0] == -1 and liste[i][1] >= length:
            return i

def find_last_value(liste, last_value):
    for i in range(len(liste)):
        if liste[i][0] == last_value:
            return i

with open("input.txt", "r") as file:
    string = file.read()
    liste = [string[i] for i in range(len(string))]
    condition = 0
    string = []
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    for i in range(len(liste)):
        if condition % 2 == 0:
            if boolean:
                string.append([condition//2, int(liste[i])])
            else:
                for j in range(int(liste[i])):
                    string.append(condition//2)

        else:
            if boolean:
                string.append([-1, int(liste[i])])
            else:
                for j in range(int(liste[i])):
                    string.append(-1)
        condition += 1

    liste = string

    if not boolean:
        condition = True
        i_1 = 0
        i_2 = len(liste)
        while condition:
            i_1 = get_first1(liste, i_1)
            i_2 = get_last(liste, i_2)
            if i_1 < i_2:   
                swap(liste, i_1, i_2)
            else:
                condition = False
    else:
        last_value = condition//2
        while last_value >= 0:
            last_index = find_last_value(liste, last_value)
            first_index = find_first(liste, liste[last_index][1])
            if first_index == None:
                last_value -= 1
                continue
            if first_index < last_index:
                if liste[first_index][1] == liste[last_index][1]:
                    temp = liste[first_index]
                    liste[first_index] = liste[last_index]
                    liste[last_index] = temp
                else:
                    temp = liste[last_index]
                    liste[last_index] = [-1, temp[1]]
                    liste[first_index] = [-1, liste[first_index][1]-temp[1]]
                    liste.insert(first_index, [last_value, temp[1]])
            last_value -= 1
        new_liste = []
        for index, value in enumerate(liste):
            for j in range(value[1]):
                new_liste.append(value[0])
        liste = new_liste.copy()
    print(check_sum(liste))