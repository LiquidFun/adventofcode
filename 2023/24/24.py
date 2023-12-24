import numpy as np
import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, product, combinations_with_replacement
from queue import PriorityQueue

lines = open(0).read().splitlines()
Y, X = len(lines), len(lines[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_intersection(m1, c1, m2, c2):
    if m1 == m2:
        return -1, -1

    x_intersect = (c2 - c1) / (m1 - m2)
    y_intersect = m1 * x_intersect + c1

    return x_intersect, y_intersect
from z3 import *

sx = Real('x')
sy = Real('y')
sz = Real('z')
sdx = Real('dx')
sdy = Real('dy')
sdz = Real('dz')
s = Solver()

coords = []
for i, line in enumerate(lines[:3]):
    x, y, z, dx, dy, dz = map(int, line.replace("@", ",").split(","))
    # coords.append((px, py, pz, vx, vy, vz))

    t = Real(f't{i}')
    s.add(sx + sdx * t == x + dx * t, t>=0)
    s.add(sy + sdy * t == y + dy * t, t>=0)
    s.add(sz + sdz * t == z + dz * t, t>=0)
print(s)
print(s.check())
ans = s.model()
print(ans)
print(ans["x"])
# print(s.x)
exit()

# Please replace the example points and direction vectors with the actual data of your specific problem

from typing import List, Tuple
def find_intersecting_lines():
    lines = coords
    intersections = []
    n = len(lines)
    print(n)

    # Helper function to solve a linear system
    def solve_linear_system(a, b, c, d, e, f, g, h, i, j, k, l):
        determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
        if determinant == 0:
            return None, None  # Lines are parallel or coincident
        t = (j * (e * i - f * h) - k * (d * i - f * g) + l * (d * h - e * g)) / determinant
        s = (-b * (j * i - l * f) + c * (j * h - l * e) - (a * (k * i - l * f) - c * (k * h - j * g)) + b * (k * h - j * g)) / determinant
        return t, s

    for lini in range(n):
        for linj in range(lini+1, n):
            # print(i, j)
            line1 = lines[lini]
            line2 = lines[linj]
            
            # Unpack line equations
            p1, d1 = line1[:3], line1[3:]
            p2, d2 = line2[:3], line2[3:]
            
            # Set up the linear equations
            a, b, c = d1
            d, e, f = -1 * d2[0], -1 * d2[1], -1 * d2[2]
            g, h, i = p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]

            # Solve for the parameters t and s
            t, s = solve_linear_system(a, b, c, d, e, f, g, h, i, a, b, c)

            if t is not None and s is not None:
                # We have an intersection
                intersection_point = (p1[0] + t * d1[0], p1[1] + t * d1[1], p1[2] + t * d1[2])
                intersections.append(intersection_point)

    return intersections

def dot_product(v1, v2):
    return sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))

def cross_product(v1, v2):
    return (v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0])

def closest_point_on_second_line(P1, d1, P2, d2):
    # P1 = np.array(P1, dtype=np.int64)
    # d1 = np.array(P1, dtype=np.int64)
    # P2 = np.array(P2, dtype=np.int64)
    # d2 = np.array(d2, dtype=np.int64)

    # Calculate the w vector
    w0 = np.subtract(P2, P1)
    
    # Create the coefficient matrix for the system of equations
    a = dot_product(d1, d1)
    b = -dot_product(d1, d2)
    c = dot_product(d2, d2)
    d = int(dot_product(d1, w0))
    e = int(-dot_product(d2, w0))
    
    # Check for case where the lines are parallel (cross product is zero)
    if cross_product(d1, d2) == (0, 0, 0):
        print("The lines are parallel or coincident, no unique closest point exists.")
        return None
    
    # Solving the linear system via matrix computation
    denom = a * c - b * b
    if denom == 0:
        print("Lines are parallel or coincident, cannot find a unique closest point.")
        return None

    t1 = (b * e - c * d) / denom
    t2 = (b * d - a * e) / denom

    closest_point_on_line_1 = np.add(P1, np.multiply(t1, d1))
    closest_point_on_line_2 = np.add(P2, np.multiply(t2, d2))

    # Calculate the distance between the closest points
    distance = np.linalg.norm(closest_point_on_line_1 - closest_point_on_line_2)
    print(closest_point_on_line_1)
    print(closest_point_on_line_2)
    print("dist", distance)
    print()
    
    return closest_point_on_line_2

