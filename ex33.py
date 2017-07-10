def count(end, by):
    numbers = []
    for i in range(0, end, by):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % (i + by)

    print "The numbers: "

    for num in numbers:
        print num

count(6,2)
