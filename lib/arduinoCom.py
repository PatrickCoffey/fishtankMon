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
        
        Check pySerial Documentation
    '''
    
    def __init__(self, comPort='/dev/ttyACM0', baudRate=115200):
        '''Overloaded to set default values - Check pySerial Documentation'''
        Serial.__init__(self, comPort, baudRate)
        print("Initialised Serial connection")
        time.sleep(3)

    def _readChar(self):
        '''Read a single byte from the Serial buffer'''
        ret = ''
        if self.isOpen():
            ret = self.read(1)
            return(ret)
    
    def _processData(data):
        ret = {}
        sensors = str.split(data, ',')
        for sensor in sensors:
            temp = str.split(sensor, ':')
            ret[str.strip(temp[0])] = float(str.strip(temp[1]))
        return ret
        

class ArduinoCom(ArduinoComBase):
    '''
    Arduino Communication Object:
        This represents the arduino connected via serial. 
        It is basically the Serial class from pySerial wrapped into
        a class with a few extra arduino specific functions.
        
        Check pySerial Documentation
    '''
    
    def arduinoGetSensors(self):
        '''Gets the sensor values from the Arduino'''
        ret = {}
        if self.isOpen():
            self.flush()
            self.write('R')
            time.sleep(0.25)
            ret = self._processData(self.readline())
            return(ret)
        
            
if __name__ == "__main__":
    pass
    #derp = _processData('light: 512, ph: 7.2')
    #print derp
    
    #arduino = ArduinoCom()
    #while arduino.isOpen():
        #print(arduino.arduinoGetSensors())

