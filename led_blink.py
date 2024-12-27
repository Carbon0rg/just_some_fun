from pyfirmata import Arduino, util
import time

board = Arduino("/dev/ttyUSB0")

it = util.Iterator(board)

it.start()

led1 = board.get_pin('d:12:o')
led2 = board.get_pin('d:11:o')
led3 = board.get_pin('d:10:o')
led4 = board.get_pin('d:9:o')
led5 = board.get_pin('d:8:o')

def pattern(l1, dl1, l2, dl2, l3, dl3, l4, dl4, l5, dl5):
    led1.write(l1)
    time.sleep(dl1)
    led2.write(l2)
    time.sleep(dl2)
    led3.write(l3)
    time.sleep(dl3)
    led4.write(l4)
    time.sleep(dl4)
    led5.write(l5)
    time.sleep(dl5)

while True:
    pattern(1, 0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1, 0.1,)
    pattern(0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1,)
    pattern(1, 0.1, 0, 0.1, 1, 0.1, 0, 0.1, 1, 0.1)
    pattern(0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1,)
