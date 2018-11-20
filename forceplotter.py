import matplotlib.pyplot as plt
import numpy
import RPi.GPIO as GPIO
import time
import sys

from hx711 import HX711

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

hx = HX711(12, 13)

hx.set_reference_unit(-31856.0)

hx.reset()
hx.tare()

force = []
timeStep = 0.0
startime = 0.0
endtime = 0.0
while True:
    try:
        starttime = time.clock()
        val = hx.get_weight(5)
        print
        "weight: %.1f" % val

        force.append(val)

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

        endtime = time.clock()
        timeStep = endtime - starttime
        print(timeStep)

        plt.plot(force)
        plt.xlabel("time (timestep %.5f)" % timeStep)
        plt.ylabel("force (kg)")
        plt.grid(True)
        plt.show()

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
