import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = 'QuRT1OV_7skAAAAAAAAAARKSegLECoAIwSAJLS6PrRqCk6J5vbFO_w1b3Cl6clSx'
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, file_to):
        dbx.files_upload(f.read(), file_to, made = dropbox.files.WriteMode.overWrites)
        print("files uploaded")
        
def main():
    while(True):
        if ((time.time()- start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main()