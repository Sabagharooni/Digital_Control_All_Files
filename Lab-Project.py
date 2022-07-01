import serial 
import getch
serialport = serial.Serial("/dev/ttyS0")
serialport.baudrate = 115200
while(True):
    x = getch.getch().lower() #Lower case letters are also accepted
    if x=='q' :               #Come out of loop by pressing q
        break
    elif x=='w':
        cmd = "100+10015+00"  #Go Up
    elif x=='s':
        cmd = "-100-10015+00" #Go down
    elif x=='d':
        cmd = "050-05015+00"  #Go right  
    elif x=='a':
        cmd = "-050+05015+00" #Go left
    else:
        cmd="000+00015+00"    # if any other character is pressed do nothing
