import cv2

capture = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('WIN_20258702_11_42_11_Pro.jpg')

gray =(cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY))

cv2.waltkey()

faces=fear_hear_cascade.detectMultiScale(gray, 1,1,4)


for (x,y,w,b) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+b),(0,255,0),5)

    cv2.imshow("video",image)

    if k == 27:
        break

cv2.release()