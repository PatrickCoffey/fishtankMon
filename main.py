#!/usr/bin/python
# -*- coding: utf-8 -*-

# fishtankMon - main.py
# -----------------------
# This is the main program logic

import lib.arduinoCom as arduinoCom
import lib.dbHandler as dbHandler

import time

arduino = arduinoCom.ArduinoCom()
db = dbHandler.sensorStore()

while true:
    data = arduino.arduinoGetSensors()
    print data
    #db.insertData(data)