# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    count = []
    for s in segments:
        points.append([s.start,s.end])
        #points.append(s.end)
    for i in range(len(points)):
        if points[i+1][0] > points[i][0] or points[i+1][0] < points[i][1]:
            if points[
    return points

if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *data = map(int, input().split(' '))
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
