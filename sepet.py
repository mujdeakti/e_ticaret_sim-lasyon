from kullanici import dosyayi_yukle, dosyaya_kaydet

def sepeti_goster(sepet):
    if not sepet:
        print("🛒 Sepetiniz boş...")
    else:
        print("\n--- Sepetiniz ---")
        toplam = sum(urun["fiyat"] for urun in sepet)
        for i, urun in enumerate(sepet, start=1):
            print(f"{i}. {urun['isim']} - {urun['fiyat']} TL")
        print(f"Toplam Tutar: {toplam} TL")

def sepetten_cikar(sepet):
    if not sepet:
        print("🛒 Sepetinizde ürün yok.")
        return
    sepeti_goster(sepet)
    try:
        sil_index = int(input("Çıkarmak istediğiniz ürün numarasını girin: "))
        if 1 <= sil_index <= len(sepet):
            silinen = sepet.pop(sil_index - 1)
            print(f"❎ {silinen['isim']} sepetten çıkarıldı.")
        else:
            print("❌ Geçersiz ürün numarası.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin!")

def satin_al(sepet, kullanici):
    if not sepet:
        print("❌ Sepetiniz boş. Satın alma işlemi yapılamaz.")
        return
    toplam = sum(urun["fiyat"] for urun in sepet)
    print("💳 Satın alma işlemi tamamlandı. Teşekkür ederiz!")
    print(f"Toplam Ödeme: {toplam} TL")

    for urun in sepet:
        kullanici["gecmis"].append(urun)

    veriler = dosyayi_yukle()
    for k in veriler:
        if k["kullanici_adi"] == kullanici["kullanici_adi"]:
            k["gecmis"] = kullanici["gecmis"]
            break
    dosyaya_kaydet(veriler)
    sepet.clear()