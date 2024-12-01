import numpy as np
import matplotlib.pyplot as plt
import os 
from lecture import lecture_exp         # entrée : filename, coeff_1, coeff_2 / sortie :  x, y, x_adim, y_adim
from lecture import lecture_simu        # entrée : filename, add_x,factor_x, add_y, factor_y / sortie : x, y, x_dim, y_dim
from lecture import sort
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

plt.figure(2)
plt.plot(position_mu_adim_10, u_mean_adim_10, 'o-', label="r/D = 1.0 exp")
plt.plot(position_mu_fluent_adim_10[:70], u_mean_fluent_adim_10[:70], 'o-', label="r/D = 1.0 Fluent")
plt.plot(position_mu_adim_30, u_mean_adim_30, 'o-', label="r/D = 3.0 exp")
plt.plot(position_mu_fluent_adim_30[:70], u_mean_fluent_adim_30[:70], 'o-', label="r/D = 3.0 Fluent")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("comp-u_mean_adim.png")

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

plt.figure(3)
plt.plot(position_inter_10, k_dim_10, 'o-', label="r/D = 1.0 Exp")
plt.plot(position_k_fluent_dim_10, k_fluent_dim_10, 'o-', label="r/D = 1.0 Fluent")
plt.plot(position_inter_30, k_dim_30, 'o-', label="r/D = 3.0 Exp")
plt.plot(position_k_fluent_dim_30[:70], k_fluent_dim_30[:70], 'o-', label="r/D = 3.0 Fluent")
plt.xlabel("Position y")
plt.ylabel("k")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente")
plt.legend()
plt.savefig("comp_k_dim.png")

print(len(position_k_fluent_dim_30))

plt.figure(4)
plt.plot(position_inter_10/D, np.sqrt(k_dim_10)/u_bulk, 'o-', label="r/D = 1.0")
plt.plot(position_k_fluent_dim_10/D, np.sqrt(k_fluent_dim_10)/u_bulk, 'o-', label="r/D = 1.0 Fluent")
plt.plot(position_inter_30/D, np.sqrt(k_dim_30)/u_bulk, 'o-', label="r/D = 3.0")
plt.plot(position_k_fluent_dim_30[:70]/D, np.sqrt(k_fluent_dim_30[:70])/u_bulk, 'o-', label="r/D = 3.0 Fluent")
plt.xlabel("Position y/D")
plt.ylabel("k**0.5/UBULK")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente adimensionné")
plt.legend()
plt.savefig("comp_k_adim_exp.png")


####################### Nusselt (figure 11 Nu/Re**0.7*Pr*0.4) #######################################
# Impinging Jet: H/D=2, Re=23000
# Nusselt Number Data
# Expts. of Baughn et al (1992)
#  R/D        Nu/(Re**0.7)

position_Nu_exp_adim, Nu_exp_adim, position_Nu_exp_dim, Nu_exp_dim = lecture_exp('ij2lr-nuss.dat', D, Re**0.7)

# Fluent
position_heat, heat,position_heat_adim, heat_adim = lecture_simu('heat_flux.xy', 0, 1/D, 0, 1)

position_Nu_dim, heat = sort(position_heat, heat) 
position_Nu_adim = position_Nu_dim/D

h = heat/DeltaT
Nu_fluent = h*D/lambda_air


plt.figure(6)
plt.plot(position_Nu_exp_adim, Nu_exp_adim, 'o-', label="exp")
plt.plot(position_Nu_adim[:125] ,Nu_fluent[:125]/(Re**0.7), 'o-', label="fluent")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.legend()
plt.savefig("comp_nu_adim.png")

print(len(position_Nu_adim))
#############################################################
plt.show()


