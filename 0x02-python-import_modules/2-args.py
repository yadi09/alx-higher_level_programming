#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
count = len(argv)
count -= 1
if count == 0:
    print("0 argument.")
else:
    print("{} argument:".format(count))
    for i in range(1, (count + 1)):
        print("{:d}: {}".format(i, argv[i]))
