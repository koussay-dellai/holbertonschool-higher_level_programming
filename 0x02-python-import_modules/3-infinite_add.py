#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) <= 1):
        print("{:d}".format(len(sys.argv) - 1))
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
                sum = sum + int(sys.argv[i])
        print("{:d}".format(sum))
