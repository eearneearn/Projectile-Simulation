# import pygame
# import numpy as np

# wScreen = 1280
# hScreen = 720

# win = pygame.display.set_mode((wScreen,hScreen))

# class bullet(object):
#     def __init__(self,x,y)

#     def 

# import numpy as np
# import matplotlib.pyplot as pl

# sin = np.sin
# cos = np.cos
# pi = np.pi


# def y_position(y0, v0, phi, g, t):
#     y_t = y0 + v0 * sin(phi) * t + (g * t**2) / 2
#     return y_t


# def x_position_force(x0, v0, phi, k, m, alpha, t):
#     term1 = (-k / m) * (1 / alpha ** 2)
#     term2 = -np.e ** (-alpha * t)
#     x_t = x0 + v0 * cos(phi) * t + term1 * (t * (term2 - 1) + (2 - 2 * term2) / alpha)
#     return x_t


# def x_position_no_force(x0, v0, phi, t):
#     x_t = x0 + v0 * cos(phi) * t
#     return x_t


# time = np.linspace(0, 10, 100)

# #-------------  I N P U T  -------------#
# x_init  = 0
# y_init  = 2
# v_init  = 3
# theta   = 45
# gravity = -9.8
# m = 1
# k = 1
# alpha = 0.5
# #-------------  I N P U T  -------------#
# x_with_force = []
# x_with_no_force = []
# y = []

# for time_i in time:
#     x_with_force.append(x_position_force(x_init, v_init, theta, k, m, alpha, time_i))
#     x_with_no_force.append(x_position_no_force(x_init, v_init, theta, time_i))
#     y.append(y_position(y_init, v_init, theta, gravity, time_i))

# # print(x1_data)
# # print(x2_data)
# # print(y_data)

# pl.subplot(211)
# pl.title('Constant and Time-Dependent Forces')
# pl.xlabel('time')
# plot1 = pl.plot(time, x_with_force, 'r', label='x_coord_dynamicF')
# plot2 = pl.plot(time, x_with_no_force, 'g', label='x_coord_staticF')
# plot3 = pl.plot(time, y, 'b', label='y_coord')
# pl.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)

# pl.subplot(212)
# pl.title('Trajectory (x,y)')
# pl.xlabel('X')
# pl.ylabel('Y')
# plot4 = pl.plot(x_with_force, y, 'r^')
# plot5 = pl.plot(x_with_no_force, y, 'b*')
# pl.show()