/*
    PF1 Serial interface
    --- ------ ---------
  
    This is a simple interface to talk to my python app on a
    python capable device via serial.
  
    It contains quite a few useful features that include:
     -* Reads data from sensors and sends it via
        serial with multiple formats when asked.
     -* Has an interface that allows the settings to be
        configured via serial.
     -* coded as pythonic and simple as i could with
        Arduino. The idea is for this to be simple
        and easily reusable for alternate projects.

    // Sensor Definitions 
        int iSensorCount = 1
         * Total Number of Sensors.
         * can be used to disable the higher numbered sensors.
    
        int sensor1Pin = 1
        char sensor1Type = 'd'
         * Example of typical Sensor Definition
         * 'd' = Digital
         * 'a' = Analog
    
    // General Settings
        char statusChar = '`'
         * Char to repeat over searial to signify waiting.
         
        int iExpire = 100
         * Total loops to complete before entering wait mode.
        
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
*/
 
// Sensor Definitions 
int iSensorCount = 2;

int sensorPins[] = {1,1}; 
char sensorTypes[] = {'d','a'};
String sensorNames[] = {"Leak", "Light"};
//---------------------

// General Settings
char statusChar = '`';
char cSeperator = ',';
int iExpire = 100;
int iMainDelay = 50;
int iWaitDelay = 500;
//---------------------

// Other Settings/Globals
int inByte = 0;            //global
int iCountExp = 0;         //global
char serialIn[16];         //global
//---------------------

void setup() {
  Serial.begin(115200);
  //while (!Serial) {
  //  ;
  //}
  initPins();
  establishContact(); // enter wait mode
}

void loop() {
  iCountExp += 1;
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    if (inByte == 'R') {
      // send sensor values
      String val = readSensors();
      Serial.print(val);   
    }
  }
  if (iCountExp == iExpire) {
    iCountExp = 0;
    establishContact();  // Return to wait mode after timeout
  }
  delay(iMainDelay);
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print(statusChar);   // send statusChar
    delay(iWaitDelay);
  }
}

void initPins() {
  for (int i = 0; i < iSensorCount - 1; i++) {
    switch (sensorTypes[i]) {
      case 'd':
        //Digital Sensor
        pinMode(sensorPins[i], INPUT);
        break;
      case 'a':
        //Analog Sensor
        ;
        break;
    }
  }
}

String readSensors() {
  String ret;
  String val;
  for (int i = 0; i < (iSensorCount); i++) {
    if (i > 0) {
      ret += cSeperator;
    }
    ret += sensorNames[i];
    ret += ":";
    switch (sensorTypes[i]) {
      case 'd':
        //Digital Sensor
        int valD;
        valD = digitalRead(sensorPins[i]);
        val = String(valD, DEC);
        ret += val;
        break;
      case 'a':
        //Analog Sensor
        int valA;
        valA = analogRead(sensorPins[i]);
        val = String(valA, DEC);
        ret += val;
        break;
    }
  }
  ret += "\n";
  return ret;
}  