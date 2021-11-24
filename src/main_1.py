import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import tensorflow.keras
import serial
import time

arduino = serial.Serial('com8', 9600)

# Load the model
model = load_model('keras_model.h5')

#웹캠 임포트
#capture = cv2.VideoCapture(0)
capture=cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.open(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)


#웹캠 이미지 처리
def preprocessing(frame):
    size=(224,224)
    frame_resized=cv2.resize(frame,size,interpolation=cv2.INTER_AREA)
    frame_nomalized=(frame_resized.astype(np.float32)/127.0)-1
    frame_reshaped=frame_nomalized.reshape((1,224,224,3))
    return frame_reshaped

#예측
def predict(frame):
    prediction = model.predict(frame)
    return prediction


while True:
    ret, frame = capture.read()
    detection="None"
    detection_Bottle=0
    detection_Can=0
    if cv2.waitKey(100)>0:
        break

############################################################################


    preprocessed=preprocessing(frame)
    prediciton = predict(preprocessed)

    
    #prediction[0,0] == Can
    #prediction[0,1] == Bottle
    #prediction[0,2] == Bg
    
    
    if (prediciton[0,0] <prediciton[0,2] and prediciton[0,1] <prediciton[0,2]):
        print("Bg")
    elif(prediciton[0, 0] < prediciton[0, 1] and prediciton[0, 2] < prediciton[0, 1]):
        detection = "Bottle"
    else:
        detection = "Can"


    print(detection)

###################################################################

    if detection == "Bottle":
        var = '1'
        var = var.encode('utf-8')
        arduino.write(var)
        time.sleep(9)
    elif detection == "Can":
        var = '0'
        var = var.encode('utf-8')
        arduino.write(var)
        time.sleep(9)

    cv2.imshow("VideoFrame",frame)

