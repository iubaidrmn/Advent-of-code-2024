import time

start = time.time()
with open("input.txt", "r") as f:
    line = f.read().strip()

disk = ""
empty = False
i = 0
for char in line:
    if empty:
        disk += ("😊"*int(char))
    else:
        disk += (chr(i)*int(char))
        i += 1
    empty = not empty

disk = list(disk)
first_dot = 0

while True:
    while disk[-1] == "😊":
        disk.pop()
    try:
        first_dot = disk.index("😊", first_dot)
    except:
        break
    disk[first_dot] = disk[-1]
    disk.pop()

total = 0
for i, c in enumerate(disk):
    total += i * ord(c)

end = time.time()
print(total)

print(f"time: {end-start}s")
