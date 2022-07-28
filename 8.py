def print_A():
    with open("story.txt") as f:
        for l in f:
            if l[0] == "A":
                print(l)
print_A()
