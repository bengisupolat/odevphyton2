# odevphyton2
soru1
#a=katma değer ciro b=toplam satış miktarı c=hammadde maliyeti d=bakım onarım giderleri
#e=sevkiyat giderleri f=satın alınan hizmet giderleri
def katmaDegerCiroHesapla(b,c,d,e,f):
    global a
    a=b-(c+d+e+f)
    if(a>1000):
        print('işletme katma değer çirosu yüksektir')
    elif(500<a<999):
        print('işletme katma değer cirosu normal')
    else:
        print('işletme katma değer cirosu düşük')
    return a
print('lütfen değerleri giriniz') 
b=int(input('toplam satış miktarını giriniz'))
c=int(input('hammadde maliyeti  giriniz'))
d=int(input('bakım onarım giderlerini giriniz'))
e=int(input('sevkiyat giderlerini giriniz'))
f=int(input('satın alma hizmet giderlerini giriniz'))
x=katmaDegerCiroHesapla(b,c,d,e,f)
print(x)
soru2
#x=2016 yılı y=2017 yılı,a=müşteri çalışma süresi d=çalışılan süre,t=toplam müşteri miktarı
def musteriCalismaSuresi2016yiliHesapla(d,t):
    global a
    a=d/t
    return a
def musteriCalismaSuresi2017yiliHesapla(d,t):
    global f
    f=(d+50)/(t+20)
    return f
t=50
d=170
x=musteriCalismaSuresi2016yiliHesapla(d,t)
y=musteriCalismaSuresi2017yiliHesapla(d,t)
print(x-y)
soru3
#a=yazılım gelirleri, b=finansman gelirleri,c=ürün satış gelirleri,d=çalışan maaşları
#e=kira giderleri,f=donanım maliyeti,g=sponsorluk geliri,h=e-ticaret geliri,i=bakım maliyeti
def ilkaltikar(a,b,c,d,e,f):
    global ilkalti
    ilkalti=(a+b+c)-(d+e+f)
    return ilkalti
def sonaltikar(a,g,h,c,d,e,i):
    global sonalti
    sonalti=(a+g+h+c)-(d+e+i)
    return sonalti
print("lütfen değerleri giriniz")
a=int(input("yazılım gelirlerini giriniz"))
b=int(input("finansman gelirlerini giriniz"))
c=int(input("ürün satış geirlerini giriniz"))
d=int(input("çalışan maaşlarını giriniz"))
e=int(input("kira giderini giriniz"))
f=int(input("donanım maliyetini giriniz"))
g=int(input("sponsorluk gelirlerini giriniz"))
h=int(input("e ticaret gelirlerini giriniz"))
i=int(input("bakım maliyetini giriniz"))
x=ilkaltikar(a,b,c,d,e,f)
y=sonaltikar(a,g,h,c,d,e,i)
print(x-y)
if (x-y>5000):
    print("işletme çok karlı")
elif (1000<x-y<5000):
    print("işletme karı normal")
else:
    print("işletme yeterince karda değil")
soru4
satilanKoltukSayisi=int(25)
satilanYatakSayisi=int(20)
satilanDolapSayisi=int(10)
alinanYatakSayisi=int(15)
alinanKoltukSayisi=int(10)
alinanDolapSayisi=int(5)
def donemBasiStok(koltukSayisi,yatakSayisi,dolapSayisi):
    global donemBasiStok
    donemBasiStok=koltukSayisi+yatakSayisi+dolapSayisi
    return donemBasiStok
def donemSonuStok(satilanKoltukSayisi,satilanYatakSayisi,satilanDolapSayisi,alinanKoltukSayisi,alinanYatakSayisi,alinanDolapSayisi):
    global donemSonuStok
    donemSonuStok=(donemBasiStok-(satilanKoltukSayisi+satilanYatakSayisi+satilanDolapSayisi)+(alinanKoltukSayisi+alinanYatakSayisi+satilanDolapSayisi))
    return donemSonuStok
def ortalamaStok(donemBasiStok,donemSonuStok):
    global ortalamaStok
    ortalamaStok=((donemBasiStok+donemSonuStok)/2)
    return ortalamaStok
koltukSayisi=int(input("koltuk sayısı giriniz"))
yatakSayisi=int(input("yatak sayısı giriniz"))
dolapSayisi=int(input("dolap sayısı giriniz"))
x=donemBasiStok(koltukSayisi,yatakSayisi,dolapSayisi)
y=donemSonuStok(satilanKoltukSayisi,satilanYatakSayisi,satilanDolapSayisi,alinanKoltukSayisi,alinanYatakSayisi,alinanDolapSayisi)
z=ortalamaStok(donemBasiStok,donemSonuStok)
z=(x+y)/2
print(z)
    

                    
