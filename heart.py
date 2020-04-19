import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

# ON
GPIO.output(7, 1)
time.sleep(1)

GPIO.output(11, 1)
time.sleep(1)

GPIO.output(12, 1)
time.sleep(1)

GPIO.output(13, 1)
time.sleep(1)

GPIO.output(15, 1)
time.sleep(1)

GPIO.output(29, 1)
time.sleep(1)

GPIO.output(31, 1)
time.sleep(1)

GPIO.output(33, 1)
time.sleep(1)

GPIO.output(35, 1)
time.sleep(1)

GPIO.output(37, 1)
time.sleep(1)

#OFF
GPIO.output(7, 0)
time.sleep(1)

GPIO.output(11, 0)
time.sleep(1)

GPIO.output(12, 0)
time.sleep(1)

GPIO.output(13, 0)
time.sleep(1)

GPIO.output(15, 0)
time.sleep(1)

GPIO.output(29, 0)
time.sleep(1)

GPIO.output(31, 0)
time.sleep(1)

GPIO.output(33, 0)
time.sleep(1)

GPIO.output(35, 0)
time.sleep(1)

GPIO.output(37, 0)
time.sleep(1)


# ON ALL
GPIO.output(7, 1)
GPIO.output(11, 1)
GPIO.output(12, 1)
GPIO.output(13, 1)
GPIO.output(15, 1)
GPIO.output(29, 1)
GPIO.output(31, 1)
GPIO.output(33, 1)
GPIO.output(35, 1)
GPIO.output(37, 1)

time.sleep(2)

GPIO.output(7, 0)
GPIO.output(11, 0)
GPIO.output(12, 0)
GPIO.output(13, 0)
GPIO.output(15, 0)
GPIO.output(29, 0)
GPIO.output(31, 0)
GPIO.output(33, 0)
GPIO.output(35, 0)
GPIO.output(37, 0)


GPIO.cleanup()
