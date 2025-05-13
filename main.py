
from urun import urunleri_yukle, urunleri_listele
from kullanici import kayit_ol, giris_yap
from sepet import sepeti_goster, sepetten_cikar, satin_al
import json


print("ana menü çalışıyor")
def ana_menu():
    while True:
        print("\n=== E-Ticaret Sistemi ===")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            kayit_ol()
        elif secim == "2":
            kullanici = giris_yap()
            if kullanici:
                urunler = urunleri_yukle()
                sepet = []

                while True:
                    print("\n--- Kullanıcı Menüsü ---")
                    print("1. Ürünleri Görüntüle")
                    print("2. Sepete Ürün Ekle")
                    print("3. Sepeti Görüntüle")
                    print("4. Sepetten Ürün Çıkar")
                    print("5. Satın Al")
                    print("6. Çıkış Yap")

                    secim = input("Seçiminiz: ")

                    if secim == "1":
                        urunleri_listele(urunler)
                    elif secim == "2":
                        urunleri_listele(urunler)
                        try:
                            urun_id = int(input("Sepete eklemek istediğiniz ürün ID'si: "))
                            urun = next((u for u in urunler if u["id"] == urun_id), None)
                            if urun:
                                sepet.append(urun)
                                print(f"✅ {urun['isim']} sepete eklendi.")
                            else:
                                print("❌ Geçersiz ürün ID!")
                        except ValueError:
                            print("❌ Lütfen geçerli bir sayı girin!")
                    elif secim == "3":
                        sepeti_goster(sepet)
                    elif secim == "4":
                        sepetten_cikar(sepet)
                    elif secim == "5":
                        satin_al(sepet, kullanici)
                    elif secim == "6":
                        print("🔒 Çıkış yapıldı.")
                        break
                    else:
                        print("❌ Geçersiz seçim!")
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    ana_menu()
