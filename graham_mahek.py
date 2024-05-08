import math
import matplotlib.pyplot as plt


def cross_product(o,a,b):
    
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def polar_angle(base,p):
    return math.atan2(p[1]-base[1],p[0]-base[0])
    
def graham_scan(points):
    hull = []
    start = min(points, key = lambda p: (p[1],p[0]))
    sort_arr = sorted(points,key = lambda p:(polar_angle(start,p),p[0],p[1]))
    
    for point in sort_arr:
        while len(hull)>=2 and cross_product(hull[-2],hull[-1],point)<=0:
            hull.pop()
        hull.append(point)
    return hull

points = [(0,0),(1,1),(2,2),(3,3),(4,4),(0,3),(1,3),(1,2),(3,1)]

convex = graham_scan(points)
print(convex)
x,y = zip(*points)
hx,hy = zip(*convex)
plt.scatter(x,y)
plt.plot(hx+(hx[0],),hy+(hy[0],))
plt.legend()
plt.show()