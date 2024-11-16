# module
from os import system
from time import sleep
import sys, datetime
import os,sys,time
import requests, json, time, threading, os, sys
from colorama import Fore, init
import itertools
import random
import pyfiglet
import base64
import socket
import shutil
import concurrent.futures

red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
otp = random.randrange(100000, 1000000)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/gapiapja/bussid/refs/heads/main/sandiaja"

def key():
    if sys.platform.startswith("windows"):
        os.system("start \"\" https://work.ink/1WFv/m20k4gwz")
        
    elif sys.platform.startswith("linux"):
        os.system("termux-open-url https://work.ink/1WFv/m20k4gwz")
        
    else:        
        os.system("open \"\" https://work.ink/1WFv/m20k4gwz")
        
        
def load_users():
    try:
        response = requests.get(GITHUB_RAW_URL)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error mengambil data : {e}")
        return {}

def login():
    global username
    username = input("Masukkan username: ")
    key()
    
    

init(autoreset=True)

def animate_text(text):
  number_of_characters=1
  print("\n")
  print(text[0:number_of_characters])
  number_of_characters += 1
  if number_of_characters > len(text):
    number_of_characters = 0
    time.sleep(0.02) 
    os.system("cls||clear") 

def log():
  
  user = input(f"{blue}Masukin Token {white}:")
  
  check_key = 'https://redirect-api.work.ink/tokenValid/' + user
  p = requests.get(check_key)
  p.raise_for_status()
  g = p.json()
  hasi = g["valid"]
  if hasi == True:
       print(f"{green}--------------------------------------------")
       print(f"{green}      Token Ditemukan        ")
       print(f"{green}--------------------------------------------")  
       time.sleep(3)
  else:      
    print(f"{red}--------------------------------------------")
    print(f"{red} Token Tidak Ditemukan ")
    print(f"{red}--------------------------------------------")  
    os.system("cls||clear")
    log()
       
        
login()  
log()
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        time.sleep(1)
        total_second -= 1
    print("""\33[0;35m==========================""")


# Config
system("clear")

try:
  __import__('requests')
except ModuleNotFoundError:
  os.system ('pip3 install requests')
finally:
  import requests

try:
  __import__('bs4')
except ModuleNotFoundError:
  os.system ("pip3 install bs4")
finally:
  from bs4 import BeautifulSoup as parser


logo = f"\n╔═════════════════════════════════════╗\n║[{yellow}•] {red}𝙽𝙾𝙼𝙾𝚁 0: {white}UP TO 2𝙹𝚞𝚝𝚊             ║\n║[{yellow}•] {red}𝙽𝙾𝙼𝙾𝚁 1: {white}UP TO 1𝙹𝚞𝚝𝚊             ║\n║[{yellow}•] {red}𝙽𝙾𝙼𝙾𝚁 2: {white}UP TO 800𝚁𝚒𝚋𝚞           ║\n║[{yellow}•] {red}𝙽𝙾𝙼𝙾𝚁 3: {white}UP TO 500𝚁𝚒𝚋𝚞           ║\n║[{yellow}•] {red}𝙽𝙾𝙼𝙾𝚁 4: {white}REVERSE -500𝚁𝚒𝚋𝚞        ║\n╚═════════════════════════════════════╝"







done = False


def animate():
    for c in itertools.cycle(['🖕', '😎']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.9)





txt = "JOKIBUSSID"
banner = pyfiglet.figlet_format(txt, font="slant", justify="center")



print(banner)



auth = input(f"\033[1;33;41m•\033[1;37[Input X-Authorization Code\033[1;33m•\033[0m\033[")

record = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 20},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 13},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},{"Key":{"sourceCity":"PBR","destinationCity":"BKT","routePassed":["BKT","PBR"],"activityRewards":None},"Value":50},{"Key":{"sourceCity":"PBR","destinationCity":"PDG","routePassed":["PDG","BKT","PBR"],"activityRewards":None},"Value":9},{"Key":{"sourceCity":"BKT","destinationCity":"PDG","routePassed":["PDG","BKT"],"activityRewards":None},"Value":50},]





headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}

def mxxxx():
        data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
        response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['InfoResultPayload']
                                uang= chat['UserVirtualCurrency']
                                money= uang['RP']

                                fff= chat['AccountInfo']
                                zzz= fff['TitleInfo']
                                www= zzz['TitlePlayerAccount']
                                saa= www['Id']

                                gcc= chat['AccountInfo']
                                id= gcc['TitleInfo']
                             #   you= id['DisplayName']
                                ketik(f"{green}---------------------------- {white}Info Akun{green} ----------------------------")                               
                                ketik(f"{white} - {green}Total_Money{white}: {white}{money}   {white}                    ")
                                ketik(f"{red} - Id_Kamu: {green}{saa}               {white}     ")
                                ketik(f"{red}╚═════════════════════ - {yellow}════════════════════════╝")



