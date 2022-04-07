#include <wiringPi.h>
#include <stdio.h>
#include <softTone.h>

#define LED1 6
#define SW1 25
const int pinPiezo = 0;
const int aMelody[8] = {100,300,600,1000,1500,2000,3000,4000};

int main() {
	if(wiringPiSetup() == -1) return 0;
	softToneCreate(pinPiezo);
	pinMode(LED1, OUTPUT);
	pinMode(SW1, INPUT);
	while(1)
	{
		int i;
		for(i=0;i<8;i++) {
			softToneWrite(pinPiezo,aMelody[i]);
			delay(1000);
		}
		softToneWrite(pinPiezo,0);
		delay(1000);
		/*
		digitalWrite(LED1, 1);
		delay(1000);
		printf("%d\n", digitalRead(SW1));
		digitalWrite(LED1, 0);
		delay(1000);
		printf("%d\n", digitalRead(SW1));
		*/
	}
	return 0;
}
