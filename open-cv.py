import cv2

face_haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("person.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)
cv2.waitKey()
faces = face_hear_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h),(255,0, 0),5)

    cv2.imshow("Detected Faces", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


