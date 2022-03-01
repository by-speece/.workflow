# Universal Bright for DWM
# Only work with amd for this time
# By Aiden Speece - Szymon Galka
import os.path
import os
import sys

amd_path = '/sys/class/backlight/amdgpu_bl0/' 


#intel_gpu = os.path.isdir(intel_path) 
amd_gpu = os.path.isdir(amd_path)

def amd():
    amd_file = open("/sys/class/backlight/amdgpu_bl0/brightness")
    print("Current Brightness: ", int(amd_file.read())/2.55, "%")
    set_brightness = input("What Brightness Level [%] do you want: ")
    calc_set_brightness = int((int(set_brightness)) * 2.55)
    brightness_path = open('/sys/class/backlight/amdgpu_bl0/brightness', 'r+')
    brightness_path.write(str(calc_set_brightness))

def Main():
    if amd_gpu == True:
        amd()

    else:
        print("Device is not supported")


Main()


