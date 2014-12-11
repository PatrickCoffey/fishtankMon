#!/usr/bin/python
# -*- coding: utf-8 -*-

# lib/arduinoCom.py
# -----------------------
# This is the class for the arduiono communication object.
# Its basically just a wrapper for a the serial object
# but it has a bit of extra arduino specific finctionality.


from serial import Serial
import time

class ArduinoComBase(Serial):
    '''
    Base Arduino Communication Object:
        This represents the base of the arduino connected via serial. 
        This class houses all the code used internally to the function.
        The ArduinoCom class inherits this and adds the user functions.
        
        Most documentation is found in pySerial
    '''
    
    def __init__(self, comPort='/dev/ttyACM0', baudRate=115200, statusChar='`'):
        '''Overloaded to allow default values - Check pySerial Documentation'''
        Serial.__init__(self, comPort, baudRate)
        print("Initialised Serial connection")
        self.statusChar = statusChar
        time.sleep(2)

    def _readChar(self):
        '''Read a single byte from the Serial buffer'''
        ret = ''
        assert(isinstance(ret, str))
        
        if self.isOpen():
            ret = self.read(1)
            return(ret) 

class ArduinoCom(ArduinoComBase):
    '''
    Arduino Communication Object:
        This represents the arduino connected via serial. 
        It is basically the Serial class from pySerial wrapped into
        a class with a few extra arduino specific functions.
        
        Most documentation is found in pySerial
    '''
    
    def arduinoGetSensors(self):
        '''Gets the sensor values from the Arduino'''
        ret = ''
        assert(isinstance(ret, str))
        
        if self.isOpen():
            self.flush()
            self.write('R')
            time.sleep(0.25)
            ret = self.readline()
            return(ret)
        
            
if __name__ == "__main__":
    arduino = ArduinoCom()
    while arduino.isOpen():
        print(arduino.arduinoGetSensors())

