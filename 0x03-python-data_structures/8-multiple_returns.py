#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        return len(sentence), sentence[0]
    else:
        sentence[0].append(None)
        return len(sentence), sentence[0]
