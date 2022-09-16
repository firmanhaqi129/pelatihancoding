print('menghitung volume balok')
p = int(input('panjang: '))
l = int(input('lebar: '))
t = int(input('tinggi: '))

def volume(p,l,t):
    V = p * l * t   
    return V

print('panjang={}, lebar={}, tinggi={} , volume={} ,'.format(p,l,t, volume(p,l,t),))

print('menghitung volume kubus')
sisi = int(input('sisi: '))
hasil = sisi*sisi*sisi
print('volume kubus adalah : '+ str(hasil))