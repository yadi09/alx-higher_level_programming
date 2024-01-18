#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv as ag

if (not len(ag) == 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

i = ag[2]

if i == '+':
    print("{} + {} = {}".format(ag[1], ag[3], add(int(ag[1]), int(ag[3]))))
    exit(0)
elif i == '-':
    print("{} - {} = {}".format(ag[1], ag[3], sub(int(ag[1]), int(ag[3]))))
    exit(0)
elif i == '*':
    print("{} * {} = {}".format(ag[1], ag[3], mul(int(ag[1]), int(ag[3]))))
    exit(0)
elif i == '/':
    print("{} / {} = {}".format(ag[1], ag[3], div(int(ag[1]), int(ag[3]))))
    exit(0)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
