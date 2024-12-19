//www.elegoo.com
//2016.09.12
int ENA=10; 
int IN1=9;
int IN2=8;
int ENB=5; 
int IN3=7;
int IN4=6;
void setup()
{
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  digitalWrite(ENA,HIGH);  
  digitalWrite(ENB,HIGH);      

}

void stop(){
  digitalWrite(IN1,LOW);      
  digitalWrite(IN2,LOW);       
  digitalWrite(IN3,LOW);      
  digitalWrite(IN4,LOW);  
}
void forward(int ms){
  digitalWrite(IN1,LOW);      
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,LOW);      
  digitalWrite(IN4,HIGH);
  delay(ms);
  stop();
}
void back(int ms){
  digitalWrite(IN1,HIGH);      
  digitalWrite(IN2,LOW);        
  digitalWrite(IN3,HIGH);      
  digitalWrite(IN4,LOW);
  delay(ms);
  stop();
}
void right(int ms){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  delay(ms);
  stop(); 
}
void backright(int ms){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2,LOW);
  delay(ms);
  stop();
}
void left(int ms){
  digitalWrite(IN3,LOW);
  digitalWrite(IN4, HIGH);
  delay(ms);
  stop();
}
void backleft(int ms){
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(ms);
  stop();
}


void right_angle(){
  int FOrBms = 500 //this value will be changed based on results
  int Turnms = 500
  forward(ms);
  delay(500);
  right(ms);
  delay(500);  
}

void loop()
{
  right_angle();
}

