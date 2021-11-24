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
    # 7번 연속 판정 시키고 더 많이 판정된 결과(캔/병)를 디텍션 값으로 어싸인

    preprocessed=preprocessing(frame)
    prediciton = predict(preprocessed)

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
#클래스 1이 else문









'''
2021/11/09
while True:
    ret, frame = capture.read()
    if cv2.waitKey(100)>0:
        break
    preprocessed=preprocessing(frame)
    prediciton = predict(preprocessed)
## cnt 판별
    if (prediciton[0,0] <prediciton[0,1]):
        print("Bottle")
        cv2.putText(frame,'Bottle',(0,25),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
    else:
        cv2.putText(frame,"Can",(0,25),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
        print("Can")
    cv2.imshow("VideoFrame",frame)
#클래스 1이 else문
'''



'''
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open('<IMAGE_PATH>')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array
# run the inference
prediction = model.predict(data)
print(prediction)
'''