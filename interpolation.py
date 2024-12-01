import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
def interpolate_files(file1_path, file2_path, output_file, num_points=500):
    """
    Interpole les données de deux fichiers pour qu'elles aient les mêmes abscisses.
    
    Parameters:
        file1_path (str): Chemin vers le premier fichier.
        file2_path (str): Chemin vers le second fichier.
        output_file (str): Chemin pour sauvegarder les données interpolées.
        num_points (int): Nombre de points communs pour l'interpolation.
    
    Returns:
        None: Sauvegarde un fichier CSV contenant les données interpolées.
    """
    # Charger les fichiers
    data1 = np.loadtxt(file1_path)
    data2 = np.loadtxt(file2_path)

    # Abscisses et ordonnées
    x1, y1 = data1[:, 0], data1[:, 1]
    x2, y2 = data2[:, 0], data2[:, 1]

    # Définir un ensemble commun d'abscisses (intersection ou étendue commune)
    x_common = np.linspace(max(min(x1), min(x2)), min(max(x1), max(x2)), num=num_points)

    # Interpolation
    interp1 = interp1d(x1, y1, kind='linear', fill_value="extrapolate")
    interp2 = interp1d(x2, y2, kind='linear', fill_value="extrapolate")

    y1_interp = interp1(x_common)
    y2_interp = interp2(x_common)

    # Sauvegarder les résultats
    interpolated_data = pd.DataFrame({
        'x': x_common,
        'y1': y1_interp,
        'y2': y2_interp
    })
    interpolated_data.to_csv(output_file, index=False)

    print(f"Fichier interpolé sauvegardé : {output_file}")

    # Tracer les résultats
    plt.figure(0)
    plt.plot(x1, y1, 'o-', label="Données 1")
    plt.plot(x_common, y1_interp, '-', label="Interpolé 1")
    plt.legend()

    plt.figure(1)
    plt.plot(x2, y2, 'o-', label="Données 2")
    plt.plot(x_common, y2_interp, '-', label="Interpolé 2")
    plt.legend()
    return x_common, y1_interp, y2_interp
    #plt.show()


def interpolate_lists(x1, y1, x2, y2, num_points=500):
    """
    Interpole les données de deux listes pour qu'elles aient les mêmes abscisses.

    Parameters:
        x1 (array-like): Abscisses du premier jeu de données.
        y1 (array-like): Ordonnées du premier jeu de données.
        x2 (array-like): Abscisses du second jeu de données.
        y2 (array-like): Ordonnées du second jeu de données.
        num_points (int): Nombre de points communs pour l'interpolation.

    Returns:
        x_common (np.ndarray): Abscisses communes interpolées.
        y1_interp (np.ndarray): Ordonnées interpolées pour le premier jeu de données.
        y2_interp (np.ndarray): Ordonnées interpolées pour le second jeu de données.
    """
    # Définir un ensemble commun d'abscisses (intersection ou étendue commune)
    x_common = np.linspace(max(min(x1), min(x2)), min(max(x1), max(x2)), num=num_points)

    # Interpolation
    interp1 = interp1d(x1, y1, kind='linear', fill_value="extrapolate")
    interp2 = interp1d(x2, y2, kind='linear', fill_value="extrapolate")

    y1_interp = interp1(x_common)
    y2_interp = interp2(x_common)

    # Tracer les résultats
    plt.figure(0)
    plt.plot(x1, y1, 'o-', label="Données 1 (originales)")
    plt.plot(x2, y2, 'o-', label="Données 2 (originales)")
    plt.plot(x_common, y1_interp, '-', label="Données 1 (interpolées)")
    plt.plot(x_common, y2_interp, '-', label="Données 2 (interpolées)")
    plt.legend()
    plt.title("Interpolation des données")
    plt.xlabel("Abscisse (x)")
    plt.ylabel("Ordonnée (y)")
    plt.grid(True)
    #plt.show()

    return x_common, y1_interp, y2_interp

