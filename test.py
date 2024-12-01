import numpy as np
import matplotlib.pyplot as plt
import os 
from lecture import lecture_exp         # entrée : filename, coeff_1, coeff_2 / sortie :  x, y, x_adim, y_adim
from lecture import lecture_simu        # entrée : filename, add_x,factor_x, add_y, factor_y / sortie : x, y, x_dim, y_dim
from lecture import sort
from interpolation import interpolate_files 
from interpolation import interpolate_lists
import pandas as pd

u_bulk = 13 # m/s
D = 0.026 # m
Re = 23000
DeltaT = 200
lambda_air = 0.0242


####################### mu : u mean (figure 7 sqrt(U²+V²)/Ub) #######################################
# Données expérimentales
position_mu_adim_10, u_mean_adim_10, position_mu_dim_10 , u_mean_dim_10 = lecture_exp('ij2lr-10-sw-mu.dat', D, u_bulk)
position_mu_adim_30, u_mean_adim_30, position_mu_dim_30 , u_mean_dim_30 = lecture_exp('ij2lr-30-sw-mu.dat', D, u_bulk)

# Fluent
position_mu_fluent_dim_10, u_mean_fluent_dim_10, position_mu_fluent_adim_10 , u_mean_fluent_adim_10 = lecture_simu('umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_fluent_dim_30, u_mean_fluent_dim_30, position_mu_fluent_adim_30 , u_mean_fluent_adim_30 = lecture_simu('umean_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

plt.figure(2)
plt.plot(position_mu_adim_10, u_mean_adim_10, 'o-', label="r/D = 1.0 exp")
plt.plot(position_mu_fluent_adim_10, u_mean_fluent_adim_10, 'o-', label="r/D = 1.0 Fluent")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()

sort_position_fluent, sort_u_mean_fluent = sort(position_mu_fluent_adim_10, u_mean_fluent_adim_10)

plt.figure(3)
plt.plot(position_mu_adim_10, u_mean_adim_10, 'o-', label="r/D = 1.0 exp")
plt.plot(sort_position_fluent, sort_u_mean_fluent, 'o-', label="r/D = 1.0 Fluent")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne sort")
plt.legend()
plt.grid()

plt.show()
