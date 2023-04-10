#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    with open('ind1.txt', 'r') as ind:
        ind = ind.readlines()
    ind = [i.split() for i in ind]
    x = [[int(i) for i in j] for j in ind]
    for i in x:
        for j in i:
            if 9 < j < 100:
                print(*i)
                break
