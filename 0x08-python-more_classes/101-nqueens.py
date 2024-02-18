#!/usr/bin/python3


from sys import argv

if __name__ == "__main__":
    l = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    m = int(argv[1])
    if m < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(m):
        l.append([i, None])

    def already_exists(y):
        for x in range(m):
            if y == l[x][1]:
                return True
        return False

    def reject(x, y):
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(l[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        for i in range(x, m):
            l[i][1] = None

    def nqueens(x):
        for y in range(m):
            clear_a(x)
            if reject(x, y):
                l[x][1] = y
                if (x == m - 1):
                    print(l)
                else:
                    nqueens(x + 1)

    nqueens(0)
