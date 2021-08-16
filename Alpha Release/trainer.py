#imports needed libaries
import cv2
import numpy as np
from PIL import Image
import os
#video capture set as cam with set width and hieght
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
#face_detector set as the face default template
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person enter a face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
#declares count which counts the number of images taken
count = 0
#loop until break by using ESC or 30 images are taken
while(True):
    #ret and img is set to what is read from cam variable
    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically ONLY USE IF NEEDED!!!
    #sets gray as grey colour from cv2 lib
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detects faces from greyscale images
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    #for location of faces
    for (x,y,w,h) in faces:
	#makes rectangle around face
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
	#adds 1 to cound
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
	#shows image
        cv2.imshow('image', img)
   #checks if ESC is used
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
#ends cam and closes cv2 windows
cam.release()
cv2.destroyAllWindows()

# Path for face image database
path = 'dataset'
#creates face recognizer 
recognizer = cv2.face.LBPHFaceRecognizer_create()
#creates detector from template
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    #for each image in the dataset folder
    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
	#id is after the "." in img name
        id = int(os.path.split(imagePath)[-1].split(".")[1])
	#the face is detected from the image
        faces = detector.detectMultiScale(img_numpy)
	#for dimensions in face
        for (x,y,w,h) in faces:
	    #appends img to samples
            faceSamples.append(img_numpy[y:y+h,x:x+w])
	    #append id to ids
            ids.append(id)
    #returns samples and ids
    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
#gets images and labels from dataset
faces,ids = getImagesAndLabels(path)
#makes a trainer model for the faces with Ids
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.save('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
