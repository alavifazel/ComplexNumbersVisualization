import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin, radians, degrees, atan

import matplotlib.animation as animation

vectorScale = 10 # don't change this to None. Matplotlib will use it's own scaling
origin = [0], [0]

V = np.array([[2,2],[1,-1]], dtype='f8')
fig,axes = plt.subplots(1,2)

def vectorLength(v):
    return sqrt(np.power(v[0],2) + np.power(v[1],2))

def rotateVector(v, r,theta, dTheta):
    v[0] =  r * (cos(radians(theta + dTheta)))   
    v[1] =  r * (sin(radians(theta + dTheta)))
    
def initialAngel(v):
    return degrees(atan(v[1]/v[0]))

sx = [[],[],[]]
sy = [[],[],[]]

def plotSinFunctions(x, y, color):
    axes[1].plot(x, y, color)
    
for i in range(1, 1000): 
    vs = V[0] + V[1]
    
    projections = [vs[0], V[0][0], V[1][0]]

    if i == 1: # calculating initial angel
        t0 = initialAngel(V[0])
        t1 = initialAngel(V[1])
        t = initialAngel(vs)

    # plt.title("Iteration: " + str(i))

    axes[0].quiver(*origin, vs[0], vs[1], scale=vectorScale)
    axes[0].quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale = vectorScale)


    r0 = vectorLength(V[0])
    r1 = vectorLength(V[1])
    r = vectorLength(vs)
    
    rotateVector(V[0], r0,t0, i)
    rotateVector(V[1], r1,t1, i)
    rotateVector(vs, r,t, i)


    if i > 150:
        for j in range(0,3):
            sx[j].pop(0)
            sy[j].pop(0)
        axes[1].clear()    
    
#    if i%3 == 0: uncomment for non-smooth plotting (better performance but uglier)
    for j in range(0,3):
        sx[j].append(i)
        sy[j].append(projections[j])
    plotSinFunctions(sx[0], sy[0], "k")
    plotSinFunctions(sx[1], sy[1], "r")
    plotSinFunctions(sx[2], sy[2], "b")
    
    plt.pause(0.00001)

    axes[0].clear()
plt.show()
