ögrencisayisi = 1000
koltuksayisi   = 26


servissayisi        = ögrencisayisi//koltuksayisi
kalanogrencisayisi  = ögrencisayisi%koltuksayisi
boskoltuksayisi     = koltuksayisi-kalanogrencisayisi

if kalanogrencisayisi>=0 and boskoltuksayisi<=koltuksayisi:
    servissayisi = servissayisi+1

    print(f"{servissayisi} tane servis gereklidir.")
    print(f"Servislerimizde {boskoltuksayisi} tane boş koltuğunuz bulunmaktadır.")

