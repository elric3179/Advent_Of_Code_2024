mem = {}

def rec(value:str, n):
    global mem
    somme = 0
    if n==0:
        return 1
    if (value, n) in mem:
        return mem[(value,n)]
    else:
        if value == "0":
            somme += rec("1", n-1)
        elif len(value) % 2 == 0:
            somme += rec(value[:len(value)//2], n-1)
            somme += rec(str(int(value[len(value)//2:])), n-1)
        else:
            somme += rec(str(2024*int(value)), n-1)
        mem[(value, n)] = somme
        return somme

        

with open("input.txt", "r") as file:
    liste = file.read().split()
    somme = 0
    boolean = bool(int(input("First star (1) or Second star (2) : "))-1)
    for value in liste:
        somme += rec(value, 75 if boolean else 25)
print(somme)