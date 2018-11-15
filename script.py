# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:32:36 2018

@author: jieqiang
"""

from kinematic_func import three_agents
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt

# b,c,d are three edge lengths of the desired formation
b = 3.0
c = 4.0
d = 5.0

y0 = [1,1,3,3,2,1]
t = np.linspace(0, 100, 100000)

sol = odeint(three_agents, y0, t, args=(b, c, d))

plt.plot(sol[:, 0], sol[:, 1], 'b', label='agent1')
plt.plot(sol[:, 2], sol[:, 3], 'r', label='agent2')
plt.plot(sol[:, 4], sol[:, 5], 'g', label='agent3')

#plot the initial positions
size = 0.03
circle1 = plt.Circle(y0[0:2], 2*size, color='b', fill=False)
circle2 = plt.Circle(y0[2:4], 2*size, color='r', fill=False)
circle3 = plt.Circle(y0[4:], 2*size, color='g', fill=False)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

#plot the final positions
circle1f = plt.Circle(sol[-1,0:2], size, color='b', fill=True)
circle2f = plt.Circle(sol[-1,2:4], size, color='r', fill=True)
circle3f = plt.Circle(sol[-1,4:], size, color='g', fill=True)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle1f)
ax.add_artist(circle2f)
ax.add_artist(circle3f)

#plot the final formation
dashes = [1,1,1,1]
line_12,=ax.plot(sol[-1,[0,2]],sol[-1,[1,3]],'--', color='black')
line_12.set_dashes(dashes)
line_23,=ax.plot(sol[-1,[2,4]],sol[-1,[3,5]],'--', color='black')
line_23.set_dashes(dashes)
line_31,=ax.plot(sol[-1,[0,4]],sol[-1,[1,5]],'--', color='black')
line_31.set_dashes(dashes)

#plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
#plt.xlabel('t')
plt.axes().set_aspect('equal')
plt.grid()
plt.show()