

import io
from picamera import PiCamera
import cv2
import numpy
import time
from picamera.array import PiRGBArray

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

def detectface():
    # allow the camera to warmup
    time.sleep(0.1)
    
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        #buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
        #image = cv2.imdecode(buff, 1)
        image = cv2.flip(image,0)
        image = cv2.flip(image,1)
        face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/my-awesome-project/faces.xml')
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        print "Found "+str(len(faces))+" face(s)"
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        

        # show the frame
        #cv2.imshow("Frame", image)
        #key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        #if key == ord("q"):
        #        break

        if len(faces) == 0:
            rarray = [len(faces)]
        else:
            rarray = [len(faces), x, y, w]

        return rarray
        #break



    #MR.DEBUGGER

    #Convert the picture into a numpy array
    #buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    #Now creates an OpenCV image
    #image = cv2.imdecode(buff, 1)

    #image = cv2.flip(image,0)
    #image = cv2.flip(image,1)

    #Load a cascade file for detecting faces
    #face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/OPENCV/faces.xml')

    #Convert to grayscale
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    #faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    #print "Found "+str(len(faces))+" face(s)"

    #Draw a rectangle around every found face
    #for (x,y,w,h) in faces:
    #    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

    #Save the result image
    #cv2.imwrite('result.jpg',image)
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    #if len(faces) == 0:
    #    rarray = [len(faces)]
    #else:
    #    rarray = [len(faces), x, y]

    #return rarray
    
    #camera.close()

#detectface()
