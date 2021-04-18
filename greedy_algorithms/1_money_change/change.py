# Uses python3
import sys

def get_change(m):
    #write your code here
    count=0
    if m/10>1:
        count+=int(m/10)
        m -= int(m/10)*10
    if m/5>1:
        count+=int(m/5)
        m -= int(m/5)*5
    count+=m
    return count

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = input()
    print(get_change(int(m)))
