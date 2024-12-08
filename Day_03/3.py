somme = 0
import re
#Full flemme 1st star
with open("input_3.txt", "r") as file:
    temp_string = file.read()
    condition_dict = {}
    string = temp_string
    s_index = 0
    while True:
        # r"mul\((/d{1:3}),(/d{1:3})\)|do\(\)|"
        do_match = re.search(r"do\(\)", string)
        dont_match = re.search(r"don't\(\)", string)
        mul_match = re.search(r"mul\(\d+,\d+\)", string)
        if do_match != None and dont_match != None and mul_match != None:
            if do_match.start() < dont_match.start() and do_match.start() < mul_match.start():
                condition_dict[do_match.start()+s_index] = True
                string = string[do_match.end():]
                s_index += do_match.end()
            elif dont_match.start() < mul_match.start() and dont_match.start() < do_match.start():
                condition_dict[dont_match.start()+s_index] = False
                string = string[dont_match.end():]
                s_index += dont_match.end()
            else:
                n_str = str(mul_match)
                n_str = n_str.split("(")[2].split(")")[0].split(",")
                condition_dict[mul_match.start()+s_index] = int(n_str[0]) * int(n_str[1])
                string = string[mul_match.end():]
                s_index += mul_match.end()
        elif do_match == None and dont_match != None and mul_match != None:
            if dont_match.start() < mul_match.start():
                condition_dict[dont_match.start()+s_index] = False
                string = string[dont_match.end():]
                s_index += dont_match.end()
            else:
                n_str = str(mul_match)
                n_str = n_str.split("(")[2]
                n_str = n_str.split(")")[0].split(",")
                condition_dict[mul_match.start()+s_index] = int(n_str[0]) * int(n_str[1])
                string = string[mul_match.end():]
                s_index += mul_match.end()
        elif mul_match != None:
            n_str = str(mul_match)
            n_str = n_str.split("(")[2]
            n_str = n_str.split(")")[0]
            n_str = n_str.split(",")
            condition_dict[mul_match.start()+s_index] = int(n_str[0]) * int(n_str[1])
            string = string[mul_match.end():]
            s_index += mul_match.end()
        else:
            break

somme = 0
condition = True
for key, value in condition_dict.items():
    if type(value) == bool:
        condition = value
    else:
        if condition:
            somme += value
print(somme)