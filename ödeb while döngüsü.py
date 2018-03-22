satis_miktari=500
birim_satis_fiyati=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=ciro+(satis_miktari*birim_satis_fiyati)
    satis_miktari=satis_miktari+200
    birim_satis_fiyati=birim_satis_fiyati+10
    i=i+1
print('500.000 den fazla kar',i,'. ayda tamamlanmıştr')
