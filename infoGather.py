#!/bin/python3
import keyboard
import os
import nmap
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system("clear")
os.system("sh banner")
print ("_" * 50)
print ("\n")
nm = nmap.PortScanner()
nma = nmap.PortScannerAsync()
print(bcolors.WARNING + "you which to scan an ip/ips ? \n" + bcolors.ENDC)

def range_intense_all()


def callback_result(host, scan_result):
             print("scaning please wait .........\n")
             nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
             hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
             for host, status in hosts_list:
              print('{0}:{1}'.format(host, status)  + bcolors.OKGREEN + '                              online' + bcolors.ENDC)
              print('-'* 50) 
             while nma.still_scanning():
              print("scanning ...")
              nma.wait(2)       
              out1=input("press enter to start  over or q to quit\n")
              if out1 == '' :
               user_choice()
              else :
               exit()

def user_choice() :
    print(bcolors.OKCYAN + "make a choice \n" + bcolors.ENDC)
    print(bcolors.OKGREEN + "1 - scan a range of ips ? " + bcolors.ENDC)
    print (bcolors.OKGREEN + "2 - scan a single ip  ?\n" + bcolors.ENDC)
    choice = input("press enter for range scan or type 2 for single target : ")
    os.system("clear")
    if choice == '' :
      print('-'* 50)
      print('-'* 50)
      ip_range = input(bcolors.HEADER + "PRESS ENTER  : "    +  bcolors.ENDC + """to scan local 192.168.1.1/24 network 
      or enter desired network ip ?
--------------------------------------------------
--------------------------------------------------\n""")
      if ip_range == "" :
          os.system("clear")
          os.system("sh  header.1") 
          range_sub_scan=input("Please press enter or type no : ")
          if range_sub_scan == '' :
            os.system("clear")
            print(bcolors.WARNING + "scaning local-network [192.168.1.1] for up hosts \n" + bcolors.ENDC)
            callback_result('host','scan_result')
            call_back_to_main=input("Press enter to start over or type q to exit : ")
            if call_back_to_main == '' :
              user_choice()
            else : 
               exit()
                
          elif range_sub_scan == 'no' :
            all_ports_ = input(""" 1 - scan all ports  ? 
 2 - selected ports scan ? \n\n""")
            if all_ports_ == '1' :
                intense = input("\nis it intense scan or enmuration scan ?\n yes or no : ")
                if intense =='yes' :
                 range_intense_all()
      else :
       print ("not ENTER")
user_choice()


#for input in user_choice : 
#  if input == 1 : 
#      print ("1 selected")

#def range_ips() :
 #   if user_choice(1) : 
  #   print ("choice 1 ")   
   #  exit
 #def single_ip() :
 #def selected_port() :
 #def range_ports() :
# def ping_alive1() :
 #def ping_alive2() :
 #def save_to_file():