def find_closest_point(XA0, XAd, XB0, XBd):
    from numpy import array, cross
    from numpy.linalg import solve, norm

    XA0 = np.array(XA0)
    XA1 = XA0 + XAd
    XB0 = np.array(XB0)
    XB1 = XB0 + XBd
    # compute unit vectors of directions of lines A and B
    UA = (XA1 - XA0) / norm(XA1 - XA0)
    UB = (XB1 - XB0) / norm(XB1 - XB0)
    # find unit direction vector for line C, which is perpendicular to lines A and B
    UC = cross(UB, UA); UC /= norm(UC)

    # solve the system derived in user2255770's answer from StackExchange: https://math.stackexchange.com/q/1993990
    RHS = XB0 - XA0
    LHS = array([UA, -UB, UC]).T
    return solve(LHS, RHS)
# prints "[ 0. -0.  1.]"

# closest_point = closest_point_on_second_line(P1, d1, P2, d2)
# print("The closest point on the second line to the first line is:", closest_point)
# exit()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

sdx = -33
sdy = -25
sdz = 32

# Define the figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Loop through each line and plot it
for x,y,z,dx,dy,dz in sorted(coords):
    # ax.quiver(x, y, z, dx, dy, dz, length=100000000000 * math.sqrt(dx**2+dy**2+dz**2), normalize=True)
    color = f"#{min(255,abs(dx)):02x}{min(255,abs(dy)):02x}{min(255,abs(dz)):02x}"
    if color in ["#9e1324", "#824b3c", "#a93b2f", "#5d2573"] or True:
        # ax.quiver(x, y, z, dx, dy, dz, length=205000000000000, normalize=True, color=color, linewidth=0.5)
        ax.quiver(x/sdx, y/sdy, z/sdz, dx/sdx, dy/sdy, dz/sdz, length=20500000000000, normalize=True, color=color, linewidth=0.5)

# azimuth:-26, elevation: 29

# sx = 373474908948239
# sy = 361357857930075
# sz = 185364402503613

# sx = 373905585564057
# sy = 361528383921964
# sz = 185128885023709

# sx2 = 373584835366359
# sy2 = 361409039061671
# sz2 = 185289314254093

# sx = 257400146806249
# sy = 272828776985511
# sz = 298676339005784

sx = 242925990361460
sy = 262097223462152
sz = 311766970071262

sx2 = 312182148063510
sy2 = 312874854707645
sz2 = 244607326974783

sdx = -(sx2 - sx)
sdy = -(sy2 - sy)
sdz = -(sz2 - sz)
print(sdx, sdy, sdz)
diff = abs(abs(sdz) - abs(sdx))
print(sdx / diff, sdy / diff, sdz / diff)

Ps = (sx, sy, sz)
Pd = (sdx, sdy, sdz)
# closest_point = closest_point_on_second_line(Ps, Pd, P2, d2)

def calculate_distance(r1, e1, r2, e2):
    # e1, e2 = Direction vector
    # r1, r2 = Point where the line passes through
    r1 = np.array(r1)
    r2 = np.array(r2)
    e1 = np.array(e1)
    e2 = np.array(e2)

    # Find the unit vector perpendicular to both lines
    n = np.cross(e1, e2).astype(np.float64)

    # Calculate distance
    d = abs(np.dot(n / np.linalg.norm(n), r1 - r2))

    # v = r1 - r2
    # t1 = np.dot(np.cross(v, e2), n) / np.dot(e1, np.cross(e2, n))
    # t2 = np.dot(np.cross(v, e1), n) / np.dot(e2, np.cross(e1, n))
    t1 = np.dot(np.cross(e2, n), (r2 - r1)) / np.dot(n, n)
    t2 = np.dot(np.cross(e1, n), (r2 - r1)) / np.dot(n, n)
    # t1 = np.cross(e2, n) * (r2 - r1) / (n* n)
    # t2 = np.cross(e1, n) * (r2 - r1) / (n* n)
    # print(t1, t2)
    p1 = r1 + t1 * e1
    p2 = r2 + t2 * e2
    # print(p1, p2)
    # print(d, np.linalg.norm(p1 - p2))
    # assert math.isclose(d, np.linalg.norm(p1 - p2))

    return d, p1, p2

# def search_distance(p1, d1, p2, d2):
#     P1 = np.array(p1)
#     P2 = np.array(p2)
#     d1 = np.array(d1)
#     d2 = np.array(d2)

