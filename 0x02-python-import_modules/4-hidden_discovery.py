#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = [name for name in dir(hidden_4) if "__" not in name]
    for i in range(len(list)):
        print(list[i])
