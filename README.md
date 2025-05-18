# ARP Spoofing Tespit Aracı  
## 📌 Ağ Güvenliği İçin Otomatik Tespit Sistemi  

🔍 **Bu proje, ARP trafiğini analiz ederek ağda gerçekleşen spoofing saldırılarını tespit etmek için geliştirilmiştir.**  

---

## 🔍 Özellikler  
Bu sistem aşağıdaki güvenlik işlevlerini yerine getirir:  

- **Gerçek Zamanlı ARP İzleme** → Ağdaki IP ve MAC adreslerini takip eder.  
- **ARP Spoofing Tespiti** → Aynı IP adresinden farklı MAC adresleri gelirse uyarı verir.  
- **Loglama ve İzleme** → Şüpheli aktiviteleri tarih ve saat bilgisi ile kaydeder.  
- **Otomatik Tarama** → Belirlenen aralıklarla ağ trafiğini analiz eder.  

---

---

## 🚀 Kurulum  
### 🔹 Bağımlılıkları yükleyin:  
```bash
pip install scapy
python arp_sniffer.py