def create_ff():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_mll(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']

def pass_missyu():
        carrer = create_ff()
        if carrer != None:
                token = carrer['token']
                skip_mll(token)
                mxxxx()

headers['X-Authorization'] = auth

def rename():
        data = json.dumps({"DisplayName":"Top Up Tes"})
        response = requests.post('https://4ae9.playfabapi.com/Client/UpdateUserTitleDisplayName', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['DisplayName']

#800k
recordd = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},]
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}

def remove():
        data = json.dumps({"FunctionName":"PurchaseAccessories","FunctionParameter":{"bus":"JB-003","accToPurchase":[],"pPriceIDs":[],"accToRemove":["CAG1b-RT5I0","BAR3-RT0I0","BCNS1-L0T2.10I15","BCNS1-L0T2.10I16","BCNS1-L0T2.10I17","BCNS1-L0T2.10I18","BCNS1-L0T2.10I19","BCNS1-RT2I0","BCNS1-RT2I2","BCNS1-RT2I1","BCNS1-RT2I3","BCNS1-RT2I4","HRN3-RT9I0","HRN3-RT9I1","BPRF2-RT3I0","WIN0b-RT35I0","BCNL0-RT1.2I0","LGTS1-RT11I0","MFPWF2-RT13I0","LGTS1-RT11I1","MFPWR1-RT14I0","LGTS1-RT11I2","BPRR3-RT4I0","LGTS3-L4T11I9","LGTS3-L4T11I10","LGTS3-L4T11I11","BCNS1-RT2I6","BCNS1-RT2I5","BCNS1-RT2I7","RAK3-RT15I0","BCNS1-RT2I12","BCNS1-RT2I11","BCNS1-RT2I10","BCNS1-RT2I9","BCNS1-RT2I8","MFPWF1-RT13I1","MFPWR1-RT14I1","SPL3-RT18I0"],"rPriceIDs":["P-CAGc","P-BARe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-HRNe","P-HRNe","P-BPRe","P-WINm","P-BCNe","P-LGTc","P-MFPe","P-LGTc","P-MFPm","P-LGTc","P-BPRm","P-LGTc","P-LGTc","P-LGTc","P-BCNm","P-BCNm","P-BCNm","P-RAKe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-MFPm","P-MFPm","P-SPLm"],"discountDict":{"BPRF2-RT3I0":False}}})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                           print(f"")


def penipu():
        data = json.dumps({"FunctionName":"PurchaseAccessories","FunctionParameter":{"bus":"JB-003","accToPurchase":["BPRF2-RT3I0","TRN4a-RT36I0","CAG3a-RT5I0","HRN3-RT9I0","HRN3-RT9I1","BCNS1-RT2I0","BCNS1-RT2I1","BCNS1-RT2I2","BCNS1-RT2I3","BCNL0-RT1.2I0","BCNS1-RT2I4","BCNS1-L0T2.10I15","BCNS1-L0T2.10I16","BCNS1-L0T2.10I19","BCNS1-L0T2.10I18","BCNS1-L0T2.10I17","BAR3-RT0I0","MFPWF2-RT13I0","LGTS3-RT11I0","LGTS3-RT11I1","MFPWR3-RT14I0","EXH4a-RT34I0","BPRR3-RT4I0","LGTS3-L4T11I10","LGTS3-L4T11I11","LGTS3-L4T11I9","LGTS3-RT11I7","LGTS3-RT11I3","BCNS1-RT2I8","BCNS1-RT2I12","BCNS1-RT2I11","BCNS1-RT2I10","BCNS1-RT2I9","SPL3-RT18I0","BCNS1-RT2I5","BCNS1-RT2I6","BCNS1-RT2I7","RAK3-RT15I0","WIN3a-RT35I0","MFPWF2-RT13I1","LGTS3-RT11I4","LGTS3-RT11I5","MFPWR3-RT14I1"],"pPriceIDs":["P-BPRe","P-TRNm","P-CAGe","P-HRNe","P-HRNe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BARe","P-MFPe","P-LGTc","P-LGTc","P-MFPe","P-EXHm","P-BPRm","P-LGTc","P-LGTc","P-LGTc","P-LGTc","P-LGTc","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-SPLm","P-BCNm","P-BCNm","P-BCNm","P-RAKe","P-WINe","P-MFPe","P-LGTc","P-LGTc","P-MFPe"],"accToRemove":["BPRF3-RT3I0"],"rPriceIDs":["P-BPRe"],"discountDict":{"BPRF2-RT3I0":False,"TRN4a-RT36I0":False,"CAG3a-RT5I0":False,"HRN3-RT9I0":False,"HRN3-RT9I1":False,"BCNS1-RT2I0":False,"BCNS1-RT2I1":False,"BCNS1-RT2I2":False,"BCNS1-RT2I3":False,"BCNL0-RT1.2I0":False,"BCNS1-RT2I4":False,"BCNS1-L0T2.10I15":False,"BCNS1-L0T2.10I16":False,"BCNS1-L0T2.10I19":False,"BCNS1-L0T2.10I18":False,"BCNS1-L0T2.10I17":False,"BAR3-RT0I0":False,"MFPWF2-RT13I0":False,"LGTS3-RT11I0":False,"LGTS3-RT11I1":False,"MFPWR3-RT14I0":False,"EXH4a-RT34I0":False,"BPRR3-RT4I0":False,"LGTS3-L4T11I10":False,"LGTS3-L4T11I11":False,"LGTS3-L4T11I9":False,"LGTS3-RT11I7":False,"LGTS3-RT11I3":False,"BCNS1-RT2I8":False,"BCNS1-RT2I12":False,"BCNS1-RT2I11":False,"BCNS1-RT2I10":False,"BCNS1-RT2I9":False,"SPL3-RT18I0":False,"BCNS1-RT2I5":False,"BCNS1-RT2I6":False,"BCNS1-RT2I7":False,"RAK3-RT15I0":False,"WIN3a-RT35I0":False,"MFPWF2-RT13I1":False,"LGTS3-RT11I4":False,"LGTS3-RT11I5":False,"MFPWR3-RT14I1":False}}})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['FunctionResult']
                                uang = chat['currentMoney']
                                #print(f"{red} [💵{red}] {yellow}KURAS UB->{green} -$500.000")
                                #print(f"{uang}")
                                ketik(uang)
                                ketik("sudah dikurangi 500.000")
 

