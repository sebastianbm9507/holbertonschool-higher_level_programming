#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # going throug list ✅#
    for names in dir(hidden_4):
        if names[0] != '_':
            print("{}".format(names))
