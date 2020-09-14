import serial, sys

strPort1 = sys.argv[1]   # serial port

ser1=serial.Serial(strPort1, 115200)

print("connected to: " + ser1.portstr)

while True:
  try:
    line1 = ser1.readline()
    line2 = line1.decode('utf-8')
    line3 = line2.strip() 

    print(line3);

  except KeyboardInterrupt:
    print ('exiting')
    break
ser1.flush()
ser1.close()