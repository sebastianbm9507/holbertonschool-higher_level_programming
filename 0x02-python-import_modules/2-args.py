#!/usr/bin/python3
if __name__ == '__main__':
    import sys
# printing the number of argv 🔢 #
    args_number = len(sys.argv)
# checking 0 arguments  ✅#
    if args_number == 1:
        print("0 arguments.")
# checking 1 argument 🟢 #
    elif args_number == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
# there is more than 2 arguments 🟣 #
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
# going throug list ✅#
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
