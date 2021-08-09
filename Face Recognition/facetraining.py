#imports needed libaries
import cv2
import numpy as np
from PIL import Image
import os

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
