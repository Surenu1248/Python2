# 4. What is the output of following code:

counter = 1


def dolots(count):
    global counter
    for i in (1, 2, 3):
        counter = count + i


print(dolots(4))
print(counter)

# -----------The above code will gives the following output----------

# None
# 7
