import cv2


def resize():
    img = cv2.imread("D:/Gun-Detection-Cascade/negetiveImageSource/10.jpg", cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(img, (50, 50))
    cv2.imwrite('01.png', resized_image)


resize()