#include <wiringPi.h>
#include <stdio.h>
#include <softTone.h>

#define LED1 6
#define LED2 5
#define LED3 4

#define SW1 25
#define SW2 29
#define SW3 28
#define SW4 27

#define RLY1 2
#define RLY2 3

const int pinPiezo = 0;
const int aMelody[8] = {100,300,600,1000,1500,2000,3000,4000};
int i = 0;

int main() {
	if(wiringPiSetup() == -1) return 0;
	softToneCreate(pinPiezo);
	pinMode(LED1, OUTPUT);
	pinMode(LED2, OUTPUT);
	pinMode(LED3, OUTPUT);
	pinMode(RLY1, OUTPUT);
	pinMode(RLY2, OUTPUT);
	pinMode(SW1, INPUT);
	pinMode(SW2, INPUT);
	pinMode(SW3, INPUT);
	pinMode(SW4, INPUT);
	while(1)
	{
		if(!digitalRead(SW1)) {
			
			softToneWrite(pinPiezo,aMelody[i]);
			i++;
			digitalWrite(LED1, 1);
			delay(1000);
		}
		else if(!digitalRead(SW2)) {
			softToneWrite(pinPiezo,aMelody[i]);
			i++;
			digitalWrite(LED2, 1);
			delay(1000);
		}
		else if(!digitalRead(SW3)) {
			softToneWrite(pinPiezo,aMelody[i]);
			i++;
			digitalWrite(LED3, 1);
			delay(1000);
		}
		else if(!digitalRead(SW4)) {
			softToneWrite(pinPiezo,aMelody[i]);
			i++;
			digitalWrite(RLY1, 1);
			digitalWrite(RLY2, 1);
			delay(1000);
		}
		
		if(i >= 8) i = 0;
		softToneWrite(pinPiezo,0);
		digitalWrite(LED1, 0);
		digitalWrite(LED2, 0);
		digitalWrite(LED3, 0);
		digitalWrite(RLY1, 0);
		digitalWrite(RLY2, 0);
		delay(10);
		
	}
	return 0;
}
