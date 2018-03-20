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
