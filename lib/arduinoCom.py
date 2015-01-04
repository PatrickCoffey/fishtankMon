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
    
    STATUS_AWAKE = '0 - Awake!'
    STATUS_BUSY = '1 - Busy!'
    CHAR_READ = 'R'
    CHAR_STATUS = 'S'
    CHAR_SLEEP = 'P'
    
    def __init__(self, comPort='/dev/ttyACM1', baudRate=9600):
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
    
    def _processData(self, data):
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
    
    def arduinoIsReady(self):
        '''Gets the status of the Arduino, can be used to check if it is ready'''
        ret = ''
        if self.isOpen():
            self.flush()
            self.write(self.CHAR_STATUS)
            time.sleep(0.5)
            ret = self.readline()
            if ret == self.STATUS_AWAKE:
                return True
            else:
                return False  
            
    def arduinoGetSensors(self):
        '''Gets the sensor values from the Arduino'''
        ret = {}
        if self.arduinoIsReady():
            self.flush()
            self.write(self.CHAR_READ)
            time.sleep(0.5)
            ret = self._processData(self.readline())
            return(ret)

    def arduinoSleep(self):
        '''Puts the Arduino to sleep by calling the sleep function in PF1 Firmware'''
        ret = ''
        if self.arduinoIsReady():
            self.flush()
            self.write(self.CHAR_SLEEP)
            time.sleep(0.5)


if __name__ == "__main__":
    pass
    #derp = _processData('light: 512, ph: 7.2')
    #print derp
    
    #arduino = ArduinoCom()
    #while arduino.isOpen():
        #print(arduino.arduinoGetSensors())

