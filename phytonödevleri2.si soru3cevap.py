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
