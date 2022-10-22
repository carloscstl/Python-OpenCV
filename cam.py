import cv2 as cv

cap = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('cascades/frontalfaces.xml')

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    auxFrame = frame.copy()
    gray = cv.cvtColor(auxFrame,cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(
    frame, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        cv.putText(frame,'Hola Mundo',(x,y-10),2,1,(0,255,255),2,cv.LINE_AA)
    cv.imshow("Video", frame)
    cv.imshow("Grey", gray)

    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
