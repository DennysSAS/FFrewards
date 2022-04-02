#!/usr/bin/env python3
import time
import random
import string
import argparse
import requests
from rich import print
from rich.console import Console

requests.packages.urllib3.disable_warnings() # Aviso Desabilitado
console = Console()



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
token_tm = len(Inic_codigin)
tm_final = 12 - 2 - token_tm

def gerador_codingin():

    a = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    
    b = ''.join(random.choice(string.digits) for _ in range(1))
    
    c = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tm_final))

    return "{}{}{}{}".format(Inic_codigin, a, b, c)


def reques():
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
    
    while "error_invalid_serialno" in reques():
        console.print ("[red][-] Injetando Codigin:[/red] {}[red][-][/red]".format(gerador_codingin()), end="\r")
        time.sleep(0.1)
             
    if "error_too_many_requests" in reques():
        console.print ("\n[yellow][!] Muitas Tentativas [!][/yellow]")
        raise SystemExit
    
    if "expired" in reques():
        console.print("\n[yellow][!] Token Expirado [!][/yellow]")
        raise SystemExit 
    
    if "error_invalid_token" in reques():
        console.print("\n[yellow][!] Token Invalido [!][/yellow]", )
        raise SystemExit
    
    if "Success" in reques():
        console.print ("\n[green][+] Codigin Encontrado:[/green] {}[green][+][/green]".format(gerador_codingin()))
        console.print ("\n",reques())
    
    else:
        raise SystemExit
def logo():
                                                                                                                                                               
    logo_ascci =  """[green]
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&JY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
555555555555#@P55555555PG#@@@@@P55555555555&&55555555555P@@@@@@#55555555555P&@@@@B!~!#@@@@&PPPPPPPPPPG#@@@@&555555555555
            5@.           ^?#@&.           GG           .&@@@@@P            #@@@@7~~~J@@@@B           .^J&@G            
      ..... P@:    .^:.     :B&:           GG           :&@@@@@P           .#@@@&!~~~?@@@@B     .:.      ^&G            
     7######&&:    7@@#J     !&:    !##BBBB@G     J#BBBB#@@@@@@P     5######@@@@@P!~~?@@@@B     5&&B~     5B     J#BBBBB
     7&&&&&&@&:    7@@@B     !&:    !@&&&&&@G     Y@&&&&@@@@@@@P     P&&&&&@@@@@@G!~~?@@@@B     P@@@5     YB     Y@&&&&@
      .....?@&:    ~PPJ:     G@:    .::::.^@G     .::::.7@@@@@@P     ......P@@@@@G!~~?@@@@B     ?P5?.    :#G     .::::.!
           !@&:           .~G@&:          .&G           !@@@@@@P           5@@@@@G!~~?@@@@B            :7#@G           ~
     ~YYYYYG@&:    :     !#@@@&:    ^YYYYY5@G     7YYYYYP@@@@@@P     75YYYY#@@@#J7~~~!Y@@@B     :     ?&@@@G     !YYYYYP
     ?@@@@@@@&:    ?G.    ~B@@&:    7@@@@@@@G     P@@@@@@@@@@@@P     P@@@@@@@@@@B!~~~Y&@@@B     Y5     7&@@G     P@@@@@@
P?   7@@@@@@@&:    7@B~7.:..5@&:    :777!??#G     ^7777??&@@@@@&5~   P@@@@@@@@@@@7~~~G@@@@B     Y@G~?.^ :G@G     ^7777?7
@@5^ J@@@@@@@&?BBY^J@@@@PB#G#@&..^:^~  :7GB&B :^:~^  ^?#B&@@@@@@@&J. P@@@@@@@@@@&7~Y?P@@@@GJ#G?:5@@@@G&BP#@G :^:~^  ^?#G
@@@PY#@@@@@@@@&@@@@@@@@@@@@@@@@J5@&@@GB#@@@@&?B@&@@PB&@@@@@@@@@@@@@P5@@@@@@@@@@@@PPG5#@@@@&@@@@@@@@@@@@@@@@#7B@&@@PB&@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[/green]"""


    print (logo_ascci)



logo()
validacao()