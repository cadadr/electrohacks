# three digit binary counter

# circuit:
# - 3 leds, positives go to pins 18, 15, 14
#           negatives go to ground thru 470ohm
# - ground to RPi, any ground pin does

import RPi.GPIO as g

import time

g.setmode(g.BCM)

pins = [18, 15, 14]

# init
for pin in pins:
    g.setup(pin, g.OUT)
    g.output(pin, g.LOW)

# say hi
for pin in pins:
    g.output(pin, g.HIGH)
    time.sleep(1)
    g.output(pin, g.LOW)

time.sleep(1)

for _ in range(2):
    for pin in pins:
        g.output(pin, g.HIGH)
    time.sleep(0.5)
    for pin in pins:
        g.output(pin, g.LOW)
    time.sleep(0.5)


# binary counter infloop

beg = 7
end = 0
cur = beg
step = 0.5
skip = 0.1

try:
    while True:
        # represent number as three boolean binary digits
        digits = [bool(int(b)) for b in f"{cur:03b}"]
        # reverse to map onto pins
        digits.reverse()
        # light number up
        for index, digit in enumerate(digits):
            # put pin high if digit True
            g.output(pins[index], digit and g.HIGH)
        time.sleep(step)
        # reset
        for pin in pins:
            g.output(pin, g.LOW)

        time.sleep(skip)

        cur -= 1
        if cur < 0:
            cur = beg

finally:
    # reset
    for pin in pins:
        g.output(pin, g.LOW)
    g.cleanup()
