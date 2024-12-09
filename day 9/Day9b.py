import time

with open("input.txt", "r") as f:
    line = f.read().strip()
    
start = time.time()

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

first_dot = 0
while disk[-1] == "😊":
    disk.pop()

# get list of files without spaces
files = []
last = disk[0]
file_length = 0
for i, char in enumerate(disk):
    if char != last:
        files.append((last*file_length, i-file_length)) if last != "😊" else 0
        file_length = 1
    else:
        file_length += 1
    last = char
len_disk = len(disk)
files.append((last*file_length, len(disk)-file_length))

while len(files) > 0:
    # get length of last file
    length_last = len(files[-1][0])
    # find the first space with same or more space
    try:
        first_dot = disk.index("😊"*length_last, 0, files[-1][1])
    except:
        files.pop()
        continue
    # MOVE last file there
    disk = disk[:first_dot] + files[-1][0]+ disk[first_dot + length_last:files[-1][1]] + "😊"*length_last + disk[files[-1][1]+length_last:]

    # pop the last file from the list
    files.pop()

total = 0
for i, c in enumerate(disk):
    if c == "😊":
        continue
    total += i * ord(c)

end = time.time()
print(total)

print(f"time: {end-start}s")
