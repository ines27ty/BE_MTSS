import numpy as np
import matplotlib.pyplot as plt
import os 

# Création de données
# Impinging Jet: H/D=2, Re=23000
# Nusselt Number Data
# Expts. of Baughn et al (1992)
#  R/D        Nu/(Re**0.7)

# Lire les lignes du fichier
filename = "ij2lr-nuss.dat"

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

# Initialiser des listes pour les positions et des nombres de Nusselt
# position = R/D
# Nu_adim = Nu/(Re**0.7)
position_adim_1 = []
Nu_exp = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_1.append(float(values[0]))
    Nu_exp.append(float(values[1]))

# Tracer Nu_adim en fonction de position_adim
plt.figure(1)
plt.plot(position_adim_1, Nu_exp, 'o-', label="expérimental")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("lr-nuss-exp.png")

# Position" "Total Surface Heat Flux")

# Lire les lignes du fichier
filename = "surface_total_heat_flux_ines.xy"

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

# Initialiser des listes pour les positions et pressions
position_ines = []
surface_heat_ines = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    values = line.split('\t')  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_ines.append(float(values[0]))
    surface_heat_ines.append(float(values[1]))


Delta_T = 200
lambda_air = 0.0242
D = 0.026
Re = 23000

# Variables

# Calculs 
h_ines = [surface_heat_ines[i]/((Delta_T)) for i in range(len(surface_heat_ines))] 
Nu_simu_ines = [h_ines[i]*D/lambda_air for i in range(len(h_ines))]
Nu_simu_adim_ines = [Nu_simu_ines[i]/(Re**0.7) for i in range(len(Nu_simu_ines))]

position_adim_ines = [position_ines[i]/D for i in range(len(position_ines))]


# Lire les lignes du fichier
filename = "surface_total_heat_flux_outflow.xy"

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

# Initialiser des listes pour les positions et pressions
position_hugo = []
surface_heat_hugo = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    values = line.split('\t')  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_hugo.append(float(values[0]))
    surface_heat_hugo.append(float(values[1]))


Delta_T = 200
lambda_air = 0.0242
D = 0.026
Re = 23000

# Variables

# Calculs 
h_hugo = [surface_heat_hugo[i]/((Delta_T)) for i in range(len(surface_heat_hugo))] 
Nu_simu_hugo = [h_hugo[i]*D/lambda_air for i in range(len(h_hugo))]
Nu_simu_adim_hugo = [Nu_simu_hugo[i]/(Re**0.7) for i in range(len(Nu_simu_hugo))]

position_adim_hugo = [position_hugo[i]/D for i in range(len(position_hugo))]


plt.figure(0)
plt.plot(position_adim_1, Nu_exp, 'o-', label="expérimental")
plt.plot(position_adim_ines, Nu_simu_adim_ines, 'o-', label="ines")
plt.plot(position_adim_hugo, Nu_simu_adim_hugo, 'o-', label="hugo")
plt.xlabel("Position R/D")
plt.ylabel(" Nu/(Re**0.7)")
plt.title("Profil de Nu adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.legend()
plt.savefig("lr-nuss-simu-nous.png")


#turbulent kinetic energy 0.0002535
#turbulent dissipation rate 0.0004567