import cv2
#define classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#reading image
#img = cv2.imread('admin.jpg')
cap = cv2.VideoCapture('Megamind.avi')
#reading video for continuous face detection

while cap.isOpened() :
   ret, img = cap.read()
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting image frames to gray
   faces = face_cascade.detectMultiScale(gray, 1.1, 4)
   for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w] #face from gray scale
        roi_color = img[y:y + h, x:x + w] #colored face scale region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 5)

   cv2.imshow('img', img)
   if cv2.waitKey(1) & 0XFF  == ord('q'):
        break

cap.release()