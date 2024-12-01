import random
import math
import matplotlib.pyplot as plt


def polar_angles(data):
    start = min(data, key=lambda p: (p[1], p[0]))
    data.remove(start)
    sorted_data = sorted(data,key= lambda p: (math.atan2(p[1]-start[1],p[0]-start[0]),p[0],p[1]))
    sorted_data.insert(0, start) 

    return sorted_data


def check_ccw(point_a,point_b,point_c):
    a_x=point_a[0]
    a_y=point_a[1]
    b_x=point_b[0]
    b_y=point_b[1]
    c_x=point_c[0]
    c_y=point_c[1]
    v_x=b_x-a_x
    v_y=b_y-a_y
    w_x=c_x-a_x
    w_y=c_y-a_y
    area = (v_x*w_y)-(w_x*v_y)

    if area<0:
        return -1
    elif area>0:
        return 1
    else :
        return 0

def boundary_points(data,stack=None,ax=None, lines=[]):
    if stack is None:
        stack = []
    stack.append(data[0])
    stack.append(data[1])

    for i in range(2,len(data)):
        next = data[i]
        p = stack.pop()
        while(len(stack)!=0 and check_ccw(stack[-1],p,next)<=0):
            p = stack.pop()
        stack.append(p)
        stack.append(next)
        if ax:
            plot_lines(stack,ax,lines)
            plt.pause(0.5)
    p = stack.pop()

    if(check_ccw(stack[-1],p,stack[0])>0):
        stack.append(p)
    stack.append(stack[0])

    if ax:
        plot_lines(stack,ax, lines)
        plt.pause(1)

    return stack

def plot_lines(stack, ax, lines):
    x_b,y_b = zip(*stack)
    line1, =ax.plot(x_b, y_b, color='red', marker='o', linestyle='-', linewidth=2, label='Convex Hull')
    lines.append(line1)
    plt.pause(0.5)
    if len(lines)>1:
        lines[-2].remove()

def plot_all(sorted_data, ax):
    x, y = zip(*sorted_data)
    ax.scatter(x, y, color='blue', marker='o', label='Points')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Random Coordinates with Convex Hull')
    ax.legend()
    ax.grid(True)



data = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(20)]
sorted_data = polar_angles(data)
fig, ax = plt.subplots()
plot_all(sorted_data,ax)
plt.show(block=False)
stack=boundary_points(sorted_data,ax=ax)
print("Data points:", data)
print("Convex hull points:", stack)