
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n

l = ["Rupa", "Rahul", "Farhan", "an"]

print(rem(l, "an"))
