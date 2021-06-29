#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:02:06 2020

@author: johnviljoen
"""

''' This file contains all parameters (paras) required to run the simulation,
the aircraft, environmental, simulation, initial conditions, and other parameters'''

#import numpy as np
import numpy as np
from numpy import pi
from scipy.constants import g

# In[initial_conditions mk2]  

''' states in m/s, rad, rad/s '''
npos = 0. # m
epos = 0. # m
h = 3048. # m
phi = 0.    # rad
theta = 0. # rad
psi = 0. # rad

vt = 213.36 # m/s
alpha = 1.0721 * pi/180 # rad
beta = 0. # rad
p = 0. # rad/s
q = 0. # rad/s
r = 0. # rad/s

''' control states in rad '''
T = 2886.6468
dh = -2.0385 #* pi/180
da = -0.087577 #* pi/180
dr = -0.03877 #* pi/180
lef = 0.3986

# In[aircraft parameters]  

weight                  = 91188         # Newtons

Ixx                     = 12875         # Kg m^2
Iyy                     = 75674         # Kg m^2
Izz                     = 85552         # Kg m^2
Ixz                     = 1331          # Kg m^2
# the other Izy, Iyz = 0

b                       = 9.144         # m wingspan
S                       = 27.87         # m^2 wing area
cbar                    = 3.45          # m wing mean aerodynamic chord

He                      = 216.9         # engine angular momentum constant

x_cg_ref                = 0.35 * cbar   # assuming mac = cbar
x_cg                    = 0.8*x_cg_ref  # FOR NOW THIS IS WRONG

dh_limits               = 25.           # degrees +-
da_limits               = 5.375         # degrees +-
aileron_limits          = 21.5          # degrees +-
rudder_limits           = 30.           # degrees +-
leading_edge_flap_limit = 25.           # degrees NOT +-, this is the 'lef'
speed_brake_limit       = 60.           # degrees NOT +-

# unecessary:
length = 14.8 #m
height = 4.8 #m

# In[limits]

npos_min        = -np.inf       # (m)
epos_min        = -np.inf       # (m)
h_min           = 0             # (m)
phi_min         = -np.inf       # (deg)
theta_min       = -np.inf       # (deg)
psi_min         = -np.inf       # (deg)
V_min           = 0             # (m/s)
alpha_min       = -20.          # (deg)
beta_min        = -30.          # (deg)
p_min           = -30           # (deg/s)
q_min           = -10           # (deg/s)
r_min           = -5            # (deg/s)

T_min = 1000 # (lbs)
dh_min = -25 # (deg)
da_min = -21.5 # (deg)
dr_min = -30. # (deg)
lef_min = 0. # (deg)


# In[simulation parameters]  

time_step, time_start, time_end = 0.001, 0., 30.

# fi_flag = 1 -> high fidelity model (full Nguyen)
# fi_flag = 1 -> low fidelity model (Stevens Lewis reduced)
fi_flag = 1

# stability_flag only functional for high fidelity model currently!
# stability_flag = 1 -> unstable xcg 35% model
# stability_flag = 0 -> stable xcg 25% model
stability_flag = 0

# In[wrap for input]  

initial_state_vector = np.array([npos, epos, h, phi, theta, psi, vt, alpha, beta, p, q, r, T, dh, da, dr, lef, fi_flag])
    
aircraft_properties = [Ixx, Iyy, Izz, Ixz, weight, b, S, cbar, He, x_cg, x_cg_ref]

simulation_parameters = [time_step, time_start, time_end, g, stability_flag]
