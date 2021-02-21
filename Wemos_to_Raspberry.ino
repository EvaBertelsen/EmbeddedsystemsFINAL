// libraries to import (board and sensor)
#include "ESP8266WiFi.h" // board library
 // #include <aREST.h> not sure if it's necessary, it's for arduino boards
#include "DHT.h" // sensor library

// DHT sensor pins
#define DHTPIN 5 // assigns the sensor pin to 5
#define DHTTYPE DHT22 // not sure about number?

// not sure if needed
// aRest rest = aRest();

// initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE, 15);

// wifi parameters for the wifi the smart home is in
const char* ssid = "your-wifi-name";
const char* password = "your-wifi-password";

// the port that listens for incoming TCP connections
#define LISTEN_PORT             80

// Create an instance of the server
WiFiServer server(LISTEN_PORT);

// variables to be exposed to the API
int temperature;
int humidity;

void setup(void)
{
  Serial.begin(115200); // Start Sterial
  
  dht.begin(); // Within DHT inicialize it (INIT)

  // check if this rest. is needed, it might be needed aRest.h library together (not sure)
  rest.variable("temperature", &temperature); // INIT variables and expose them to rest API
  rest.variable("humidity", &humidity);

  rest.set_id("1"); // give Identification (number) to device
  rest.set_name("sensor_module"); // give a name to device

  
  // Connecting to Wifi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 // starting server
  server.begin();
  Serial.print("Server Started");
 // print the ip address in the serial monitor
  Serial.println(Wifi.localIP());
  
}
void loop () {
  // reading the temperature and humidity
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  // handle REST calls
  WiFiClient client = server.available();
  if (!client) {
    return; 
  }
  while(!client.available((){
    delay(1);
  }
  rest.handle(client);

  
}
