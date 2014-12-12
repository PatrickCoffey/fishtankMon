fishtankMon
===========

code for my fish tank monitor project...

I'm trying to keep it fairly reusable


fishtankMon - main.py
=====================
This is the main program logic


lib/dbHandler.py
================
This represents the database where the data will be logged.
Its a collection of SQLite3 objects wrapped together for ease.

    Database Object:
        This represents the database where the data will be logged. 
        Its a collection of SQLite3 objects wrapped together for ease.
        
        if dbPath is left blank on initialisation it will use an in
        ':memory:' database


lib/arduinoCom.py
=================
This is the class for the arduiono communication object.
Its basically just a wrapper for a the serial object
but it has a bit of extra arduino specific finctionality.

    Base Arduino Communication Object:
        This represents the base of the arduino connected via serial. 
        This class houses all the code used internally to the function.
        The ArduinoCom class inherits this and adds the user functions.
        
        Most documentation is found in pySerial

    Arduino Communication Object:
        This represents the arduino connected via serial. 
        It is basically the Serial class from pySerial wrapped into
        a class with a few extra arduino specific functions.
        
        Most documentation is found in pySerial


PF1 Arduino firmware
====================
  
This is a simple serial interface to talk to my python app on a
python capable device via serial.
 
It contains quite a few useful features that include:
 * Reads data from sensors and sends it via
    serial with multiple formats when asked.
 * Has an interface that allows the settings to be
    configured via serial.
 * coded as pythonic and simple as i could with
    Arduino. The idea is for this to be simple
    and easily reusable for alternate projects.

  Sensor Definitions 
  ------------------
    int iSensorCount = 1
     * Total Number of Sensors.
     * can be used to disable the higher numbered sensors.
     
    int sensor1Pin = 1
    char sensor1Type = 'd'
     * Example of typical Sensor Definition
     * 'd' = Digital
     * 'a' = Analog
    
  General Settings
  ----------------
    int iMainDelay = 50
     * The number of miliseconds to pause in the mail loop.
     * This is linked to the iExpire variable in the sense
       that: 
            iExpire * iMainDelay = time in ms before going
                                   into wait mode.
        
    int iWaitDelay = 500
     * The number of miliseconds to wait between sending
       StatusChar when im wait mode.

  ~Patty
         11/12/2014
