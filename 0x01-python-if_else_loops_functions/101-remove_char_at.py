#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    for i in range(len(str)):
        if i is n:
            continue
        else:
            new_str.append(str[i])
    return (''.join(new_str))
