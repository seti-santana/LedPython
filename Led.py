from pyfirmata import Arduino, util
import time

Uno = Arduino('COM4')

print('Olá Mundo!')

while True:

    Uno.digital[7].write(1)
    print('LED ligado')
    time.sleep(0.5)

    Uno.digital[7].write(0)
    print('LED desligado')
    time.sleep(1)