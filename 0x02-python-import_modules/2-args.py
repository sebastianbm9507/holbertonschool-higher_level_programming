#!/usr/bin/python3
if __name__ == '__main__':
    import sys
# printing the number of argv 🔢 #
    args_number = len(sys.argv) - 1
# checking 0 arguments  ✅#
    if args_number == 1:
        print("{:d} argument.".format(len(sys.argv) - 1))
# checking 1 argument 🟢 #
    elif args_number == 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
# there is more than 2 arguments 🟣 #
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
# going throug list ✅#
    for i in range(len(sys.argv)):
        if i == 0:
            continue;
        print("{:d}: {:s}".format(i, sys.argv[i]))
