# include "DHT.h"

#define DHTPIN  5 // define DHTPIN to pin 5 of wemos

#define DHTTYPE DHT22 // defines what DHT sensor is using (the library can use 11 or 12 or 22)

DHT dht (DHTPIN, DHTTYPE, 15);


void setup() {
  Serial.begin(115200);
  
  dht.begin();
//Within the DHT sensor
}

void loop() {
  float h = dht.readHuminidity(); // reading temp. and humidity
  float t = dht.readTemperature(); // Read the temperature as Celsius

//Display Data
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" *C ");

  delay(2000); //delay the measurements between seconds
  // repeats every 2 seconds
  // DHT22 sensor will give temperature and hum. within the serial port
  
}
