# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n==2:
        return [2]
    for i in range(n):
        summands.append(i+1)
        if n-i-1<=summands[-1]:
            rem = n-i-1+summands[-1]
            summands.pop()
            summands.append(rem)
            return summands
        n-=i+1
    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
