import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#             break

# Solution 1
# 0.74
# for name_1 in names_1:
#     if(name_1 in names_2):
#         duplicates.append(name_1)

# Solution 2
# 0.004
sett = set()
for name_2 in names_2:
    sett.add(name_2)

for name_1 in names_1:
    if(name_1 in sett):
        duplicates.append(name_1)

# Solution 3
# 0.10
# bst = BinarySearchTree(names_2[0])
# for name_2 in names_2:
#     bst.insert(name_2)

# for name_1 in names_1:
#     if(bst.contains(name_1)):
#         duplicates.append(name_1)


# 64

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
