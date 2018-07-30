#!/usr/bin/env python3
import os
import sys
import subprocess




def welcome():
 ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
 os.system('clear')
 print("""
                       *     *      * * * * * *
                       *    *       *         *
                       *   *                  *        
                       *  *                   *      
                       * *          * * * * * *
                       *  *         *
                       *   *        *
                       *    *       *         *
                       *     *      * * * * * *
                     
                           Made By: Farhan
 """)
 print("                 * * * * * * Menu * * * * * * *")
 print(" 1) OS Details                                5) Show Mac address                   ")
 print(" 2) SQLmap Automated                          6) Set random Mac address              ")
 print(" 3) Social Engineering Toolkit                7) View Public IP addres            ")
 print(" 4) Scan Active Hosts In Network              0) Exit                ")
 print("Enter any option")
 p=input()
 if p=="1":
    print(os.uname())
    input("press any key to go back")
 if p=="2":
    subprocess.Popen(["gnome-terminal", "-e", "python sqlauto.py"])
    input("press any key to go back")
    welcome()
 if p=="3":
     subprocess.Popen(["gnome-terminal", "-e", "setoolkit"])
     input("press any key to go back")
     welcome()
 if p=="4":
     subprocess.call('nmap -PR 10.0.1.0/24 -sn',shell=True)
     input("press any key to go back")
     welcome()
 if p=="5":
     print("Device: eth0")
     subprocess.call('macchanger -s eth0', shell=True)
     print("\nDevice: wlan0")
     subprocess.call('macchanger -s wlan0', shell=True)
     input("Press any key to go back")
     welcome()
 if p=="6":

     print("Device: eth0 ")
     r1=subprocess.call('macchanger -r wlan0', shell=True)
     r2=subprocess.call('macchanger -r eth0', shell=True)
     print(r1)
     print(r2)
     input("press any key to go back")
     welcome()
 if p=="7":
     print("Public IP:")
     subprocess.call("curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//'", shell=True)
     input("Press any key to go back")
     welcome()
 if p=="0":
     exit()
 else:
     welcome()


welcome()




