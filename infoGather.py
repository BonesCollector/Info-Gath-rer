#!/bin/python3
import os
import nmap


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
    GREEN = '\033[1;32m'
    RED= '\033[1;31m'

os.system("clear")
os.system("sh banner")
print ("_" * 50)
print ("\n")
nm = nmap.PortScanner()
nma = nmap.PortScannerAsync()
print(bcolors.WARNING + "you which to scan an ip/ips ? \n" + bcolors.ENDC)

def call_back_to_main():
 call_back_to_main=input("Press enter to start over or type q to exit : ")
 if call_back_to_main == '' :
    main()

def _intense_scan():
 os.system('clear')
 os.system('sh header.2')
 host = input('enter the ip address to scan : \n' )
 port = input('enter the port ranges : \n')
 print(bcolors.BOLD + bcolors.GREEN +"plase wait .............")
 nm.scan(host, port , arguments='-T4 -A -sVC -oN intense-scan.opt')
 for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
          print('----------')
          print('Protocol : %s' % proto)

          lport = nm[host][proto].keys()
          for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
              

def enmuration_scan():
 os.system('clear')
 os.system('sh header.2')
 print("Enmuration scan is a faster method than intense to scan")
 host = input('enter the ip address to scan : \n' )
 port = input('enter the port ranges : \n')
 print(bcolors.BOLD + bcolors.GREEN +"plase wait .............")
 nm.scan(host, port , arguments='-T4 -sVC -oN enmuration-scan.opt')
 for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
          print('----------')
          print('Protocol : %s' % proto)

          lport = nm[host][proto].keys()
          for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                

def callback_result(host, scan_result):
 print("scaning please wait .........\n")
 nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE ')
 hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
 for host, status in hosts_list:
  print('{0}:{1}'.format(host, status)  + bcolors.OKGREEN + '                              online' + bcolors.ENDC)
  print('-'* 50) 
  while nma.still_scanning():
    print("scanning ...")
    nma.wait(2)       
    out1=input("press enter to start  over or q to quit\n")
    if out1 == '' :
     main()
    else :
     exit()
## ---  TO DO -- ADD MORE OPTIONS 
def main() :
    print(bcolors.OKCYAN + "make a choice \n" + bcolors.ENDC)
    print(bcolors.OKGREEN + "1 - scan an IP/IPS ? " + bcolors.ENDC)
    print (bcolors.OKGREEN + "2 - exit . \n" + bcolors.ENDC)
    choice = input("press enter for scan or type 2   : \n")
    if choice == '2' :
     exit()
    elif choice == '' or '1' :
          os.system("clear")
          os.system("sh  header.1") 
          range_sub_scan=input("Please press enter or type no : \n")
          if range_sub_scan == '' :
            print(bcolors.WARNING + "scaning local-network [192.168.1.1] for up hosts \n" + bcolors.ENDC)
            callback_result('host','scan_result')
            call_back_to_main()
          else :
            intense_ = input(""" 1 - intense scan   ? 
 2 - enmuration ports scan ? \n\n""")
            if intense_ == '1' :
              _intense_scan()
              call_back_to_main()
            elif intense_ =='2' :
              enmuration_scan()
              call_back_to_main()
            else :
             print (bcolors.BOLD + bcolors.RED + "Wrong selections ! "  + bcolors.ENDC ) 
             main()

    else :
     print('Bye Bye .')
     exit() 

if __name__ == "__main__":
    main()