from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from {} to {}".format(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, "w")
out_file.write(indata)

print("we're all done")

in_file.close()
out_file.close()
