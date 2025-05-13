import json
import os

KULLANICI_DOSYASI = "kullanicilar.json"

def dosyayi_yukle():
    if not os.path.exists(KULLANICI_DOSYASI):
        with open(KULLANICI_DOSYASI, "w") as f:
            json.dump([], f)
    with open(KULLANICI_DOSYASI, "r") as f:
        return json.load(f)

def dosyaya_kaydet(veriler):
    with open(KULLANICI_DOSYASI, "w") as f:
        json.dump(veriler, f, indent=4)

def kayit_ol():
    print("\n--- Kayıt Ol ---")
    kullanici_adi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")

    veriler = dosyayi_yukle()
    for k in veriler:
        if k["kullanici_adi"] == kullanici_adi:
            print("❌ Bu kullanıcı adı zaten alınmış.")
            return

    yeni_kullanici = {
        "kullanici_adi": kullanici_adi,
        "sifre": sifre,
        "ad": ad,
        "soyad": soyad,
        "gecmis": []
    }

    veriler.append(yeni_kullanici)
    dosyaya_kaydet(veriler)
    print("✅ Kayıt başarılı!")

def giris_yap():
    print("\n--- Giriş Yap ---")
    kullanici_adi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")

    veriler = dosyayi_yukle()
    for k in veriler:
        if k["kullanici_adi"] == kullanici_adi and k["sifre"] == sifre:
            print(f"✅ Hoş geldin {k['ad']} {k['soyad']}!")
            return k
    print("❌ Hatalı kullanıcı adı veya şifre.")
    return None