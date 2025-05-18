from scapy.all import ARP, Ether, srp
import time
import datetime

# Ağdaki IP aralığını belirt —> kendi subnet aralığını kullanman gerekebilir
ip_araligi = "192.168.1.0/24"  # Gerekirse değiştir

# MAC adreslerini tutacağımız sözlük
ip_mac_kayitlari = {}

def tarama_yap():
    # ARP isteği gönder
    arp = ARP(pdst=ip_araligi)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paket = ether / arp

    sonuc = srp(paket, timeout=3, verbose=0)[0]

    mac_listesi = {}

    for gönderilen, alınan in sonuc:
        ip = alınan.psrc
        mac = alınan.hwsrc

        # Aynı IP birden fazla MAC'e sahipse logla
        if ip in ip_mac_kayitlari and ip_mac_kayitlari[ip] != mac:
            zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{zaman}] ⚠️ ŞÜPHELİ ARP TESPİTİ: IP {ip} --> MAC {mac} (önceki: {ip_mac_kayitlari[ip]})")

        ip_mac_kayitlari[ip] = mac

def main():
    print("ARP Spoofing tespit aracı başlatıldı. (Çıkmak için Ctrl+C)\n")

    try:
        while True:
            tarama_yap()
            time.sleep(10)  # her 10 saniyede bir kontrol et
    except KeyboardInterrupt:
        print("\nDurduruldu.")

if __name__ == "__main__":
    main()
