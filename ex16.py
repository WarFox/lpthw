# Exercise 16: Reading and Writing Files
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

# No need to invoke truncate() in "w" mode
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

content = """
%s
%s
%s
""" % (line1, line2, line3)

target.write(content)

print "And finally, we close it."
target.close()
