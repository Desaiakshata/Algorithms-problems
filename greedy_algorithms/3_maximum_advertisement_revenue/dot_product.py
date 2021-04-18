#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    while a:
        ind = 0
        ind_ = 0
        maxa = a[0]
        maxb = b[0]
        print(a,b)
        for i in range(len(a)):
            if a[i]>maxa:
                maxa = a[i]
                ind = i
            if b[i]>maxb:
                maxb = b[i]
                ind_ = i
        res+=maxa*maxb
        a.remove(a[ind])
        b.remove(b[ind_])
        
    return res

if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split(' ')))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
