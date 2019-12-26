#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in(dir(hidden_4)):
        out = "__"
        if out not in i:
            print("{}".format(i))
