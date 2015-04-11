import picamera
import time

date = time.strftime("%d-%m-%Y_%H:%M:%S")
camera = picamera.PiCamera()

camera.capture('project/'+date+'.jpg',resize=(320,240))

