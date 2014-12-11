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
         * 'i' = I2c
         * 's' = SPI
    
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
int iSensorCount = 1;

int sensor1Pin = 1; 
char sensor1Type = 'd';
//---------------------

// General Settings
char statusChar = '`';
int iExpire = 100;
int iMainDelay = 50;
int iWaitDelay = 500;
//---------------------

// Other Settings/Globals
int inByte = 0;            //global
int iCountExp = 0;         //global
//---------------------

void setup()
{
  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  establishContact(); // enter wait mode
}

void loop()
{
  iCountExp += 1;
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    if (inByte == 'R') {
      // send sensor values
      Serial.write("DERP");   
    }
    else if (inByte == 'C') {
      Serial.write("CONFIG MENU\n");
      Serial.write(" s - Set statusChar\n");
      Serial.write(" e - Set iExpire\n");
      Serial.write(" m - Set iMainDelay\n");
      Serial.write(" w - Set iWaitDelay\n");
      
      // Get the answer
      inByte = getInput();
      if (inByte == 's') {
        Serial.write("Enter the StatusChar");
        //Get the answer
        inByte = getInput();
        statusChar = inByte;
        Serial.write("statusChar set to:");
        Serial.write(statusChar);
        Serial.write("\n");
      }
      else if (inByte == 'e') {
        Serial.write("Enter the iExpire");
        //Get the answer
        inByte = getInput();
        statusChar = inByte;
        Serial.write("statusChar set to:");
        Serial.write(statusChar);
        Serial.write("\n");
      }
    }
    else {
      establishContact(); //Return to wait mode
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

char getInput() {
  do {
    inByte = Serial.readBytes();
    if (inByte != -1 or inByte != 0) {
      return inByte;
    }
  } while (inByte == -1 or inByte == 0);
}

