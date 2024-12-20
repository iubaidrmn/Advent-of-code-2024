import re

# for debugging
def display_grid():
    for i in range(MAX_DIM + 1):
        for j in range(MAX_DIM + 1):
            if (j, i) in corrupt:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')

# MAX_DIM = 6
MAX_DIM = 70

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

# BYTES_IN = 12
BYTES_IN = 1024

corrupt = set()
for L in lines[:BYTES_IN]:
    x, y = re.findall(r'\d+', L)
    corrupt.add((int(x), int(y)))

# Dijkstra's algorithm to find shortest path
start = (0, 0)
end = (MAX_DIM, MAX_DIM)
nodes_to_process = {}
nodes_to_process[start] = 0
completed_nodes = set()
while nodes_to_process:
    current_node = min(nodes_to_process, key=nodes_to_process.get)
    x = current_node[0]
    y = current_node[1]
    cost = nodes_to_process[current_node]

    if x-1 >= 0 and (x-1, y) not in corrupt \
        and (x-1, y) not in completed_nodes \
            and (x-1, y) not in nodes_to_process:
        nodes_to_process[(x-1, y)] = cost + 1
    if x+1 <= MAX_DIM and (x+1, y) not in corrupt \
        and (x+1, y) not in completed_nodes \
            and (x+1, y) not in nodes_to_process:
        nodes_to_process[(x+1, y)] = cost + 1
    if y-1 >= 0 and (x, y-1) not in corrupt \
        and (x, y-1) not in completed_nodes \
            and (x, y-1) not in nodes_to_process:
        nodes_to_process[(x, y-1)] = cost + 1
    if y+1 <= MAX_DIM and (x, y+1) not in corrupt \
        and (x, y+1) not in completed_nodes \
            and (x, y+1) not in nodes_to_process:
        nodes_to_process[(x, y+1)] = cost + 1

    if end in nodes_to_process:
        break
    completed_nodes.add((x,y))
    del nodes_to_process[(x, y)]

print(nodes_to_process[end])
    