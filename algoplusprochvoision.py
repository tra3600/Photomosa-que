import numpy as np

def procheVoisin(A: np.ndarray, w: int, h: int) -> np.ndarray:
    """
    Redimensionne l'image A à la taille w × h en utilisant l'interpolation au plus proche voisin.
    
    Arguments :
    A -- Une image en niveaux de gris (tableau numpy à deux dimensions)
    w -- La nouvelle largeur de l'image (en pixels)
    h -- La nouvelle hauteur de l'image (en pixels)
    
    Retourne :
    Une nouvelle image redimensionnée (tableau numpy à deux dimensions)
    """
    H, W = A.shape
    a = np.zeros((h, w), dtype=np.uint8)
    
    for i in range(h):
        for j in range(w):
            x = int(i * H / h)
            y = int(j * W / w)
            a[i, j] = A[x, y]
    
    return a

# Exemple d'utilisation
A = np.array([[85, 0, 127, 170, 85, 150],
              [119, 102, 102, 123, 81, 170],
              [255, 170, 90, 112, 63, 97],
              [171, 212, 225, 186, 162, 171]], dtype=np.uint8)

w, h = 3, 2
a = procheVoisin(A, w, h)
print(a)