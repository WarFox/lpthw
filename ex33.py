# Exercise 33: While Loops
def print_numbers(n, step):
    i = 0
    numbers = []

    for i in range (0, n, step):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now:", numbers
        print "At the bottom i is %d", i

    print "The numbers: "

    for num in numbers:
        print num

print_numbers(6, 2)
print_numbers(2, 1)
