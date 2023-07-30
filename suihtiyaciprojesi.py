yetiskin = 1250
cocuk = 750
bebek = 500

print("""
Su İhtiyacı Hesaplama Programı
""")

yin = int(input("Lütfen ailenizdeki yetişkin sayısını giriniz: "))
cin = int(input("Lütfen ailenizdeki çocuk sayısını giriniz (Eğer çocuk yok ise 0 giriniz!)"))
bin = int(input("Lütfen ailenizdeki bebek sayısını giriniz (Eğer bebek yok ise 0 giriniz!): "))

hesapla = yetiskin*yin + cocuk*cin + bebek*bin
print(f"Aileniz için gerekli maksimum su miktarı {hesapla} litredir.")