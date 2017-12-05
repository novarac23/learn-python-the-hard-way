ten_things = "Applles Oranges Crows Telephone Light Sugar"

print("Wait ther are not 10 things")

stuff = ten_things.split(' ')
more_stuff = ["one", "two", "three", "four"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)

print(stuff)

print(stuff[1])
print(stuff[-1])


print(stuff[3:5])
