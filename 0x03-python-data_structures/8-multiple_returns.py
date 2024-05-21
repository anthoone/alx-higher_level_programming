#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    sen_first = sentence[0] if sentence else  None
    return (sen_len, sen_first)
