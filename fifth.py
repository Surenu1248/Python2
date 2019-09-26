# 5.Write a code to read  the data from  input file called input.txt and count the number of characters per line,
#  number of words per line and write these into output file called as output.txt

with open("sample.txt") as my_file:
    f = open("fourth_output.txt", "w")
    words = 0
    chars = 0
    no_of_lines = 0
    for ln in my_file:
        total_words = ln.split()
        no_of_lines = no_of_lines + 1
        words = words + len(total_words)

        s1 = "Words count at line ", no_of_lines, "is : ", words
        f.write(str(s1) + '\n')
        chars += sum(len(word) for word in total_words)
        s2 = "Characters count at line ", no_of_lines, "is : ", chars
        f.write(str(s2) + '\n')

    print("Lines are: ", no_of_lines)

f.close()
