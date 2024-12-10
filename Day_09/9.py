def is_sorted(liste):
    l = len(liste) -1
    for i in range(len(liste)-1):
        if liste[l - i - 1] == -1 and liste[l - i] != -1:
            print(l-i-1)
            return False        
    return True

def get_last(liste, i_2):
    for i in range(i_2):
        if liste[len(liste)-1-i] != -1:
            return len(liste)-1-i

def get_first(liste, length):
    for i in range(len(liste)-length):
        if [liste[i+j] for j in range(length)] == [-1]*length:
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
    for i in range(len(liste)):
        if condition % 2 == 0:
            string.append([condition//2,int(liste[i])])
        else:
            string.append([-1,int(liste[i])])
        condition += 1
    last_value = condition//2
    liste = string
    condition = True
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
print(check_sum(new_liste))