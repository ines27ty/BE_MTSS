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

# Inlet 1 eps 0.04
position_mu_eps1_dim_10, u_mean_eps1_dim_10, position_mu_eps1_adim_10 , u_mean_eps1_adim_10 = lecture_simu('eps_0.04_u_mean_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_eps1_dim_30, u_mean_eps1_dim_30, position_mu_eps1_adim_30 , u_mean_eps1_adim_30 = lecture_simu('eps_0.04_u_mean_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_eps1_adim_10, u_mean_eps1_adim_10 = sort(position_mu_eps1_adim_10, u_mean_eps1_adim_10)
position_mu_eps1_adim_30, u_mean_eps1_adim_30 = sort(position_mu_eps1_adim_30, u_mean_eps1_adim_30)

# Inlet 2 eps 0.004
position_mu_eps2_dim_10, u_mean_eps2_dim_10, position_mu_eps2_adim_10 , u_mean_eps2_adim_10 = lecture_simu('eps_0.004_u_mean_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_eps2_dim_30, u_mean_eps2_dim_30, position_mu_eps2_adim_30 , u_mean_eps2_adim_30 = lecture_simu('eps_0.004_u_mean_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_eps2_adim_10, u_mean_eps2_adim_10 = sort(position_mu_eps2_adim_10, u_mean_eps2_adim_10)
position_mu_eps2_adim_30, u_mean_eps2_adim_30 = sort(position_mu_eps2_adim_30, u_mean_eps2_adim_30)

# Inlet 3 eps 0.00004 
position_mu_eps3_dim_10, u_mean_eps3_dim_10, position_mu_eps3_adim_10 , u_mean_eps3_adim_10 = lecture_simu('eps_0.00004_u_mean_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_eps3_dim_30, u_mean_eps3_dim_30, position_mu_eps3_adim_30 , u_mean_eps3_adim_30 = lecture_simu('eps_0.00004_u_mean_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_eps3_adim_10, u_mean_eps3_adim_10 = sort(position_mu_eps3_adim_10, u_mean_eps3_adim_10)
position_mu_eps3_adim_30, u_mean_eps3_adim_30 = sort(position_mu_eps3_adim_30, u_mean_eps3_adim_30)


plt.figure(2)
plt.plot(position_mu_adim_10, u_mean_adim_10, label="r/D = 1.0 Expérimental")
plt.plot(position_mu_eps1_adim_10[:70], u_mean_eps1_adim_10[:70], label="r/D = 1.0 ε = 0.04 m²/s³") 
plt.plot(position_mu_eps2_adim_10[:70], u_mean_eps2_adim_10[:70], label="r/D = 1.0 ε = 0.004 m²/s³")
plt.plot(position_mu_eps3_adim_10[:70], u_mean_eps3_adim_10[:70], label="r/D = 1.0 ε = 0.00004 m²/s³")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("eps-u_mean_adim_1D.png")


plt.figure(3)
plt.plot(position_mu_adim_30, u_mean_adim_30, label="r/D = 3.0 Expérimental")
plt.plot(position_mu_eps1_adim_30[:70], u_mean_eps1_adim_30[:70], label="r/D = 3.0 ε = 0.04 m²/s³")
plt.plot(position_mu_eps2_adim_30[:70], u_mean_eps2_adim_30[:70], label="r/D = 3.0 ε = 0.004 m²/s³")
plt.plot(position_mu_eps3_adim_30[:70], u_mean_eps3_adim_30[:70], label="r/D = 3.0 ε = 0.00004 m²/s³")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("eps-u_mean_adim_3D.png")

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

k_dim_10 = 0.5* (np.power(uu_inter_10.flatten(),1)  + np.power(vv_inter_10.flatten(),1)   )
k_dim_30 = 0.5* (np.power(uu_inter_30.flatten(),1)  + np.power(vv_inter_30.flatten(),1)   )

# Fluent Inlet 0.04
position_k_eps1_dim_10, k_eps1_dim_10, position_k_eps1_adim_10 , k_eps1_adim_10 = lecture_simu('eps_0.04_tke_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_eps1_dim_30, k_eps1_dim_30, position_k_eps1_adim_30 , k_eps1_adim_30 = lecture_simu('eps_0.04_tke_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_eps1_dim_10, k_eps1_dim_10 = sort(position_k_eps1_dim_10, k_eps1_dim_10)
position_k_eps1_dim_30, k_eps1_dim_30 = sort(position_k_eps1_dim_30, k_eps1_dim_30)

# Fluent Inlet 0.004
position_k_eps2_dim_10, k_eps2_dim_10, position_k_eps2_adim_10 , k_eps2_adim_10 = lecture_simu('eps_0.004_tke_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_eps2_dim_30, k_eps2_dim_30, position_k_eps2_adim_30 , k_eps2_adim_30 = lecture_simu('eps_0.004_tke_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_eps2_dim_10, k_eps2_dim_10 = sort(position_k_eps2_dim_10, k_eps2_dim_10)
position_k_eps2_dim_30, k_eps2_dim_30 = sort(position_k_eps2_dim_30, k_eps2_dim_30)

# Fluent Inlet 0.00004
position_k_eps3_dim_10, k_eps3_dim_10, position_k_eps3_adim_10 , k_eps3_adim_10 = lecture_simu('eps_0.00004_tke_rD_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_eps3_dim_30, k_eps3_dim_30, position_k_eps3_adim_30 , k_eps3_adim_30 = lecture_simu('eps_0.00004_tke_rD_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_eps3_dim_10, k_eps3_dim_10 = sort(position_k_eps3_dim_10, k_eps3_dim_10)
position_k_eps3_dim_30, k_eps3_dim_30 = sort(position_k_eps3_dim_30, k_eps3_dim_30)

plt.figure(7)
plt.plot(position_inter_10/D, np.sqrt(k_dim_10)/u_bulk, label="r/D = 1.0 Expérimental")
plt.plot(position_k_eps1_dim_10[:70]/D, np.sqrt(k_eps1_dim_10[:70])/u_bulk, label="r/D = 1.0 ε = 0.04 m²/s³")
plt.plot(position_k_eps2_dim_10[:70]/D, np.sqrt(k_eps2_dim_10[:70])/u_bulk, label="r/D = 1.0 ε = 0.004 m²/s³")
plt.plot(position_k_eps3_dim_10[:70]/D, np.sqrt(k_eps3_dim_10[:70])/u_bulk, label="r/D = 1.0 ε = 0.00004 m²/s³")
plt.xlabel("Position y/D")
plt.ylabel("k**0.5/UBULK")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente adimensionné")
plt.legend()
plt.savefig("eps_k_adim_exp_1d.png")

plt.figure(5)
plt.plot(position_inter_30/D, np.sqrt(k_dim_30)/u_bulk, label="r/D = 3.0 Expérimental")
plt.plot(position_k_eps1_dim_30[:70]/D, np.sqrt(k_eps1_dim_30[:70])/u_bulk, label="r/D = 3.0 ε = 0.04 m²/s³")
plt.plot(position_k_eps2_dim_30[:70]/D, np.sqrt(k_eps2_dim_30[:70])/u_bulk, label="r/D = 3.0 ε = 0.004 m²/s³")
plt.plot(position_k_eps3_dim_30[:70]/D, np.sqrt(k_eps3_dim_30[:70])/u_bulk, label="r/D = 3.0 ε = 0.00004 m²/s³")
plt.xlabel("Position y/D")
plt.ylabel("k**0.5/UBULK")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente adimensionné")
plt.legend()
plt.savefig("eps_k_adim_exp_3d.png")


####################### Nusselt (figure 11 Nu/Re**0.7*Pr*0.4) #######################################
# Impinging Jet: H/D=2, Re=23000
# Nusselt Number Data
# Expts. of Baughn et al (1992)
#  R/D        Nu/(Re**0.7)

position_Nu_exp_adim, Nu_exp_adim, position_Nu_exp_dim, Nu_exp_dim = lecture_exp('ij2lr-nuss.dat', D, Re**0.7)

# Fluent Inlet 0.04
position_eps1_heat, heat_eps1,position_eps1_heat_adim, heat_eps1_adim = lecture_simu('eps_0.04_Q.xy', 0, 1/D, 0, 1)
position_Nu_dim_eps1, heat_eps1 = sort(position_eps1_heat, heat_eps1) 
position_Nu_adim_eps1 = position_Nu_dim_eps1/D

h_eps1 = heat_eps1/DeltaT
Nu_eps1 = h_eps1*D/lambda_air

# Fluent Inlet 0.004
position_eps2_heat, heat_eps2,position_eps2_heat_adim, heat_eps2_adim = lecture_simu('eps_0.004_Q.xy', 0, 1/D, 0, 1)
position_Nu_dim_eps2, heat_eps2 = sort(position_eps2_heat, heat_eps2)
position_Nu_adim_eps2 = position_Nu_dim_eps2/D

h_eps2 = heat_eps2/DeltaT
Nu_eps2 = h_eps2*D/lambda_air

# Fluent Inlet 0.00004
position_eps3_heat, heat_eps3,position_eps3_heat_adim, heat_eps3_adim = lecture_simu('eps_0.00004_Q.xy', 0, 1/D, 0, 1)
position_Nu_dim_eps3, heat_eps3 = sort(position_eps3_heat, heat_eps3)
position_Nu_adim_eps3 = position_Nu_dim_eps3/D

h_eps3 = heat_eps3/DeltaT
Nu_eps3 = h_eps3*D/lambda_air


plt.figure(6)
plt.plot(position_Nu_exp_adim, Nu_exp_adim, label="Expérimental")
plt.plot(position_Nu_adim_eps1[:125] ,Nu_eps1[:125]/(Re**0.7), label="ε = 0.04 m²/s³")
plt.plot(position_Nu_adim_eps2[:125] ,Nu_eps2[:125]/(Re**0.7), label="ε = 0.004 m²/s³")
plt.plot(position_Nu_adim_eps3[:125] ,Nu_eps3[:125]/(Re**0.7), label="ε = 0.00004 m²/s³")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.legend()
plt.savefig("eps_nu_adim.png")

#############################################################
plt.show()


