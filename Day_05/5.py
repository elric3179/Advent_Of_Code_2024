with open("input_5.txt", "r") as file:
    string = file.read()
    l_1 = string.split("\n\n")[0]
    l_2 = string.split("\n\n")[1]
    l_1 = l_1.split("\n")
    l_2 = l_2.split("\n")
    dic = {}
    for i in range(len(l_1)):
        l_1[i] = [int(l_1[i].split("|")[0]), int(l_1[i].split("|")[1])]
    dic = {}
    for i in range(len(l_1)):
        if l_1[i][1] in dic:
            dic[l_1[i][1]].append(l_1[i][0])
        else:
            dic[l_1[i][1]] = [l_1[i][0]]
    somme = 0
    boolean = bool(int(input("First star (1) of Second star (2) : "))-1)
    for i in range(len(l_2)):
        liste = [int(j) for j in l_2[i].split(",")]
        already_seen = []
        condition = True
        for keyvalue in liste:
            if keyvalue in dic:
                for value in dic[keyvalue]:
                    if value not in already_seen and value in liste:
                        condition = False
                        break
            if not condition:
                break
            already_seen.append(keyvalue)
        if not boolean:
            if condition:
                somme += liste[len(liste)//2]
        else:
            if not condition:
                liste_sort = []
                for value in liste:
                    condition2 = True
                    index = len(liste_sort)
                    if value in dic:
                        while condition2:
                            for i in range(index):
                                if liste_sort[i] in dic[value]:
                                    break
                            else:
                                liste_sort.insert(index, value)
                                condition2 = False
                            index -= 1
                    else:
                        liste_sort.insert(index, value)
                somme += liste_sort[len(liste_sort)//2]
print(somme)