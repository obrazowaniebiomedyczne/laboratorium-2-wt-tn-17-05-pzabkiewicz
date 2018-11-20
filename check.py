from solution import *
import cv2
from obpng import read_png, write_png


print("- Ocena dostateczna")
renew_pictures()

print("- Ocena dobra")
image = cv2.imread("figures/crushed.png", 0)
erosion = own_simple_erosion(image)
cv2.imwrite("results/own_simple_erosion.png", erosion)


print("- Ocena bardzo dobra")
image = cv2.imread("figures/crushed.png", 0)
kernel = np.array([[0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0]])
erosion = own_erosion(image, kernel)
cv2.imwrite("results/own_erosion.png", erosion)

