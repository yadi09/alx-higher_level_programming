#!/usr/bin/python3
from sys import argv
count = -1
for i in argv:
    count += 1
    continue
if count == 0:
    print("0 argument.")
else:
    print("{} argument:".format(count))
    for i in range(1, (count + 1)):
        print("{:d}: {}".format(i, argv[i]))
