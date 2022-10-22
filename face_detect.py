import cv2 as cv

# * Leer Imagen

img = cv.imread('images/group2.jpg')
cv.imshow('Img', img)

# * Filtro Escala de Grises

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier('cascades/frontalfaces.xml')
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.3, minNeighbors=1)

print(faces_rect)
print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
cv.imshow("Detected Faces", img)

cv.waitKey(0)