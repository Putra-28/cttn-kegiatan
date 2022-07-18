import datetime
import os

x = datetime.datetime.now()
f = open("jurnal.txt", 'a')


os.system('clear')
print ('''
     SILAHKAN TULIS KEGIATAN ANDA(☞ﾟ∀ﾟ)☞
         JANGAN LUPA TERSENYUM KAWAN
              BY.MONKEY D DARMAN

1. Add Kegiatan
2. Lanjutan

''')
menu = input("=> ") 

if menu == '1':
  t = x.strftime("%d, %B")
  f.write("\n"+t)
  ruangan = input("Ruangan ☞ ")
  msg = input("Kegiatan ☞ ")
  tgl = x.strftime(f"\n[{ruangan}][%d,%B][%H.%M] ")
  f.write(tgl+msg+"\n")
  
elif menu == '2':
  ruangan = input("Ruangan ☞ ")
  msg = input("Kegiatan ☞ ")
  tgl = x.strftime(f"[{ruangan}][%d,%B][%H.%M] "+msg)
  f.write(tgl+"\n")
  
else:
  print("Wrong System")
