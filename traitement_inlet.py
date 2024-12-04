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

# Inlet 1
position_mu_inlet1_dim_10, u_mean_inlet1_dim_10, position_mu_inlet1_adim_10 , u_mean_inlet1_adim_10 = lecture_simu('umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_inlet1_dim_30, u_mean_inlet1_dim_30, position_mu_inlet1_adim_30 , u_mean_inlet1_adim_30 = lecture_simu('umean_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_inlet1_adim_10, u_mean_inlet1_adim_10 = sort(position_mu_inlet1_adim_10, u_mean_inlet1_adim_10)
position_mu_inlet1_adim_30, u_mean_inlet1_adim_30 = sort(position_mu_inlet1_adim_30, u_mean_inlet1_adim_30)

# Inlet 2
position_mu_inlet2_dim_10, u_mean_inlet2_dim_10, position_mu_inlet2_adim_10 , u_mean_inlet2_adim_10 = lecture_simu('inlet2_umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_inlet2_dim_30, u_mean_inlet2_dim_30, position_mu_inlet2_adim_30 , u_mean_inlet2_adim_30 = lecture_simu('inlet2_umean_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_inlet2_adim_10, u_mean_inlet2_adim_10 = sort(position_mu_inlet2_adim_10, u_mean_inlet2_adim_10)
position_mu_inlet2_adim_30, u_mean_inlet2_adim_30 = sort(position_mu_inlet2_adim_30, u_mean_inlet2_adim_30)

# Inlet 3 
position_mu_inlet3_dim_10, u_mean_inlet3_dim_10, position_mu_inlet3_adim_10 , u_mean_inlet3_adim_10 = lecture_simu('inlet3_umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_inlet3_dim_30, u_mean_inlet3_dim_30, position_mu_inlet3_adim_30 , u_mean_inlet3_adim_30 = lecture_simu('inlet3_umean_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_inlet3_adim_10, u_mean_inlet3_adim_10 = sort(position_mu_inlet3_adim_10, u_mean_inlet3_adim_10)
position_mu_inlet3_adim_30, u_mean_inlet3_adim_30 = sort(position_mu_inlet3_adim_30, u_mean_inlet3_adim_30)

# Inlet 4
position_mu_inlet4_dim_10, u_mean_inlet4_dim_10, position_mu_inlet4_adim_10 , u_mean_inlet4_adim_10 = lecture_simu('inlet4_umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_mu_inlet4_dim_30, u_mean_inlet4_dim_30, position_mu_inlet4_adim_30 , u_mean_inlet4_adim_30 = lecture_simu('inlet4_umean_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_mu_inlet4_adim_10, u_mean_inlet4_adim_10 = sort(position_mu_inlet4_adim_10, u_mean_inlet4_adim_10)
position_mu_inlet4_adim_30, u_mean_inlet4_adim_30 = sort(position_mu_inlet4_adim_30, u_mean_inlet4_adim_30)


plt.figure(2)
plt.plot(position_mu_adim_10, u_mean_adim_10, label="r/D = 1.0 exp")
plt.plot(position_mu_inlet1_adim_10[:70], u_mean_inlet1_adim_10[:70], label="r/D = 1.0 Fluent Inlet 1")
plt.plot(position_mu_inlet2_adim_10[:70], u_mean_inlet2_adim_10[:70], label="r/D = 1.0 Fluent Inlet 2")
plt.plot(position_mu_inlet3_adim_10[:70], u_mean_inlet3_adim_10[:70], label="r/D = 1.0 Fluent Inlet 3")
plt.plot(position_mu_inlet4_adim_10[:70], u_mean_inlet4_adim_10[:70], label="r/D = 1.0 Fluent Inlet 4")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("inlet-u_mean_adim_1D.png")


plt.figure(3)
plt.plot(position_mu_adim_30, u_mean_adim_30, label="r/D = 3.0 exp")
plt.plot(position_mu_inlet1_adim_30[:70], u_mean_inlet1_adim_30[:70], label="r/D = 3.0 Fluent Inlet 1")
plt.plot(position_mu_inlet2_adim_30[:70], u_mean_inlet2_adim_30[:70], label="r/D = 3.0 Fluent Inlet 2")
plt.plot(position_mu_inlet3_adim_30[:70], u_mean_inlet3_adim_30[:70], label="r/D = 3.0 Fluent Inlet 3")
plt.plot(position_mu_inlet4_adim_30[:70], u_mean_inlet4_adim_30[:70], label="r/D = 3.0 Fluent Inlet 4")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Vitesse moyenne adimensionnalisé")
plt.legend()
plt.grid()
plt.savefig("inlet-u_mean_adim_3D.png")

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

# Fluent Inlet 1
position_k_inlet1_dim_10, k_inlet1_dim_10, position_k_inlet1_adim_10 , k_inlet1_adim_10 = lecture_simu('k_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_inlet1_dim_30, k_inlet1_dim_30, position_k_inlet1_adim_30 , k_inlet1_adim_30 = lecture_simu('k_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_inlet1_dim_10, k_inlet1_dim_10 = sort(position_k_inlet1_dim_10, k_inlet1_dim_10)
position_k_inlet1_dim_30, k_inlet1_dim_30 = sort(position_k_inlet1_dim_30, k_inlet1_dim_30)

# Fluent Inlet 2
position_k_inlet2_dim_10, k_inlet2_dim_10, position_k_inlet2_adim_10 , k_inlet2_adim_10 = lecture_simu('inlet2_k_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_inlet2_dim_30, k_inlet2_dim_30, position_k_inlet2_adim_30 , k_inlet2_adim_30 = lecture_simu('inlet2_k_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_inlet2_dim_10, k_inlet2_dim_10 = sort(position_k_inlet2_dim_10, k_inlet2_dim_10)
position_k_inlet2_dim_30, k_inlet2_dim_30 = sort(position_k_inlet2_dim_30, k_inlet2_dim_30)

# Fluent Inlet 3
position_k_inlet3_dim_10, k_inlet3_dim_10, position_k_inlet3_adim_10 , k_inlet3_adim_10 = lecture_simu('inlet3_k_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_inlet3_dim_30, k_inlet3_dim_30, position_k_inlet3_adim_30 , k_inlet3_adim_30 = lecture_simu('inlet3_k_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_inlet3_dim_10, k_inlet3_dim_10 = sort(position_k_inlet3_dim_10, k_inlet3_dim_10)
position_k_inlet3_dim_30, k_inlet3_dim_30 = sort(position_k_inlet3_dim_30, k_inlet3_dim_30)

# Fluent Inlet 4
position_k_inlet4_dim_10, k_inlet4_dim_10, position_k_inlet4_adim_10 , k_inlet4_adim_10 = lecture_simu('inlet4_k_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)
position_k_inlet4_dim_30, k_inlet4_dim_30, position_k_inlet4_adim_30 , k_inlet4_adim_30 = lecture_simu('inlet4_k_r_3.xy', 0.208, 1/D, 0, 1/u_bulk)

position_k_inlet4_dim_10, k_inlet4_dim_10 = sort(position_k_inlet4_dim_10, k_inlet4_dim_10)
position_k_inlet4_dim_30, k_inlet4_dim_30 = sort(position_k_inlet4_dim_30, k_inlet4_dim_30)


plt.figure(7)
plt.plot(position_inter_10/D, np.sqrt(k_dim_10)/u_bulk, label="r/D = 1.0")
plt.plot(position_k_inlet1_dim_10[:70]/D, np.sqrt(k_inlet1_dim_10[:70])/u_bulk, label="r/D = 1.0 Fluent Inlet 1")
plt.plot(position_k_inlet2_dim_10[:70]/D, np.sqrt(k_inlet2_dim_10[:70])/u_bulk, label="r/D = 1.0 Fluent Inlet 2")
plt.plot(position_k_inlet3_dim_10[:70]/D, np.sqrt(k_inlet3_dim_10[:70])/u_bulk, label="r/D = 1.0 Fluent Inlet 3")
plt.plot(position_k_inlet4_dim_10[:70]/D, np.sqrt(k_inlet4_dim_10[:70])/u_bulk, label="r/D = 1.0 Fluent Inlet 4")
plt.xlabel("Position y/D")
plt.ylabel("k**0.5/UBULK")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente adimensionné")
plt.legend()
plt.savefig("inlet_k_adim_exp_1d.png")

plt.figure(5)
plt.plot(position_inter_30/D, np.sqrt(k_dim_30)/u_bulk, label="r/D = 3.0")
plt.plot(position_k_inlet1_dim_30[:70]/D, np.sqrt(k_inlet1_dim_30[:70])/u_bulk, label="r/D = 3.0 Fluent Inlet 1")
plt.plot(position_k_inlet2_dim_30[:70]/D, np.sqrt(k_inlet2_dim_30[:70])/u_bulk, label="r/D = 3.0 Fluent Inlet 2")
plt.plot(position_k_inlet3_dim_30[:70]/D, np.sqrt(k_inlet3_dim_30[:70])/u_bulk, label="r/D = 3.0 Fluent Inlet 3")
plt.plot(position_k_inlet4_dim_30[:70]/D, np.sqrt(k_inlet4_dim_30[:70])/u_bulk, label="r/D = 3.0 Fluent Inlet 4")
plt.xlabel("Position y/D")
plt.ylabel("k**0.5/UBULK")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente adimensionné")
plt.legend()
plt.savefig("inlet_k_adim_exp_3d.png")


####################### Nusselt (figure 11 Nu/Re**0.7*Pr*0.4) #######################################
# Impinging Jet: H/D=2, Re=23000
# Nusselt Number Data
# Expts. of Baughn et al (1992)
#  R/D        Nu/(Re**0.7)

position_Nu_exp_adim, Nu_exp_adim, position_Nu_exp_dim, Nu_exp_dim = lecture_exp('ij2lr-nuss.dat', D, Re**0.7)

# Fluent Inlet 1
position_inlet1_heat, heat_inlet1,position_inlet1_heat_adim, heat_inlet1_adim = lecture_simu('heat_flux.xy', 0, 1/D, 0, 1)
position_Nu_dim_inlet1, heat_inlet1 = sort(position_inlet1_heat, heat_inlet1) 
position_Nu_adim_inlet1 = position_Nu_dim_inlet1/D

h_inlet1 = heat_inlet1/DeltaT
Nu_inlet1 = h_inlet1*D/lambda_air

# Fluent Inlet 2
position_inlet2_heat, heat_inlet2,position_inlet2_heat_adim, heat_inlet2_adim = lecture_simu('inlet2_heat_flux.xy', 0, 1/D, 0, 1)
position_Nu_dim_inlet2, heat_inlet2 = sort(position_inlet2_heat, heat_inlet2)
position_Nu_adim_inlet2 = position_Nu_dim_inlet2/D

h_inlet2 = heat_inlet2/DeltaT
Nu_inlet2 = h_inlet2*D/lambda_air

# Fluent Inlet 3
position_inlet3_heat, heat_inlet3,position_inlet3_heat_adim, heat_inlet3_adim = lecture_simu('inlet3_heat_flux.xy', 0, 1/D, 0, 1)
position_Nu_dim_inlet3, heat_inlet3 = sort(position_inlet3_heat, heat_inlet3)
position_Nu_adim_inlet3 = position_Nu_dim_inlet3/D

h_inlet3 = heat_inlet3/DeltaT
Nu_inlet3 = h_inlet3*D/lambda_air

# Fluent Inlet 4
position_inlet4_heat, heat_inlet4,position_inlet4_heat_adim, heat_inlet4_adim = lecture_simu('inlet4_heat_flux.xy', 0, 1/D, 0, 1)
position_Nu_dim_inlet4, heat_inlet4 = sort(position_inlet4_heat, heat_inlet4)
position_Nu_adim_inlet4 = position_Nu_dim_inlet4/D

h_inlet4 = heat_inlet4/DeltaT
Nu_inlet4 = h_inlet4*D/lambda_air


plt.figure(6)
plt.plot(position_Nu_exp_adim, Nu_exp_adim, label="exp")
plt.plot(position_Nu_adim_inlet1[:125] ,Nu_inlet1[:125]/(Re**0.7), label="Fluent Inlet 1")
plt.plot(position_Nu_adim_inlet2[:125] ,Nu_inlet2[:125]/(Re**0.7), label="Fluent Inlet 2")
plt.plot(position_Nu_adim_inlet3[:125] ,Nu_inlet3[:125]/(Re**0.7), label="Fluent Inlet 3")
plt.plot(position_Nu_adim_inlet4[:125] ,Nu_inlet4[:125]/(Re**0.7), label="Fluent Inlet 4")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.legend()
plt.savefig("inlet_nu_adim.png")

#############################################################
plt.show()


