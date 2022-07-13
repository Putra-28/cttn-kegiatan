import datetime
import os

os.system('clear')
x = datetime.datetime.now()

print ('''
     SILAHKAN TULIS KEGIATAN ANDA(☞ﾟ∀ﾟ)☞
         JANGAN LUPA TERSENYUM KAWAN
              BY.MONKEY D DARMAN

!!Klik Enter Saja Jika Ingin Menyelesaikan!!

''')
f = open("jurnal.txt", 'a')
while True:
  msg = input("Kegiatan ☞ ")
  tgl = x.strftime("[%d,%B][%H.%M] ")
  if msg == '':
    f.write("\n \n \n")
    break
  f.write(tgl+msg+"\n")

f.close()