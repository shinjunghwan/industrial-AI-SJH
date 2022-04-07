#include <wiringPi.h>
#include <stdio.h>

#define LED1 6
#define SW1 25

int main() {
	if(wiringPiSetup() == -1) return 0;
	pinMode(LED1, OUTPUT);
	pinMode(SW1, INPUT);
	while(1)
	{
		digitalWrite(LED1, 1);
		delay(1000);
		printf("%d\n", digitalRead(SW1));
		digitalWrite(LED1, 0);
		delay(1000);
		printf("%d\n", digitalRead(SW1));
	}
}
