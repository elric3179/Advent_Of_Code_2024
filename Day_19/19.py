def if_patterns(towel:str, patterns:list[str]):
    if towel in memo:
        return False
    for pattern in patterns:
        if towel == pattern:
            return True
        if len(towel) <= len(pattern):
            continue
        elif pattern == towel[:len(pattern)]:
            if if_patterns(towel[len(pattern):], patterns):
                return True
    memo.append(towel)
    return False

def n_patterns(towel:str, patterns:list[str]):
    somme = 0
    if towel == "":
        return 1
    if towel in memo:
        return memo[towel]
    for pattern in patterns:
        if towel == pattern:
            somme += 1
        if len(towel) <= len(pattern):
            continue
        elif pattern == towel[:len(pattern)]:
            somme += n_patterns(towel[len(pattern):], patterns)
    memo[towel] = somme
    return somme

second_star = bool(int(input("First star (1) or Second star (2) : "))-1)

with open("input.txt", "r") as file:
    string = file.read()
    patterns = string.split("\n\n")[0].split(", ")
    towels = string.split("\n\n")[1].splitlines()
    somme = 0
    if not second_star:
        for towel in towels:
            memo = []
            somme += 1 if if_patterns(towel, patterns) else 0
    else:
        for towel in towels:
            memo = {}
            somme += n_patterns(towel, patterns)
    print(somme)