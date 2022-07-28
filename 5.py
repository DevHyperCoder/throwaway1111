# TODO: Consonants has a bug. It counts spaces too.
def count_text(fname):
    with open(fname) as f:
        content = f.read()
        count_upper = count_lower = count_vow = count_consonants = count_space = 0

        for i in content.strip():

            if i in "aeiouAEIOU":
                count_vow +=1
            else:
                count_consonants +=1
            if i == "\n" or i == " ":
                count_space += 1
                
            if i.islower():
                count_lower +=1
            if i.isupper():
                count_upper +=1
        print("No. of uppercase characters: ",count_upper)
        print("No. of lowercase characters: ",count_lower)
        print("No. of vowels: ",count_vow)
        print("No. of consonants: ",count_consonants - count_space)

filename = input("Enter filename: ")
count_text(filename)
