import numpy as np

pixel_blanc = np.array([255, 255, 255], dtype=np.uint8)

a = np.uint8(230)
b = np.uint8(240)

def gris(p: np.ndarray) -> np.uint8:
    """
    Calcule le niveau de gris correspondant au pixel p.
    
    Arguments :
    p -- Un tableau numpy de type np.uint8 avec trois éléments représentant les composantes RGB.
    
    Retourne :
    Un entier np.uint8 représentant le niveau de gris.
    """
    # Calculer la moyenne des composantes RGB et la convertir en uint8
    niveau_de_gris = np.mean(p).astype(np.uint8)
    return niveau_de_gris

# Exemple d'utilisation
pixel = np.array([100, 150, 200], dtype=np.uint8)
niveau_gris = gris(pixel)
print(f"Niveau de gris pour le pixel {pixel} : {niveau_gris}")