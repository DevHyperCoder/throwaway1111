def small_large(l):
    small = l[0]
    large = l[0]

    for i in l:
        if small > i:
            small = i
        if large < i:
            large = i
    print("Smallest: ",small)
    print("Largest: ",large)

l = eval(input("Enter a list of numbers: "))
small_large(l)
