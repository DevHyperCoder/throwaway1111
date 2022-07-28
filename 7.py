def count_words():
    with open("story.txt") as f:
        contents = f.read()
        words = contents.split()

        print("No. of words in story.txt is:",len(words))

count_words()
