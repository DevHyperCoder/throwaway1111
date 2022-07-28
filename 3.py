def search(l,s):
    for i in l:
        if s == i:
            print("Found element.")
            break
    else:
        print("Could not find the element")
    
l = eval(input("Enter a list with numbers: "))
search_term = int(input("Enter search element: "))
search(l,search_term)
