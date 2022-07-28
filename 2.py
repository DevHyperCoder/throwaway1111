def count_chars(s):
    count_vow = 0
    count_upper = 0
    count_lower = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count_vow += 1
        if ch.islower():
            count_lower +=1
        if ch.isupper():
            count_upper +=1

    print("No. of uppercase characters: ", count_upper)
    print("No. of lowercase characters: ", count_lower)
    print("No. of vowels: ", count_vow)

s = input("Enter a string: ")
count_chars(s)
