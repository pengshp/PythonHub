#!/usr/bin/env python3

def foib(n):
    a,b=0,1
    while a<n:
        a,b=b,a+b
        print(a)

if __name__=='__main__':
    print(foib(100))

