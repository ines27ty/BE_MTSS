import numpy as np
import matplotlib.pyplot as plt
import os 
from lecture import lecture_exp         # entrée : filename, coeff_1, coeff_2 / sortie :  x, y, x_adim, y_adim
from lecture import lecture_simu        # entrée : filename, add_x,factor_x, add_y, factor_y / sortie : x, y, x_dim, y_dim
from lecture import sort
from lecture import lecture_starccm_single
from lecture import lecture_starccm_double
from interpolation import interpolate_files 
from interpolation import interpolate_lists

u_bulk = 13 # m/s
D = 0.026 # m
Re = 23000
DeltaT = 200
lambda_air = 0.0242


# Inlet 2
position_mu_inlet2_dim_10, u_mean_inlet2_dim_10, position_mu_inlet2_adim_10 , u_mean_inlet2_adim_10 = lecture_simu('umean_inlet2_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)


print(position_mu_inlet2_adim_10)