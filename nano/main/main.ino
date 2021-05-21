#include "config.h"

int relay_control_signal = false;
int relay_control_state = RELAY_CONTROL_SYSTEM_IDLE;
bool isRelayControlSystemOn = false;
int relay_control = RELAY_CONTROL;
int relay_ctrl_sys_val[10] = {0};

void setup() {
  Serial.begin(9600);
  while (!Serial) ; // wait for serial
  Serial.println("Automatic Plant water control system - Relay control system");
  relayInit();
}

bool relaySysCtrlStatus()
{
  int count = 0;
  relay_control_signal = 0;

  for(count = 0; count < 10; count++) {
    relay_ctrl_sys_val[count] = analogRead(relay_control)/100;   // read the input pin
    delay(50);
  }

  for(count = 0; count < 9; count++) {
    if(relay_ctrl_sys_val[count] > 5) {
      if(relay_ctrl_sys_val[count] == relay_ctrl_sys_val[count+1]) {
        relay_control_signal++;
      }  
    }    
  }

  Serial.println(relay_control_signal);
  
  if(relay_control_signal > RELAY_ANALOG_VOLT) {
    return true;
  } else {
    return false;
  }
}

void loop() {
  switch(relay_control_state) {
    case RELAY_CONTROL_SYSTEM_IDLE:
      if(relaySysCtrlStatus() == true) {
        if(isRelayControlSystemOn == false) {
          relay_control_state = RELAY_CONTROL_SYSTEM_ON;  
        } else {
          relay_control_system_default_state();
        }        
      } else {
        if(isRelayControlSystemOn == true) {
          relay_control_state = RELAY_CONTROL_SYSTEM_OFF;  
        } else {
          relay_control_system_default_state();       
        }
      }      
      break;
      
    case RELAY_CONTROL_SYSTEM_ON:
      Serial.println("Automatic Plant water control system - Relay control system trun ON");
      realy_control_system_on();
      delay(2000);
      relay_control_system_default_state();
      relay_control_state = RELAY_CONTROL_SYSTEM_IDLE;
      isRelayControlSystemOn = true;
      break;
      
    case RELAY_CONTROL_SYSTEM_OFF:
      Serial.println("Automatic Plant water control system - Relay control system trun OFF");
      realy_control_system_off();
      delay(2000);
      relay_control_system_default_state();
      relay_control_state = RELAY_CONTROL_SYSTEM_IDLE;
      isRelayControlSystemOn = false;
      break;   
  }
}
