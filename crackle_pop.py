#!/usr/bin/env python3

"""
Recurse Center Instructions:

"Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle
instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. You can
use any language."

This program can be run with Python 2 or Python 3. Depending on your environment setup, the program can be run with one
(or both) of the following commands:

$ python2 crackle_pop.py
$ python3 crackle_pop.py

Alyse Dunn
alyse.dunn@gmail.com
February 2021
"""

def main():
    for i in range(1, 101):
        if i % 3 == 0:
            if not i % 5 == 0:
                print("Crackle")
            else:
                print("CracklePop")

        elif i % 5 == 0:
            print("Pop")

        else:
            print(i)


if __name__ == '__main__':
    main()
