def operations(liste, val):
    if len(liste) == 1:
        return [liste[0]]
    else:
        element = liste[-1]
        plus = operations(liste[:-1], val)
        mul = plus.copy()
        con = mul.copy()
        l = []
        for index in range(len(plus)):
            if element + plus[index] <= val:
                l.append(plus[index] + element)
            if element * mul[index] <= val:
                l.append(mul[index] * element)
            if int(str(con[index])+str(element)) <= val:
                l.append(int(str(con[index])+str(element)))
        return l
            

with open("input.txt", "r") as file:
    liste = file.read().splitlines()
    somme = 0
    for i in range(len(liste)):
        liste[i] = liste[i].split(":")
        liste[i][1] = liste[i][1].split(" ")[1:]
        liste[i][1] = [int(liste[i][1][j]) for j in range(len(liste[i][1]))]
        liste[i][0] = int(liste[i][0])
        if liste[i][0] in operations(liste[i][1], liste[i][0]):
            somme += liste[i][0]
    print(somme)