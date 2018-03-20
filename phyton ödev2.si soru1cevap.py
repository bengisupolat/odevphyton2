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
