import re

part_1, part_2 = 0, 0
enable = True

with open('input.txt') as f:
    for line in f:
        sides = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line.strip())
        for side in sides:
            if 'do()' == side:
                enable = True
            elif 'don\'t()' == side:
                enable = False
            else:
                a, b = map(int, re.findall(r'\d+', side))
                if enable:
                    part_2 += a * b

                part_1 += a * b


print(part_1, part_2)