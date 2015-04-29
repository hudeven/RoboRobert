import webiopi
import subprocess
import os
import sys


GPIO = webiopi.GPIO
L1 = 27
L2 = 17
LS = 13

R1 = 4
R2 = 3
RS = 18

speed_value = 1.0
camera_pid = 0

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)

def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)

def left_back():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)

def right_back():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)


def set_speed(speed):
    GPIO.pulseRatio(LS, speed)
    GPIO.pulseRatio(RS, speed)

def speed_up():
    print "******* start speedup ********"
    speed_value += 0.1
    print "******* start set_speed ********"
    set_speed(speed_value)
    print speed_value

def speed_down():
    if speed_value - 0.1 >= 0:
        speed_value -= 0.1
    set_speed(speed_value)
    print speed_value

def go_forward():
    left_forward()
    right_forward()

def go_back():
    left_back()
    right_back()

def turn_left():
    left_back()
    right_forward()

def turn_right():
    left_forward()
    right_back()

def stop():
    left_stop()
    right_stop()

def open_camera():
    print "open camera"
    os.chdir("./mjpg_streamer")
    camera_pid = subprocess.call("./start.sh &", shell=True)
    os.chdir("..")
    print "end open camera"
    print camera_pid

def close_camera():
    print "close camera"
    print camera_pid
    os.kill(camera_pid, 9)
    #camera_pid.terminate()
    
GPIO.setFunction(LS, GPIO.PWM)
GPIO.setFunction(L1, GPIO.OUT)
GPIO.setFunction(L2, GPIO.OUT)

GPIO.setFunction(RS, GPIO.PWM)
GPIO.setFunction(R1, GPIO.OUT)
GPIO.setFunction(R2, GPIO.OUT)

set_speed(speed_value)
stop()

server = webiopi.Server(port=80,
			login='webiopi',
			password='raspberry')
server.addMacro(go_forward)
server.addMacro(go_back)
server.addMacro(turn_left)
server.addMacro(turn_right)
server.addMacro(stop)
server.addMacro(speed_up)
server.addMacro(speed_down)
server.addMacro(open_camera)
server.addMacro(close_camera)
webiopi.runLoop()
server.stop()


