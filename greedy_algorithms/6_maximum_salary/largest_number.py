#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while len(a)!=0:
        maxa = a[0]
        for x in a:
            if int(str(x)+str(maxa))>int(str(maxa)+str(x)):
                maxa = x
        res += str(maxa)
        a.remove(str(maxa))
    return res

if __name__ == '__main__':
    #input = sys.stdin.read()
    data = input().split(' ')
    a = data[1:]
    print(largest_number(a))
    
