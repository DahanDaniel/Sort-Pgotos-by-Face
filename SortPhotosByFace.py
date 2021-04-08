#Sort pictures from party by person
import cv2
import face_recognition
import os
import shutil

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

directory = 'C:\Daniel\TestDir\\'

outputDir = 'C:\Daniel\Output\\'

Encriptions = []
People = {}

i = 1
j = 0

#Main
for filename in os.listdir(directory):
    if filename.endswith(".JPG"):
        path = directory + filename
        img = cv2.imread(path, 1)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_img, 1.1, 4)
        for (x,y,w,h) in faces:
            present = False
            # if w*h < 10000: #experimental result
            #     print('too small %d' % i)
            #     i += 1
            #     continue
            
            face1 = img[y:y+h, x:x+w].copy()
            if len(face_recognition.face_encodings(face1)):
                encode = face_recognition.face_encodings(face1)[0]
                for e in range(0,len(Encriptions)):
                    compare = face_recognition.compare_faces([Encriptions[e]],encode)
                    if compare[0]:
                        present = True
                        end = str(People[e])
                        location = (outputDir + end)
                        shutil.copy(path,location)
                        continue
                if not present:
                    cv2.imshow('face',face1)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    name = input('Who is this?')
                    if People.get(str(name)) != 0:
                        k = 1
                        name += str(k)
                        k += 1
                    People[j] = name
                    Encriptions.append(encode)
                    temp = (outputDir + name)
                    os.mkdir(temp)
                    shutil.copy(path,temp)
                    j += 1
    else:
        continue