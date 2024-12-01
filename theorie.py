import numpy as np
import matplotlib.pyplot as plt
import os 
from lecture import lecture_exp         # entrée : filename, coeff_1, coeff_2 / sortie :  x, y, x_adim, y_adim
from lecture import lecture_simu        # entrée : filename, add_x,factor_x, add_y, factor_y / sortie : x, y, x_dim, y_dim
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



plt.figure(2)
plt.plot(position_mu_adim_10, u_mean_adim_10, 'o-', label="r/D = 1.0")
plt.plot(position_mu_adim_30, u_mean_adim_30, 'o-', label="r/D = 3.0")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("theorie-u_mean_adim.png")

####################### uu (figure 5 u'/ub) #######################################
# Impinging Jet: H/D=2, Re=23000
# Single wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D         uu/(UBULK**2)
position_uu_adim_10, uu_adim_10, position_uu_dim_10 , uu_dim_10 = lecture_exp('ij2lr-10-sw-uu.dat', D, u_bulk**2)
position_uu_adim_30, uu_adim_30, position_uu_dim_30 , uu_dim_30 = lecture_exp('ij2lr-30-sw-uu.dat', D, u_bulk**2)

u_fluct_adim_10 = np.sqrt(uu_adim_10)
u_fluct_adim_30 = np.sqrt(uu_adim_30)

plt.figure(4)
plt.plot(position_uu_adim_10, u_fluct_adim_10, 'o-', label="r/D = 1.0")
plt.plot(position_uu_adim_30, u_fluct_adim_30, 'o-', label="r/D = 3.0")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("u' adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("theorie-u_adim.png")


####################### vv (figure 4 v/ub) #######################################
# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D      vv/(UBULK**2)

position_vv_adim_10, vv_adim_10, position_vv_dim_10 , vv_dim_10 = lecture_exp('ij2lr-10-cw-vv.dat', D, u_bulk**2)
position_vv_adim_30, vv_adim_30, position_vv_dim_30 , vv_dim_30 = lecture_exp('ij2lr-30-cw-vv.dat', D, u_bulk**2)

v_fluct_adim_10 = np.sqrt(vv_adim_10)
v_fluct_adim_30 = np.sqrt(vv_adim_30)

plt.figure(6)
plt.plot(position_vv_adim_10, v_fluct_adim_10, 'o-', label="r/D = 1.0")
plt.plot(position_vv_adim_30, v_fluct_adim_30, 'o-', label="r/D = 3.0")
plt.xlabel("Position y/D")
plt.ylabel("vitesse v/UBULK")
plt.title("v' adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("30-v_adim.png")

####################### uv (figure 6 uv/ub²) #######################################
# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D      vv/(UBULK**2)

position_uv_adim_10, uv_adim_10, position_uv_dim_10 , uv_dim_10 = lecture_exp('ij2lr-10-cw-uv.dat', D, u_bulk**2)
position_uv_adim_30, uv_adim_30, position_uv_dim_30 , uv_dim_30 = lecture_exp('ij2lr-30-cw-uv.dat', D, u_bulk**2)

plt.figure(8)
plt.plot(position_uv_adim_10, uv_adim_10, 'o-', label="r/D = 1.0")
plt.plot(position_uv_adim_30, uv_adim_30, 'o-', label="r/D = 3.0")
plt.xlabel("Position y/D")
plt.ylabel("vitesse -uv/UBULK**2")
plt.title("uv adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("theorie_uv_adim.png")


####################### k (figure 13 k**0.5/ub) #######################################


# Interpolation des fichiers uu et vv
position_inter_10, uu_inter_10, vv_inter_10 = interpolate_lists(position_uu_dim_10 , uu_dim_10,position_vv_dim_10 , vv_dim_10)
position_inter_30, uu_inter_30, vv_inter_30 = interpolate_lists(position_uu_dim_30 , uu_dim_30,position_vv_dim_30 , vv_dim_30)

k_dim_10 = 0.5*(uu_inter_10 + vv_inter_10 )
k_dim_30 = 0.5*(uu_inter_30 + vv_inter_30)

plt.figure(10)
plt.plot(position_inter_10/D, np.sqrt(k_dim_10)/u_bulk, 'o-', label="r/D = 1.0")
plt.plot(position_inter_30/D, np.sqrt(k_dim_30)/u_bulk, 'o-', label="r/D = 3.0")
plt.xlabel("Position y/D")
plt.ylabel("k**0.5/UBULK")
plt.grid()
plt.legend()
plt.title("Profil d'énergie cinétique turbulente adimensionné")
plt.savefig("theorie_k_adim_exp.png")


####################### Nusselt (figure 11 Nu/Re**0.7*Pr*0.4) #######################################
# Impinging Jet: H/D=2, Re=23000
# Nusselt Number Data
# Expts. of Baughn et al (1992)
#  R/D        Nu/(Re**0.7)

position_Nu_exp_adim, Nu_exp_adim, position_Nu_exp_dim, Nu_exp_dim = lecture_exp('ij2lr-nuss.dat', D, Re**0.7)

plt.figure(12)
plt.plot(position_Nu_exp_adim, Nu_exp_adim, 'o-', label="expérimental")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.legend()
plt.savefig("theorie-nuss-exp.png")





plt.show()


