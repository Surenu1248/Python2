# 3. Write a program to receive a string from keyboard and check if the string has two 'e' in the characters.
# If yes return True else False.

str1 = input("Enter the string : ")


def my_string(s):
    cnt = 0
    for i in s:
        if i == 'e':
            cnt = cnt + 1
    print(cnt)
    if cnt >= 2:
        return True
    else:
        return False


print(my_string(str1))
