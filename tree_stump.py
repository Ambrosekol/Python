print("Tree Printer")

tree_height = int(input("Enter height of tree: "))
linespace = tree_height - 1
leaf = 1
stump = linespace
while tree_height != 0:
    print(" " * linespace, end="")
    print("#" * leaf)
    linespace -= 1
    leaf += 2
    tree_height -= 1
print(" " * (stump - 1), end="")
print("###")
    