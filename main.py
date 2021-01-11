import socket as s
import threading as t
from pyfiglet import Figlet
import os

def render(text,style):
    f=Figlet(font=style)
    print('\n'*2)
    print(f.renderText(text))
    print("\t"*5)

os.system("clear")
os.system("tput setaf 1")
render('CHAT APP Server','banner3')



os.system("tput setaf 5")
print("Enter Your Machine IP : ");
os.system("tput setaf 4")
Same_Machine_IP= input("\t\t\t")

os.system("tput setaf 5")
print("Give the Port the Num to this program ! ");
os.system("tput setaf 4")
Port_No=int(input("\t\t\t"))

os.system("tput setaf 5")
print("Enter Your Friend IP: ")
os.system("tput setaf 4")
FriendIP= input("\t\t\t")

MainSoc=s.socket(s.SOCK_DGRAM,s.AF_INET) 
MainSoc.bind((Same_Machine_IP,Port_No))



def ForSending():
        while True:
            os.system("tput setaf 2")
            MainSoc.sendto(input("\t\t\t\t\t\t").encode(),(FriendIP,Port_No))   

def ForRecving():
        while True:
            os.system("tput setaf 202")
            msg=MainSoc.recvfrom(20000)
            print("IP -> " + msg[1][0] + "\t\t\t\t\t\t\t\n-->" + msg[0].decode())

t.Thread(target=ForSending).start()
t.Thread(target=ForRecving).start()