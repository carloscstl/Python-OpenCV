from http.client import CannotSendHeader
import cv2 as cv

#! Leer una imagen y mostrarla en ventana

img = cv.imread('cats.jpg')
cv.imshow('img', img)

#! Convertir a escala de grises

# gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
# cv.imshow('Gris',gray)

#! Blur

# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

#! Edge Cascade

# canny = cv.Canny(img,200,200)
# cv.imshow("Canny",canny)

#! Resize

# resized = cv.resize(img,(100,100))
# cv.imshow('resized',resized)

#! Crop an Image

# * crop = img[start_row:end_row,start_col:end_col]
# crop = img[75:320,270:470]
# cv.imshow("Cropped Image",crop)

#! Contour of an image

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(gray, 125, 175)
# cv.imshow("Edges", canny)

# contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')

#! Face Detection



cv.waitKey(0)
cv.destroyAllWindows()