def gxg():
        data = json.dumps({"ItemId":"DRI-003","VirtualCurrency":"RP","Price":10,"CatalogVersion":"driver-main","StoreId":"driver"})
        response = requests.post('https://4ae9.playfabapi.com/Client/PurchaseItem', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                           print(f"{backend_data}")


def teh():

    for i in range(jum):


                pass_missyu()
               # os.system("cls||clear")

def mampus():
    for i in range(blok):
             remove()
             penipu()

def ketik(c):
    for e in c + "\n" :
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.005)
system("clear")
kal = datetime.datetime.now()



def menu1():
    system("clear")
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0.002)

def warning():
    exit(f"DATA AKUN BUSSID ANDA GAGAL DIMUAT!")
def mxx():
        data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
        response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                print(parser)
                if parser['code'] == 401:
                        pass
                        warning()
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['InfoResultPayload']
                                uang= chat['UserVirtualCurrency']
                                money= uang['RP']
                                fff= chat['AccountInfo']
                                zzz= fff['TitleInfo']
                                www= zzz['TitlePlayerAccount']
                                saa= www['Id']
                                gcc= chat['AccountInfo']
                                id= gcc['TitleInfo']
                             #   you= id['DisplayName']
                                ketik(f"         {blue}╔═══════════════\033[1;33;41m • \033[1;37[ 𝙸𝙽𝙵𝙾 𝙰𝙺𝚄𝙽 \033[1;33m• \033[0m\033[{blue}═════════════════╗")
                                ketik(f"         {white} - Total_Money: {green}{money}        ")
                            #    ketik(f"         {white} - You_Id     : {green}{you}")
                                ketik(f"         {white} - Id_Kamu    : {green}{saa}      ")
                                ketik(f"         {blue}╚═════════════════════ - ════════════════════════╝")

print(f"{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(banner)
print(f"{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"   {yellow} - Credit {white}@JOKIBUSSID.       {yellow} - Script Type {white}Free")
print(f"""     {red} - Owner {white}Gapiapja          {red}       - Versi {white} 1.0 """)
print(f"{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"                     {white}- Welcome {username} -")
print(f"{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
mxxxx()
ketik("\033[0;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

def hack():
    rename()


headers['X-Authorization'] = auth
hack()

ketik(" {white} Di Pilih Salah Satu:")
ketik("{logo}")



contoh = input ("""{green}╭\033[1;33;41m • \033[1;37m❏ PILIH ❏\033[1;33m• \033[0m\033[
{green}╰───{yellow}▶""")


if contoh =="1":
   jum = int(input("{yellow}{green}[{red}◕ {yellow}◕ {red}◕{green}] {white}JUMLAH:{red} "))
   teh()
elif contoh =="0":
   jum = int(input("{yellow}{green}[{red}◕ {yellow}◕ {red}◕{green}] {white}JUMLAH:{red} "))
   ngopi()
elif contoh =="2":
   haya = int(input("{yellow}{green}[{red}◕ {yellow}◕ {red}◕{green}] {white}JUMLAH:{red} "))
   ngopii()
elif contoh =="3":
     gcg = int(input("{yellow}{green}[{red}◕ {yellow}◕ {red}◕{green}] {white}JUMLAH:{red} "))
     crot()
elif contoh =="4":
     blok = int(input("{yellow}{green}[{red}◕ {yellow}◕ {red}◕{green}] {white}JUMLAH:{red} "))
     ketik("GUNAKAN FITUR INI JIKA TERTIPU")
     mampus()



elif contoh =="5":

     gxg()