#     start = 0
#     end = 1e18
#     for i in range(80)
        


# for x,y,z,dx,dy,dz in sorted(coords)[:1]:
#     xyz = (x,y,z)
#     dxyz = (dx,dy,dz)
#     dist, c1, c2 = calculate_distance(Ps, Pd, xyz, dxyz)
#     l = np.linalg.norm(dxyz)
#     rang = np.arange(-dist/l, dist/l) * dxyz + c2

# for cx,cy,cz in rang:
#     for x,y,z,dx,dy,dz in sorted(coords)[2:4]:
#         xyz = (x,y,z)
#         dxyz = (dx,dy,dz)
#         print(calculate_distance((cx,cy,cz), Pd, xyz, dxyz)[0])

dists = []
for x,y,z,dx,dy,dz in sorted(coords)[:1]:
    xyz = (x,y,z)
    dxyz = (dx,dy,dz)
    # closest_point = closest_point_on_second_line(Ps, Pd, xyz, dxyz)
    # closest_point = find_closest_point(Ps, Pd, xyz, dxyz)
    # print(closest_point)
    # closest_point2 = find_closest_point(xyz, dxyz, Ps, Pd)
    # print(closest_point2)
    # dist = np.linalg.norm(closest_point - closest_point2)
    dist, c1, c2 = calculate_distance(Ps, Pd, xyz, dxyz)
    # if len(dists) == 0:
    # ax.quiver(*c1, *(c2-c1), linewidth=5, color="black")
    Ps = Ps + (c2 - c1)
    print((c1 - c2))
        # exit()
    print(dist)
    dist, c1, c2 = calculate_distance(Ps, Pd, xyz, dxyz)
    dists.append(dist)
    print(dist)
    # ax.quiver(*closest_point, *closest_point2, linewidth=3, color="black")
    # print(calculate_distance(Ps, Pd, xyz, dxyz))
    print()

print(sorted(dists))

m = 4e12
r = 0
for ddy in range(-r, r+1):
    for ddx in range(-r, r+1):
        for ddz in range(-r, r+1):
            # ax.quiver(sx-sdx*m, sy-sdy*m, sz-sdz*m, sdx+ddx, sdy+ddy, sdz+ddz, length=400000000000000, normalize=True, color="red", linewidth=1)
            ax.quiver(sx, sy, sz, 1, 1, 1, length=40000000000000, normalize=True, color="red", linewidth=1)

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# def on_mouse_move(event):
#     print('Event received:',event.xdata,event.ydata)

# plt.connect('motion_notify_event',on_mouse_move)

# Show the plot
plt.show()
exit()


# intersections = find_intersection(lines)

# print(intersections)

print(coords)

# print(intersecting_lines())
for line in find_intersecting_lines():
    print(line)

# for xyz1, xyz2 in combinations(coords, r=2):
s2 = 0
import math
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        xyz1 = coords[i]
        xyz2 = coords[j]
        print(xyz1)
        px1, py1, pz1, vx1, vy1, vz1 = xyz1
        px2, py2, pz2, vx2, vy2, vz2 = xyz2
        slope1 = vy1 / vx1
        b1 = py1 - slope1 * px1
        slope2 = vy2 / vx2
        b2 = py2 - slope2 * px2
        ix, iy = find_intersection(slope1, b1, slope2, b2)

        # if 200000000000000 <= ix <= 400000000000000:
        #     if 200000000000000 <= iy <= 400000000000000:
        #         if (px1 - ix) * vx1 < 0 and (px2 - ix) * vx2 < 0:
        #             if (py1 - iy) * vy1 < 0 and (py2 - iy) * vy2 < 0:
        #                 s += 1
        #                 print("inside")

        if (px1 - ix) * vx1 < 0 and (px2 - ix) * vx2 < 0:
            if (py1 - iy) * vy1 < 0 and (py2 - iy) * vy2 < 0:
                dt = (px1 - ix) / vx1
                if math.isclose(dt * vz1 + pz1, dt * vz2 + pz2):
                    s += 1
                    print("inside")
        # print(ix, iy)
        # print(ix, iy)
        # if 7 <= ix <= 27:
        #     if 7 <= iy <= 27:
        #         if (px1 - ix) * vx1 < 0 and (px2 - ix) * vx2 < 0:
        #             if (py1 - iy) * vy1 < 0 and (py2 - iy) * vy2 < 0:
        #                 print("inside")
        #                 s2 += 1

print(s2)

print(s)
