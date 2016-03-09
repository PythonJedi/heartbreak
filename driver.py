import serial

#===================GLOBALS===================
global_config =    {
            "yaw" :{"angle": 10.0, "delta" : 10.0, "axis": 1.0},
            "pitch":{"angle": 90.0, "delta" : 10.0, "axis": .5}
    }

#===================SerialConnection===================
print "Connecting to Arduino...."

ser = serial.Serial('/dev/ttyACM0', 9600)

print "Connected!"

#===================SerialConnection===================

#serin = ser.read()
#print serin


def kill_connection():
   ser.close()


#===================ControlStuff===================

def up(range = 90):
    setAngleServo1(global_config["pitch"]["angle"], range=range)

    if global_config["pitch"]["angle"] > 0 and global_config["pitch"]["angle"] < range:
        global_config["pitch"]["angle"]  =  global_config["pitch"]["angle"] +   global_config["pitch"]["delta"]*global_config["pitch"]["axis"]
    else:
        if abs(global_config["pitch"]["angle"] - range) < abs(global_config["pitch"]["angle"]):
            global_config["pitch"]["angle"]  =  global_config["pitch"]["angle"] -  global_config["pitch"]["delta"]*global_config["pitch"]["axis"]




def down(range = 90):
    setAngleServo1(global_config["pitch"]["angle"], range=range)

    if global_config["pitch"]["angle"] > 0 and global_config["pitch"]["angle"] < range:
        global_config["pitch"]["angle"]  =  global_config["pitch"]["angle"] -  global_config["pitch"]["delta"]*global_config["pitch"]["axis"]
    else:
        if abs(global_config["pitch"]["angle"] - range) > abs(global_config["pitch"]["angle"]):
            global_config["pitch"]["angle"]  =  global_config["pitch"]["angle"] +  global_config["pitch"]["delta"]*global_config["pitch"]["axis"]


# ===================SerialToServoInterface===================

def setAngleServo1(value, range=90):
   print ">>>>" , value
   #time.sleep(1)
   if value>0 and value < range:
       ser.write((int(value),))


def setAngleServo2(value, range=90):
   if value>0 and value < range:
       ser.write(str(value + 200).encode())

def lock():
    ser.write((-1,))

def fire():
    ser.write((-2,))
