#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include <DHT.h>
#include <SPI.h>
#include <MFRC522.h>

#define DHTPIN 5
#define DHTTYPE DHT11
#define SS_PIN 10
#define RST_PIN 9
#define TRIG_PIN 6
#define ECHO_PIN 7

DHT dht(DHTPIN, DHTTYPE);
MFRC522 rfid(SS_PIN, RST_PIN);
SoftwareSerial espSerial(2, 3);  // TX, RX (ESP8266 ile iletişim)

float temperature = 0.0;
float humidity = 0.0;
long distance = 0;
String cardUID;

void setup() {
  Serial.begin(115200);
  espSerial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  pinMode(8, OUTPUT);

  dht.begin();
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  Serial.println("Sistem Başlatıldı...");
}

void loop() {
  // Kart okutulduğunda UID okuma işlemi
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    // UID'yi temizle
    cardUID = "";
    for (byte i = 0; i < rfid.uid.size; i++) {
      cardUID += String(rfid.uid.uidByte[i], HEX);
      if (i < rfid.uid.size - 1) {
        cardUID += "";
      }
    }
    cardUID.toUpperCase();
    rfid.PICC_HaltA();

    // DHT11 sensörlerinden sıcaklık ve nem verilerini oku
    temperature = dht.readTemperature();
    humidity = dht.readHumidity();

    // Mesafe ölçümü
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    long duration = pulseIn(ECHO_PIN, HIGH);
    distance = duration * 0.0344 / 2;

    // JSON oluştur
    StaticJsonDocument<200> jsonDoc;
    jsonDoc["temperature"] = temperature;
    jsonDoc["humidity"] = humidity;
    jsonDoc["distance"] = distance;
    jsonDoc["uid"] = cardUID;

    String jsonString;
    serializeJson(jsonDoc, jsonString);

    // JSON'u ESP8266'ya gönder
    espSerial.println(jsonString);
    Serial.println("Giden JSON:");
    Serial.println(jsonString);
  }
  if (espSerial.available()) {
    String jsonResponse = espSerial.readStringUntil('\n');  // ESP8266'dan gelen JSON verisini oku

    if (jsonResponse.length() > 0) {
      Serial.println("Gelen JSON: " + jsonResponse);

      // Gelen JSON verisini çözümle
      StaticJsonDocument<200> doc;
      DeserializationError error = deserializeJson(doc, jsonResponse);
      const char* status = doc["status"];
      Serial.println(status);
      if (error) {
        int i;
        for(i=0;i<20;i++){
        digitalWrite(8, HIGH);
        delay(50);
        digitalWrite(8, LOW);
        delay(50);
        }
        
        Serial.println("JSON çözümleme hatası");
        return;
      }

      // JSON içeriğini al ve kullan

      
    }
  }
  delay(500);  // Gereksiz işlemleri engellemek için kısa bekleme
}
