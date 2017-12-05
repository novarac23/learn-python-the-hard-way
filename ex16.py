from sys import argv

script, filename = argv

print("reading the file...")
target = open(filename, 'w')

print("say hello to myu little friend")
target.truncate()

print("now writing stuff")
target.write("line1")
target.write("line2")
target.write("line3")

print("and now we are closing it")
target.close()
