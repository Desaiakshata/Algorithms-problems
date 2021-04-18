# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    a=0
    
    weight_val = list(map(lambda v,w: v/w ,values,weights))
    # write your code here
    
    while a>=0:
        print("val:",value)
        max = weight_val[0]
        ind = 0
        for i in range(len(weight_val)):
            if weight_val[i]>max:
                max=weight_val[i]
                ind = i
        print("ind and max",ind,max,weight_val)
        a = capacity - weights[ind]
        if(a>0):
            value += max*weights[ind]
            capacity = a
        elif(a==0): 
            value += values[ind]
            return value
        else:
            value += max*capacity
            return value
        weight_val[ind] = 0
    return value


if __name__ == "__main__":
    data = list(map(int, input().split(' '))) #sys.stdin.read()
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    print(values,weights,n,capacity)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
