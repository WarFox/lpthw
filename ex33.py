# Exercise 33: While Loops
def print_numbers(n):
    i = 0
    numbers = []

    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now:", numbers
        print "At the bottom i is %d", i

    print "The numbers: "

    for num in numbers:
        print num

print_numbers(6)
print_numbers(2)
