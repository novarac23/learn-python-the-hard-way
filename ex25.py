def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(stuff):
    return sorted(stuff)

def print_first_word(stuff):
    return stuff.pop(0)

def print_last_word(stuff):
    return stuff.pop(-1)


sentance = "This is an awesome sentance"

# print(break_words(sentance))
print(sort_words(sentance))
broken_sent = break_words(sentance)
print(print_first_word(broken_sent))
print(print_last_word(broken_sent))
