
int relay1 = RELAY_1;  
int relay2 = RELAY_2; 
int relay3 = RELAY_3;
int relay4 = RELAY_4;

void relayInit() 
{
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  pinMode(relay_control, INPUT);
  
  digitalWrite(relay1, LOW);
  digitalWrite(relay2, LOW);  
  digitalWrite(relay3, LOW);  
  digitalWrite(relay4, LOW);

  realy_control_system_off();
  relay_control_system_default_state();
}

void relay_control_system_default_state()
{
  digitalWrite(relay1, HIGH);    
  digitalWrite(relay2, HIGH);    
  digitalWrite(relay3, HIGH);    
  digitalWrite(relay4, HIGH);
}

void realy_control_system_on()
{
  digitalWrite(relay1, HIGH);    
  digitalWrite(relay2, HIGH);    
  digitalWrite(relay3, LOW);    
  digitalWrite(relay4, LOW);
}

void realy_control_system_off()
{
  digitalWrite(relay1, LOW);    
  digitalWrite(relay2, LOW);    
  digitalWrite(relay3, HIGH);    
  digitalWrite(relay4, HIGH);
}
