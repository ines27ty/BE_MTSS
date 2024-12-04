import os
import csv
import numpy as np
import pandas as pd

def lecture_exp(filename, coeff_1, coeff_2):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

    x = []
    y = []

    with open(filename, 'r') as fichier:
        lines = fichier.readlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if not line:  # Skip empty lines
            continue

        # Split the line into values
        values = line.split()
        if len(values) < 2:  # Ensure at least two values are present
            raise ValueError(f"Ligne invalide : {line}")
        
        try:
            x_value = float(values[0])
            y_value = float(values[1])
        except ValueError:
            raise ValueError(f"Valeurs non numériques détectées dans la ligne : {line}")

        x.append(x_value)
        y.append(y_value)

    # Convert to numpy arrays and apply coefficients
    x = np.array(x)
    y = np.array(y)
    x_dim = x * coeff_1
    y_dim = y * coeff_2

    return x, y, x_dim, y_dim

def lecture_simu(filename, add_x,factor_x, add_y, factor_y) :
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

    """
    Lit un fichier contenant deux colonnes de données numériques.
    
    :param fichier: Chemin vers le fichier à lire.
    :return: Deux listes, x et y, contenant les valeurs des colonnes.
    """
    x = []
    y = []
    
    with open(filename, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()  # Retirer les espaces ou caractères inutiles
            if not ligne:  # Ignorer les lignes vides
                continue
            
            valeurs = ligne.split()  # Diviser la ligne en colonnes
            if len(valeurs) >= 2:  # Vérifier qu'il y a au moins deux colonnes
                try:
                    x.append(float(valeurs[0]))  # Convertir en float et ajouter à x
                    y.append(float(valeurs[1]))  # Convertir en float et ajouter à y
                except ValueError:
                    print(f"Erreur : Ligne ignorée à cause de valeurs non numériques -> {ligne}")
    

    # Convert to numpy arrays and apply coefficients
    x = np.array(x)+add_x
    y = np.array(y)
    
    x_adim = (x)*factor_x
    y_adim = (y)*factor_y

    return x, y, x_adim, y_adim

def sort(x, y):
    data = {'x': x, 'y': y}
    df = pd.DataFrame(data)
    df_sorted = df.sort_values(by="x").reset_index(drop=True)
    sort_x = df_sorted['x']
    sort_y = df_sorted['y']
    return sort_x, sort_y



def lecture_starccm_double(filename, add_x1, factor_x1, add_y1, factor_y1, add_x2, factor_x2, add_y2, factor_y2):
    # Vérifier si le fichier existe
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

    x1, y1, x2, y2 = [], [], [], []

    # Lecture du fichier CSV
    with open(filename, 'r') as fichier:
        reader = csv.reader(fichier)  # Utilise le module CSV pour lire les lignes
        for row in reader:
            if not row:  # Ignorer les lignes vides
                continue
            try:
                # Convertir les valeurs en flottants
                x1.append(float(row[0]))
                y1.append(float(row[1]))
                x2.append(float(row[2]))
                y2.append(float(row[3]))

            except ValueError as e:
                raise ValueError(f"Valeurs non numériques détectées dans la ligne : {row}") from e

    # Convertir les listes en tableaux numpy
    x1 = np.array(x1) + add_x1
    y1 = np.array(y1)
    x1_adim = x1 * factor_x1
    y1_adim = y1 * factor_y1

    x2 = np.array(x2) + add_x2
    y2 = np.array(y2)
    x2_adim = x2 * factor_x2
    y2_adim = y2 * factor_y2

    return x1, y1, x1_adim, y1_adim, x2, y2, x2_adim, y2_adim




def lecture_starccm_single(filename, add_x1, factor_x1, add_y1, factor_y1):
    # Vérifier si le fichier existe
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

    x1, y1= [], []

    # Lecture du fichier CSV
    with open(filename, 'r') as fichier:
        reader = csv.reader(fichier)  # Utilise le module CSV pour lire les lignes
        for row in reader:
            if not row:  # Ignorer les lignes vides
                continue
            try:
                # Convertir les valeurs en flottants
                x1.append(float(row[0]))
                y1.append(float(row[1]))

            except ValueError as e:
                raise ValueError(f"Valeurs non numériques détectées dans la ligne : {row}") from e

    # Convertir les listes en tableaux numpy
    x1 = np.array(x1) + add_x1
    y1 = np.array(y1)
    x1_adim = x1 * factor_x1
    y1_adim = y1 * factor_y1

    return x1, y1, x1_adim, y1_adim


def lire_donnees(fichier):
    """
    Lit un fichier contenant deux colonnes de données numériques.
    
    :param fichier: Chemin vers le fichier à lire.
    :return: Deux listes, x et y, contenant les valeurs des colonnes.
    """
    x = []
    y = []
    
    with open(fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()  # Retirer les espaces ou caractères inutiles
            if not ligne:  # Ignorer les lignes vides
                continue
            
            valeurs = ligne.split()  # Diviser la ligne en colonnes
            if len(valeurs) >= 2:  # Vérifier qu'il y a au moins deux colonnes
                try:
                    x.append(float(valeurs[0]))  # Convertir en float et ajouter à x
                    y.append(float(valeurs[1]))  # Convertir en float et ajouter à y
                except ValueError:
                    print(f"Erreur : Ligne ignorée à cause de valeurs non numériques -> {ligne}")
    
    return x, y