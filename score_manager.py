#!/usr/bin/env python2

import Adafruit_BBIO.GPIO as GPIO
from time import time

class ScoreManager(object):
    RED_GOAL = "P8_45"
    RED_SUPERGOAL = "P8_46"
    RED_MINUS_BUTTON = "P8_43"
    RED_PLUS_BUTTON = "P8_44"

    BLUE_GOAL = "P8_41"
    BLUE_SUPERGOAL = "P8_42"
    BLUE_MINUS_BUTTON = "P8_39"
    BLUE_PLUS_BUTTON = "P8_40"
    
    EVENT_INTERVAL = 0.5

    def red_goal(self):
        print "red goal"

    def red_supergoal(self):
        print "red supergoal"

    def red_plus_button(self):
        print "red +1"

    def red_minus_button(self):
        print "red -1"

    def blue_goal(self):
        print "blue goal"

    def blue_supergoal(self):
        print "blue supergoal"

    def blue_plus_button(self):
        print "blue +1"

    def blue_minus_button(self):
        print "blue -1"

    def __init__(self):
        self.score = {"red": 0, "blue": 0}
        self.ltime = dict()
        self.props = ["red_goal", "red_supergoal",
                      "red_minus_button", "red_plus_button",
                      "blue_goal", "blue_supergoal",
                      "blue_minus_button", "blue_plus_button"]
        self.input_pins = [getattr(self, s.upper()) for s in self.props]
        for pin in self.input_pins:
            GPIO.setup(pin, GPIO.IN)
            self.ltime[pin] = 0
        self.handlers = dict([
            (getattr(self, s.upper()), getattr(self, s.lower()))
            for s in self.props])
    
    def run(self):
        for pin in self.input_pins:
            GPIO.add_event_detect(pin, GPIO.FALLING)
        while True:
            for pin in self.input_pins:
                if GPIO.event_detected(pin):
                    t = time()
                    if t > self.ltime[pin] + self.EVENT_INTERVAL:
                        self.ltime[pin] = t
                        self.handlers[pin]()


if __name__ == "__main__":
    sm = ScoreManager()
    sm.run()
