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

# Sort both lists in ascending order
list1.sort()
list2.sort()

# Calculate the cumulative difference
cumulative_difference = 0
for num1, num2 in zip(list1, list2):
    cumulative_difference += abs(num1 - num2)

# Output the results
print("Sorted List 1:", list1)
print("Sorted List 2:", list2)
print("Cumulative Difference:", cumulative_difference)
