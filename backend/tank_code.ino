/*The module which has their own pump is a master module.
Master module controls the water inlet pump. It switches the pump
based on their native sensor reading. A master pump can either have a dedicated water inlet
or a shared water inlet. If the inlet is shared then the connected tanks must be
of same volume.According to the connected container theory, all connected containers
will have similar level of liquid. So if the master module senses half level of water
then the connected tanks will eventually have half level of water for having the same volume*/

//The purpose of creating a master module is to save time, water and energy
#include <OneWire.h>
#include <DallasTemperature.h>

//Credentials of the module
const int set_code = 1000; //Will change for every customer
const int module_code = 123; //Will change for every module

//Variables to work with
int call_code = set_code+module_code;
int call;
int command;

//Allocation of pins
#define wlh 2
#define wlf 4
#define masterPin 6
#define checkPump 7
#define samplePump 8
#define resetPin 9
#define inPump 10
#define thermoPin 12

//Allocation of thermal reading
OneWire thermoSense(thermoPin); //Allocating pin for OneWire communication
DallasTemperature sensors(&thermoSense); //Provide pin for temperature reading

void setup(){
  digitalWrite(resetPin, HIGH);
  delay(200);
  Serial.begin(9600);
  sensors.begin();
  pinMode(wlh, INPUT_PULLUP);
  pinMode(wlf, INPUT_PULLUP);
  pinMode(masterPin, INPUT_PULLUP);
  pinMode(checkPump, OUTPUT);
  pinMode(samplePump, OUTPUT);
  pinMode(resetPin, OUTPUT);
  pinMode(inPump, OUTPUT);
  pinMode(thermoPin, INPUT);
  }

//Sends sample water during pre culture and later checks water level
void preCultureSample(){
  Serial.print("SPSW");
  while(true){
    call = Serial.readString().toInt();
    if(call == call_code){
      digitalWrite(samplePump, HIGH);
      while (true){
        int c2 = Serial.readString().toInt();
        if(c2 == call_code){
          digitalWrite(samplePump, LOW);
          break;
          }
        }
        break;
      }
    }
    while(digitalRead(wlh) == HIGH){
      digitalWrite(checkPump, HIGH);
      }
  }

//Checks temperature and sends sample water during culture and later checks water level
void cultureMonitoring(){
  sensors.requestTemperatures();
  Serial.print("TR");
  while(true){
    call = Serial.readString().toInt();
    if(call == call_code){
      Serial.print(sensors.getTempCByIndex(0));
      break;
      }
    }
   Serial.print("SCSW");
   while(true){
    call = Serial.readString().toInt();
    if(call == call_code){
      digitalWrite(samplePump, HIGH);
      while(true){
        call = Serial.readString().toInt();
        if(call == call_code){
          digitalWrite(samplePump, LOW);
          break;
          }
        }
        break;
      }
    }
    while(digitalRead(wlf) == HIGH){
      digitalWrite(checkPump, HIGH);
      }
    digitalWrite(checkPump, LOW);
  }

//Fills water to half level of the tank
void halfLevelFiller(){
  digitalWrite(inPump, HIGH);
  while(true){
    call = Serial.readString().toInt();
    if(call == call_code){
      if(digitalRead(wlh) == LOW){
        digitalWrite(inPump, LOW);
        Serial.print(true);
        break;
        } else {
          Serial.print(false);
          continue;
          }
      }
    }
    delay(1000);
  }

//Fills water to full level of tank
void fullLevelFiller(){
  digitalWrite(inPump, HIGH);
  while(true){
    call = Serial.readString().toInt();
    if(call == call_code){
      if(digitalRead(wlf) == LOW){
        digitalWrite(inPump, LOW);
        Serial.print(true);
        break;
        } else {
          Serial.print(false);
          continue;
          }
      }
    }
    delay(1000);
  }

void loop(){
  while (Serial.available()>0){
    call = Serial.readString().toInt();
    if (call == call_code){
      Serial.print('G');
      Serial.print(call_code);
      while(true){
        command = Serial.readString().toInt();
        if(command > 0){
          switch(command){
            case 1:
              Serial.print(digitalRead(masterPin));          
              break;
            case 2:
              preCultureSample();
              digitalWrite(resetPin, LOW);
            case 3:
              cultureMonitoring();
              digitalWrite(resetPin, LOW);
              break;
            case 4:
              halfLevelFiller();              
              digitalWrite(resetPin, LOW);
              break;
            case 5:
              fullLevelFiller();              
              digitalWrite(resetPin, LOW);
              break;
            case 6:
              Serial.print(digitalRead(wlh));
              break;
            case 7:
              Serial.print(digitalRead(wlf));
              break;
            default:
              continue;     
            }
            break;
          }
        }
      }
    }
  }
