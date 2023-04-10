#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open('ind2.txt', 'r') as f:
        text = f.read()
    l_text = text.split()
    s_text = set(text.split())
    MyData = sorted(zip([l_text.count(w) for w in s_text], s_text), reverse=True)
    for txt1 in MyData:
        if (txt1[0] >= MyData[0][0]):
            t = txt1
    print(t)