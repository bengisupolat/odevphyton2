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
    

                    
