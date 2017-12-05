from sys import argv

script, filename = argv

txt = open(filename)

print("here is your {}".format(filename))
print(txt.read())
