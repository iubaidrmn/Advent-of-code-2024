from collections import Counter

# Read input from file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Initialize two separate lists
list1 = []
list2 = []

# Populate lists from file
for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

# Count occurrences of each number in list2
count_list2 = Counter(list2)

# Calculate the similarity score
similarity_score = 0
for num in list1:
    if num in count_list2:
        similarity_score += num * count_list2[num]

# Output the results
print("Similarity Score:", similarity_score)
