import numpy as np
import cv2


# Zadanie na ocenę dostateczną
def renew_pictures():

    kernel = np.ones((7,7)).astype(np.uint8)
    
    crushed_img = cv2.imread('figures/crushed.png', 0)
    crushedToResult = cv2.morphologyEx(crushed_img, cv2.MORPH_OPEN, kernel)
    write_png(crushedToResult, 'results/crushedToResult.png')
    
    crushed2_img = cv2.imread('figures/crushed2.png', 0)
    kernel = np.ones((3,3)).astype(np.uint8)
    crushedToResult2 = cv2.morphologyEx(crushed2_img, cv2.MORPH_OPEN, kernel)
    crushedToResult2 = cv2.morphologyEx(crushedToResult2, cv2.MORPH_CLOSE, kernel)
    write_png(crushedToResult2, 'results/crushedToResult2.png')
    
    crushed3_img = cv2.imread('figures/crushed3.png', 0)
    kernel = np.ones((3,3)).astype(np.uint8)
    crushedToResult3 = cv2.morphologyEx(crushed3_img, cv2.MORPH_OPEN, kernel)
    crushedToResult3 = cv2.morphologyEx(crushedToResult3, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((7,7)).astype(np.uint8)
    crushedToResult3 = cv2.morphologyEx(crushedToResult3, cv2.MORPH_OPEN, kernel)
    write_png(crushedToResult3, 'results/crushedToResult3.png')
    
    crushed4_img = cv2.imread('figures/crushed4.png', 0)
    kernel = np.ones((3,3)).astype(np.uint8)
    crushedToResult4 = cv2.morphologyEx(crushed4_img, cv2.MORPH_OPEN, kernel) 
    crushedToResult4 = cv2.morphologyEx(crushedToResult4, cv2.MORPH_CLOSE, kernel) 
    kernel = np.ones((7,7)).astype(np.uint8)
    crushedToResult4 = cv2.morphologyEx(crushedToResult4, cv2.MORPH_OPEN, kernel)      
    write_png(crushedToResult4, 'results/crushedToResult4.png')

# Uwaga: brak obslugi bledu w przypadku jadra o wymiarach parzystych
# Zalozenie: algorytm obsluguje poprawnie tylko jadra o wymiarach nieparzystych
# Metody pomocnicze
# Metoda tworzy ramke o odpowiedniej szerokosci wokol macierzy reprezentujacej obraz
def copy_image_with_empty_border(img, struct):
    border_size = struct.shape[0] // 2
    image_with_border = np.zeros((img.shape[0] + 2 * border_size, img.shape[1] + 2 * border_size)).astype(np.uint8)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            image_with_border[i+border_size, j+border_size] = img[i,j]
        
    return image_with_border 

# Metoda analizuje dany piksel i jego sasiedztwo
# Na podstawie tego jest okreslane czy ma nastapic erozja tego piksela lub nie
def analyze_pixel_neighbourhood(pixel_with_neighbourhood, struct):
    new_struct = struct.dot(255)
    
    for i in range(new_struct.shape[0]):
        for j in range(new_struct.shape[1]):
            if new_struct[i,j] == 255 and pixel_with_neighbourhood[i,j] == 0:
                return True
    return False

# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    # predefined kernel
    kernel = np.array([[0,1,0], [1,1,1], [0,1,0]], dtype=image.dtype)
    
    # new matrix = original image surrounded by border (size of border = kernel // 2)
    image_with_border = copy_image_with_empty_border(image, kernel)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            
            frag = image_with_border[0+i:kernel.shape[0]+i, 0+j:kernel.shape[1]+j]
            is_erosion = analyze_pixel_neighbourhood(frag, kernel)
            
            if is_erosion:
                new_image[i,j] = 0
            else:
                new_image[i,j] = image[i,j]

    return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    image_with_border = copy_image_with_empty_border(image, kernel)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            
            frag = image_with_border[0+i:kernel.shape[0]+i, 0+j:kernel.shape[1]+j]
            is_erosion = analyze_pixel_neighbourhood(frag, kernel)
            
            if is_erosion:
                new_image[i,j] = 0
            else:
                new_image[i,j] = image[i,j]

    return new_image
