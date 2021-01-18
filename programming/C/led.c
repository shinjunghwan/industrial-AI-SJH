#include <wiringPi.h>
#include <stdio.h>

#define LED1 6

int main() {
	if(wiringPiSetup() == -1) return 0;
	pinMode(LED1, OUTPUT);
	while(1)
	{
		digitalWrite(LED1, 1);
		delay(1000);
		digitalWrite(LED1, 0);
		delay(1000);
	}
}
