#imports libaries
import cv2
import numpy as np
import os 
#creates recognizer and has it read trainer model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
#loads in deafult face template
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
#sets font
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids e.g.(Sami: id=1)
names = ['None', 'Sami', 'Greg'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
#runs until ESC is pressed
while True:
    #ret and img have image from  cam
    ret, img =cam.read()
    
    #defines what colour grey is
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #sets face requirements
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    #for dimentions in faces
    for(x,y,w,h) in faces:
	#draw rectangle around face
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
	#confidence equals the prediction functions output
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
	    #id equals name predicted person
            id = names[id]
	    #stores confidence percentage
            confidence = "  {0}%".format(round(100 - confidence))
	    #stores predicted user in user.txt so other programs can also know the user
	    f = open("user.txt", "w")
            f.write(str(id))
            f.close()
	#prediction couldn't be made
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        #positioning and colours of name and percentage text
        cv2.putText(img, str(id), (x+5,y-5), 6, 1, (255,255,255), 3)
        cv2.putText(img, str(confidence), (x-30,y+h+25), font, 1, (255,255,0), 2)  
    #shows current image
    cv2.imshow('camera',img) 
    #checks if user presses ESC, if so closes program
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
#closes camera and windows
cam.release()
cv2.destroyAllWindows()
© 2021 GitHub, Inc.
