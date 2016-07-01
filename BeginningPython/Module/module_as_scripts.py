# coding=utf-8

print "__name__:", __name__


def fib(n):
    a, b = 0, 1
    result = []
    print "in fib():", __name__
    while b < n:
        result.append(b)
        a, b = b, a+b
    print result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
