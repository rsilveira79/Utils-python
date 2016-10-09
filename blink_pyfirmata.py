from pyfirmata import Arduino, util
from time import sleep
board = Arduino("COM3", baudrate=57600)
print(" ------------	HP Magic Mirror - Presence Detection ------------	#	")
print("Arduino Firmata Version", board.get_firmata_version())
# Arduino board PIN definition
ledpin=13
relepin=6

PIR = board.get_pin('d:7:i')		# d=digital 7=pin number i=input

#analog_0 = board.get_pin('a:0:i')
#digital_7 = board.get_pin('d:7:i') 
#ledpin = board.get_pin('d:13:o') 	# d=digital 13=pin number o=output

it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
PIR.enable_reporting()


def Blink(pin, tempo):
    board.digital[pin].write(1)
    sleep(tempo)
    board.digital[pin].write(0)
    sleep(tempo)

cycles=0

while cycles == 0: 	
	Blink(relepin, 2)
	sleep(1) 