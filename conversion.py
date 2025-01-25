import numpy as np
import matplotlib.pyplot as plt

def conversion(a: np.ndarray) -> np.ndarray:
    """
    Convertit une image en couleurs en une image en niveaux de gris.
    
    Arguments :
    a -- Un tableau numpy à trois dimensions représentant une image en couleurs (hauteur, largeur, 3)
    
    Retourne :
    Un tableau numpy à deux dimensions représentant l'image en niveaux de gris (hauteur, largeur)
    """
    # Vérifier que l'image est bien en couleurs (trois composantes par pixel)
    assert a.shape[-1] == 3, "L'image doit avoir trois composantes par pixel (R, G, B)"
    
    # Calculer la moyenne des composantes RGB pour chaque pixel et convertir en uint8
    gris = np.mean(a, axis=2).astype(np.uint8)
    
    return gris

# Exemple d'utilisation
source = plt.imread("surfer.jpg")
gris_image = conversion(source)

# Affichage des images
plt.subplot(1, 2, 1)
plt.imshow(source)
plt.title("Image en couleurs")

plt.subplot(1, 2, 2)
plt.imshow(gris_image, cmap='gray')
plt.title("Image en niveaux de gris")

plt.show()