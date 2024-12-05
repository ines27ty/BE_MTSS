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


####################### mu : u mean (figure 7 sqrt(U²+V²)/Ub) #######################################
# Données expérimentales
position_mu_adim_10, u_mean_adim_10, position_mu_dim_10 , u_mean_dim_10 = lecture_exp('ij2lr-10-sw-mu.dat', D, u_bulk)
position_mu_adim_30, u_mean_adim_30, position_mu_dim_30 , u_mean_dim_30 = lecture_exp('ij2lr-30-sw-mu.dat', D, u_bulk)

# Fluent
position_mu_fluent_dim_10, u_mean_fluent_dim_10, position_mu_fluent_adim_10 , u_mean_fluent_adim_10 = lecture_simu('umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_fluent_dim_30, u_mean_fluent_dim_30, position_mu_fluent_adim_30 , u_mean_fluent_adim_30 = lecture_simu('umean_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_fluent_adim_10, u_mean_fluent_adim_10 = sort(position_mu_fluent_adim_10, u_mean_fluent_adim_10)
position_mu_fluent_adim_30, u_mean_fluent_adim_30 = sort(position_mu_fluent_adim_30, u_mean_fluent_adim_30)

# Fluent Wall
position_mu_wall_dim_10, u_mean_wall_dim_10, position_mu_wall_adim_10 , u_mean_wall_adim_10 = lecture_simu('wall_u_mean_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_wall_dim_30, u_mean_wall_dim_30, position_mu_wall_adim_30 , u_mean_wall_adim_30 = lecture_simu('wall_u_mean_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_wall_adim_10, u_mean_wall_adim_10 = sort(position_mu_wall_adim_10, u_mean_wall_adim_10)
position_mu_wall_adim_30, u_mean_wall_adim_30 = sort(position_mu_wall_adim_30, u_mean_wall_adim_30)



plt.figure(2)
plt.plot(position_mu_adim_10, u_mean_adim_10, label="r/D = 1.0 Expérimental", markersize=5, linewidth=2)
plt.plot(position_mu_fluent_adim_10[:70], u_mean_fluent_adim_10[:70], label="r/D = 1.0 k-ε", markersize=5, linewidth=2)
plt.plot(position_mu_wall_adim_10[:70], u_mean_wall_adim_10[:70], label="r/D = 1.0 k-ε Enhanced Wall Treatment", markersize=5, linewidth=2)
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Profil de vitesse moyenne r/D = 1.0")
plt.legend()
plt.grid()
plt.savefig("wall-u_mean_adim_1d.png")

plt.figure(3)
plt.plot(position_mu_adim_30, u_mean_adim_30, label="r/D = 3.0 Expérimental", markersize=5, linewidth=2)
plt.plot(position_mu_fluent_adim_30[:70], u_mean_fluent_adim_30[:70], label="r/D = 3.0 k-ε",markersize=5, linewidth=2)
plt.plot(position_mu_wall_adim_30[:70], u_mean_wall_adim_30[:70], label="r/D = 3.0 k-ε Enhanced Wall Treatment", markersize=5, linewidth=2)
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Profil de vitesse moyenne r/D = 3.0")
plt.legend()
plt.grid()
plt.savefig("wall-u_mean_adim_3d.png")

####################### uu (figure 5 u'/ub) #######################################
# Impinging Jet: H/D=2, Re=23000
# Single wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D         uu/(UBULK**2)
position_uu_adim_10, uu_adim_10, position_uu_dim_10 , uu_dim_10 = lecture_exp('ij2lr-10-sw-uu.dat', D, u_bulk**2)
position_uu_adim_30, uu_adim_30, position_uu_dim_30 , uu_dim_30 = lecture_exp('ij2lr-30-sw-uu.dat', D, u_bulk**2)

u_fluct_adim_10 = np.sqrt(uu_adim_10)
u_fluct_adim_30 = np.sqrt(uu_adim_30)

####################### vv (figure 4 v/ub) #######################################
# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D      vv/(UBULK**2)

position_vv_adim_10, vv_adim_10, position_vv_dim_10 , vv_dim_10 = lecture_exp('ij2lr-10-cw-vv.dat', D, u_bulk**2)
position_vv_adim_30, vv_adim_30, position_vv_dim_30 , vv_dim_30 = lecture_exp('ij2lr-30-cw-vv.dat', D, u_bulk**2)

v_fluct_adim_10 = np.sqrt(vv_adim_10)
v_fluct_adim_30 = np.sqrt(vv_adim_30)

####################### uv (figure 6 uv/ub²) #######################################
# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D      vv/(UBULK**2)

position_uv_adim_10, uv_adim_10, position_uv_dim_10 , uv_dim_10 = lecture_exp('ij2lr-10-cw-uv.dat', D, u_bulk**2)
position_uv_adim_30, uv_adim_30, position_uv_dim_30 , uv_dim_30 = lecture_exp('ij2lr-30-cw-uv.dat', D, u_bulk**2)

####################### k (figure 13 k**0.5/ub) #######################################

# Expérimental
# Interpolation des fichiers uu et vv
position_inter_10, uu_inter_10, vv_inter_10 = interpolate_lists(position_uu_dim_10 , uu_dim_10,position_vv_dim_10 , vv_dim_10)
position_inter_30, uu_inter_30, vv_inter_30 = interpolate_lists(position_uu_dim_30 , uu_dim_30,position_vv_dim_30 , vv_dim_30)

k_dim_10 = 0.5*(uu_inter_10 + vv_inter_10 )
k_dim_30 = 0.5*(uu_inter_30 + vv_inter_30)

# Fluent
position_k_fluent_dim_10, k_fluent_dim_10, position_k_fluent_adim_10 , k_fluent_adim_10 = lecture_simu('k_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_fluent_dim_30, k_fluent_dim_30, position_k_fluent_adim_30 , k_fluent_adim_30 = lecture_simu('k_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_fluent_dim_10, k_fluent_dim_10 = sort(position_k_fluent_dim_10, k_fluent_dim_10)
position_k_fluent_dim_30, k_fluent_dim_30 = sort(position_k_fluent_dim_30, k_fluent_dim_30)

# Fluent
position_k_wall_dim_10, k_wall_dim_10, position_k_wall_adim_10 , k_wall_adim_10 = lecture_simu('wall_tke_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_wall_dim_30, k_wall_dim_30, position_k_wall_adim_30 , k_wall_adim_30 = lecture_simu('wall_tke_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_wall_dim_10, k_wall_dim_10 = sort(position_k_wall_dim_10, k_wall_dim_10)
position_k_wall_dim_30, k_wall_dim_30 = sort(position_k_wall_dim_30, k_wall_dim_30)


plt.figure(5)
plt.plot(position_inter_10, k_dim_10, label="r/D = 1.0 Expérimental")
plt.plot(position_k_fluent_dim_10[:70], k_fluent_dim_10[:70], label="r/D = 1.0 k-ε")
plt.plot(position_k_wall_dim_10[:70], k_wall_dim_10[:70], label="r/D = 1.0 k-ε \n Enhanced Wall Treatment")
plt.xlabel("Position y")
plt.ylabel("k")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente")
plt.legend()
plt.savefig("wall_k_dim_1d.png")


plt.figure(6)
plt.plot(position_inter_30, k_dim_30, label="r/D = 3.0 Expérimental")
plt.plot(position_k_fluent_dim_30[:70], k_fluent_dim_30[:70], label="r/D = 3.0 k-ε")
plt.plot(position_k_wall_dim_30[:70], k_wall_dim_30[:70], label="r/D = 3.0  k-ε Enhanced Wall Treatment")
plt.xlabel("Position y")
plt.ylabel("k")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente")
plt.legend()
plt.savefig("wall_k_dim_3d.png")


####################### Nusselt (figure 11 Nu/Re**0.7*Pr*0.4) #######################################
# Impinging Jet: H/D=2, Re=23000
# Nusselt Number Data
# Expts. of Baughn et al (1992)
#  R/D        Nu/(Re**0.7)

position_Nu_exp_adim, Nu_exp_adim, position_Nu_exp_dim, Nu_exp_dim = lecture_exp('ij2lr-nuss.dat', D, Re**0.7)

# Fluent
position_fluent_heat, heat_fluent,position_fluent_heat_adim, heat_fluent_adim = lecture_simu('heat_flux.xy', 0, 1/D, 0, 1)

position_Nu_dim_fluent, heat_fluent = sort(position_fluent_heat, heat_fluent) 
position_Nu_adim_fluent = position_Nu_dim_fluent/D
h_fluent = heat_fluent/DeltaT
Nu_fluent = h_fluent*D/lambda_air

# Fluent wall
position_wall_heat, heat_wall,position_wall_heat_adim, heat_wall_adim = lecture_simu('wall_total_heat_flux.xy', 0, 1/D, 0, 1)

position_Nu_dim_wall, heat_wall = sort(position_wall_heat, heat_wall)
position_Nu_adim_wall = position_Nu_dim_wall/D
h_wall = heat_wall/DeltaT
Nu_wall = h_wall*D/lambda_air

plt.figure(7)
plt.plot(position_Nu_exp_adim, Nu_exp_adim, label="Expérimental")
plt.plot(position_Nu_adim_fluent[:125] ,Nu_fluent[:125]/(Re**0.7), label="k-ε")
plt.plot(position_Nu_adim_wall[:125] ,Nu_wall[:125]/(Re**0.7), label="k-ε Enhanced Wall Treatment")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.legend()
plt.savefig("wall_nu_adim.png")
#############################################################
plt.show()


