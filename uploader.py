#!/usr/bin/python

from subprocess import call
import picamera
import time

date = time.strftime('%Y-%m-%d_%H:%M:%S')
camera = picamera.PiCamera()
camera.resolution=(320,240)
camera.capture('/home/pi/Dropbox-Uploader/project/'+date+'.jpg')

photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Dropbox-Uploader/project/"+date+".jpg " +date+ ".jpg"
call([photofile], shell=True)
hapus = "/home/pi/Dropbox-Uploader/delete.sh"
call([hapus], shell=True)

