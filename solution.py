import numpy as np


# Zadanie na ocenę dostateczną
def renew_pictures():

    # ---------------
    # Do uzupełnienia
    # ---------------

    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image
