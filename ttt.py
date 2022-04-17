import urllib.parse
import urllib.request
import os, sys
import ssl
import ftplib

host = 'kdrtopl.ru'
ftp_user = 'zzz@kdrtopl.ru'
ftp_password = 'Tramadol1989'
ftp = ftplib.FTP(host, ftp_user, ftp_password)
#ftp.cwd("www/amzntopl.ru")
file = 'img1.jpg'
file_to_upload = open('img1.jpg', 'rb')
ftp.storbinary('STOR ' + file, file_to_upload)
dd = ftp.nlst()
print(dd)
