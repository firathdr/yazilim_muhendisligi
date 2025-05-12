#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>  // JSON işlemleri

// WiFi bilgileri
const char* ssid = "xxxxxxxxxxxx";  // WiFi ağ adı
const char* password = "xxxxxxxxx";               // WiFi şifresi
const char* host = "http://192.168.1.8";       // Flask Sunucusu IP (http://'yi ekledim)
const int port = 5000;                         // Port numarası

void setup() {
  Serial.begin(9600);

  // WiFi bağlantısı başlatılıyor
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Bağlanıyor...");
  }
  Serial.println("Bağlantı başarılı!");
}

void loop() {
  if (Serial.available()) {
    String jsonData = Serial.readStringUntil('\n');  // Arduino'dan JSON oku

    if (jsonData.length() > 0) {
      Serial.println("Gelen JSON: " + jsonData);

      // HTTPClient nesnesi oluştur
      HTTPClient http;

      // Sunucuya bağlantıyı başlat
      WiFiClient wifiClient;
      http.begin(wifiClient, String(host) + String(":") + String(port) + "/update_data");

      // HTTP başlıkları gönder
      http.addHeader("Content-Type", "application/json");

      // JSON verisini POST isteği olarak gönder
      int httpResponseCode = http.POST(jsonData);  // POST isteği gönder

      if (httpResponseCode > 0) {
        // HTTP yanıt kodunu yazdır
        Serial.print("HTTP Yanıt Kodu: ");
        Serial.println(httpResponseCode);

        // Sunucudan gelen cevabı al
        String response = http.getString();
        Serial.println("Sunucudan Gelen Yanıt: " + response);

        // JSON formatında cevap oluştur
        StaticJsonDocument<200> doc;  // JSON dokümanı
        doc["status"] = "success";
        doc["message"] = response;  // Sunucudan gelen yanıtı JSON mesajına ekle

        // JSON yanıtı oluştur ve Arduino'ya gönder
        String jsonResponse;
        serializeJson(doc, jsonResponse);  // JSON verisini String'e dönüştür
        Serial.println("Arduino'ya gönderilecek JSON: " + jsonResponse);  // JSON yanıtı göster

        // JSON yanıtı Arduino'ya gönder
        delay(200)
        Serial.println(jsonResponse);  // Arduino'ya JSON verisini gönder
      } else {
        Serial.print("Sunucudan yanıt alınamadı, HTTP hata kodu: ");
        Serial.println(httpResponseCode);
      }

      // Bağlantıyı sonlandır
      http.end();
    }
  }
}
