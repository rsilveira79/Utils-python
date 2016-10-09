from pyfirmata import Arduino, util
from time import sleep
board = Arduino("COM3", baudrate=57600)
print(" ------------	HP Magic Mirror - Presence Detection ------------	#	")
print("Arduino Firmata Version", board.get_firmata_version())
# Arduino board PIN definition
ledpin=13
PIR = board.get_pin('d:7:i')		# d=digital 7=pin number i=input

#analog_0 = board.get_pin('a:0:i')
#digital_7 = board.get_pin('d:7:i') 
#ledpin = board.get_pin('d:13:o') 	# d=digital 13=pin number o=output

it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
PIR.enable_reporting()


def Blink(pin):
    board.digital[pin].write(1)
    sleep(0.5)
    board.digital[pin].write(0)
    sleep(0.5)
	
print("Blinking ...")

for i in range(0,5):
	Blink(ledpin)
	board.analog[0].read()

cycles=0

print("Lendo sensor PIR ...")
while cycles == 0: 	
	val = PIR.read()
	if val == 1:
		print("Detectado alguém! __________ PIR_reading = ", int(val)) 	
		sleep(0.5) 	
	if val == 0:
		print("Ninguém detectado! __________ PIR_reading = ", int(val)) 	
		sleep(0.5) 