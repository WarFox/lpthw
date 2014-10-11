# Exercise 15: Reading Files
from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r" % filename
print txt.read()

print "Type the file name again:"
file_again = raw_input('> ')

txt_again = open(filename)

print txt_again.read()
