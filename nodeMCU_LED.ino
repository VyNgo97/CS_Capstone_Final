#define FASTLED_ESP8266_NODEMCU_PIN_ORDER
#include <FastLED.h>
#include <ESP8266WiFi.h>
#define NUM_LEDS 64
#define DATA_PIN 2

CRGB leds[NUM_LEDS];

const char* ssid = "haveagoodweekend";
const char* password = "hea316ven";


WiFiServer server(80);
void setup()
{
  FastLED.addLeds<WS2812, DATA_PIN>(leds, NUM_LEDS);

  Serial.begin(115200);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  server.begin();
  Serial.printf("Web server started, open %s in a web browser\n", WiFi.localIP().toString().c_str());
  FastLED.clear();
  FastLED.show();
}

// prepare a web page to be sent to a client (web browser)

void loop(){
  WiFiClient client = server.available();
  
  if (client){
    Serial.println("\n[Client connected]");
    while (client.connected()){
      if (client.available()){
        String line = client.readStringUntil('\r');
        Serial.print(line);
        if(line.length() == 1 && line[0] == '\n'){
          while(client.available()){
            line = client.readStringUntil('\r');
            String lineCopy = line;
            if(line.indexOf("colors")){
              Serial.println(line);
              int green = line.indexOf('G');
              int red = line.indexOf('R');
              int blue = line.indexOf('B');
              Serial.println(green);
              Serial.println(red);
              Serial.println(blue);
              String g = line.substring(green + 1, green + 4);
              String r = line.substring(red + 1, red + 4);
              String b = line.substring(blue + 1, blue + 4);
              Serial.println("Green = " + g);
              Serial.println("Red = " + r);
              Serial.println("Blue = " + b);
              client.stop();
              Serial.println("[Client disonnected]");
              lightme(g.toInt(),r.toInt(),b.toInt());
              break;
            }    
          }
        }
      }
    }
    delay(1); // give the web browser time to receive the data
  }
}
void lightme(int G, int R, int B){
  Serial.println((String)"GreenInt: " + G);
  Serial.println((String)"RedInt " + R);
  Serial.println((String)"BlueInt: " + B);
  
  fill_solid(leds, NUM_LEDS, CRGB(G,R,B));
  FastLED.show();
  
}
