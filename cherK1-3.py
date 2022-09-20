import RPi.GPIO as GP

GP.setmode(GP.BCM)

GP.setup(14,GP.OUT)
GP.setup(15,GP.IN)
p = GP.input(15)
if p == 1:
    GP.output(14,1)
else:
    GP.output(14,0)