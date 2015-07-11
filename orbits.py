import matplotlib.pyplot as plt
from math import *

#constants
r = 1.496e11;
mS = 1.989e30;
G = 6.674e-11;
vE = 3e4;

x = 0;
y = r;
xVel = vE;
yVel = 0;
xAcel = 0;
yAcel = 0;
angle = pi/2;
p = 60;
xA = [];
yA = [];

#logic
for n in range(0, 60*10000):
    a = -G*mS/r**2;
    xAcel = cos(angle) * a;
    yAcel = sin(angle) * a;
    #print xAcel, yAcel, xVel, yVel;
    #print angle;
    if y > 0:
        y = y + yVel * p + 0.5 * yAcel * p**2;
    else:
        y = y + yVel * p - 0.5 * yAcel * p**2;
    x = x + xVel * p + 0.5 * xAcel * p**2;
    xVel = xVel + xAcel * p;
    yVel = yVel + yAcel * p;
    r = (x**2+y**2)**0.5;
    if y < 0:
        angle = -atan2(-y, x);         
    else:
        angle = atan2(y, x);
    xA.append(x);
    yA.append(y);
#plotting
plt.plot(xA, yA);
plt.scatter(0, 0, color='red');
plt.axis([-2e11, 2e11, -2e11, 2e11]);
plt.gca().set_aspect('equal', adjustable='box');
#plt.set_autoscale_on(False);
plt.show();