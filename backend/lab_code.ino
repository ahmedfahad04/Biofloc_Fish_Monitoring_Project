#include <OneWire.h>
#include <DallasTemperature.h>

const float calibration_value = 26.58; //Use the calibrator code to obtain this value
float result;
float volt;
float ph_act;

unsigned long int avgval;
int tdsResult;
int buffer_arr[10];
int temp;
int count = 0;

char command;

#define samplePin 2
#define phPin 0 //Analog
#define tdsPin 3 //Analog
#define resetPin 7
#define thermoPin 9

OneWire thermoSense(thermoPin); //Allocating pin for OneWire communication
DallasTemperature sensors(&thermoSense); //Provide pin for temperature reading

void setup(){

  digitalWrite(resetPin, HIGH);
  delay(200);
  Serial.begin(9600);
  sensors.begin();
  pinMode(resetPin, OUTPUT);
  pinMode(samplePin, INPUT_PULLUP);
  pinMode(phPin, INPUT);
  pinMode(tdsPin, INPUT);
  
}
//Reports presence of sample
void samplePresence(){
  Serial.print(digitalRead(samplePin));
  }
//Reads the pH sensor reading
void phTester() {
  while (count != 5){ 
 for(int i=0;i<10;i++) 
 { 
 buffer_arr[i]=analogRead(phPin);
 delay(30);
 }
 for(int i=0;i<9;i++)
 {
 for(int j=i+1;j<10;j++)
 {
 if(buffer_arr[i]>buffer_arr[j])
 {
 temp=buffer_arr[i];
 buffer_arr[i]=buffer_arr[j];
 buffer_arr[j]=temp;
 }
 }
 }
 avgval=0;
 for(int i=2;i<8;i++)
 avgval+=buffer_arr[i];
 float volt=(float)avgval*5.0/1024/6;
 float ph_act = -5.70 * volt + calibration_value;
 result += ph_act;
 count += 1;
}
result /= 5;
Serial.print(result);
result = 0;
count = 0;
}

float thermoRead(){
  sensors.requestTemperatures();
  return sensors.getTempCByIndex(0);
  }

//Reads the TDS sensor reading
void tdsTester(){
  for (int i = 0; i < 5; i++)
  {
    tdsResult += analogRead(tdsPin);
  }
  Serial.print(tdsResult);  
}

void loop(){

  while(Serial.available() > 0){
  
  command = Serial.read();
  switch(command){
  
    case '1':
      samplePresence();
      break;
    case '2':
      phTester();
      break;
    case '3':
      tdsTester();
      break;
    case '4':
      digitalWrite(resetPin, LOW);
      break;
    default:
      break;
  } 
  }
}
