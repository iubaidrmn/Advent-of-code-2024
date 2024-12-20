with open('input.txt') as f:
    grid = f.read().splitlines()

start = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='S']
assert len(start)==1
start = start[0]
end = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='E']
assert len(end)==1
end = end[0]

track = {start:0}
cur = start
curstep = 0
while cur != end:
    curstep += 1
    i,j = cur
    for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
        newi,newj = i+di,j+dj
        if (newi,newj) not in track and grid[newi][newj] in 'SE.':
            cur = (newi,newj)
            track[cur] = curstep
            break

count = 0
for i,j in track:
    for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
        if (i+di,j+dj) not in track and (i+2*di,j+2*dj) in track and track[(i+2*di,j+2*dj)]-track[(i,j)]>=102:
            count += 1
print(count)