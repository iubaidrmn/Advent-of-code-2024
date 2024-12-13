import functools
from collections import defaultdict

with open('input.txt') as f:
    stones = [int(num) for num in f.read().split()]

stone_counts = {num:stones.count(num) for num in set(stones)}

@functools.lru_cache
def blink_one(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    length = len(stone_str)
    if length%2==0:
        return [int(stone_str[:length//2]),int(stone_str[length//2:])]
    else:
        return [2024*stone]

def blink_all(stone_counts):
    new_counts = defaultdict(lambda:0)
    for stone,count in stone_counts.items():
        for new_stone in blink_one(stone):
            new_counts[new_stone] += count
    return new_counts

for _ in range(75):
    stone_counts = blink_all(stone_counts)

answer = sum(num for num in stone_counts.values())
print(answer)