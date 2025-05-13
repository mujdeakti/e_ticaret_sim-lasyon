import json

URUN_DOSYASI = "urunler.json"

def urunleri_yukle():
    with open(URUN_DOSYASI, "r") as f:
        return json.load(f)

def urunleri_listele(urunler):
    print("\n--- Ürün Listesi ---")
    for urun in urunler:
        print(f"{urun['id']}. {urun['isim']} - {urun['fiyat']} TL")