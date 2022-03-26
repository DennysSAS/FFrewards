#!/usr/bin/env python3
import argparse
from email import header
from os import access
from turtle import clear
from bs4 import BeautifulSoup
import requests
import rich
from rich import console


#parser = argparse.ArgumentParser()
#parser.add_argument("-c", "--codigin", help="codigin", dest="url", type=str, required=True)



#args = parser.parse_args()
#Inic_codigin = args.codigin
access_token = "a52706ffa41efaac9fe58dc65cc4db34a77555931e082df40f2fa1db234ed79a"
codigin = ""
paylod = {
"Cookie": "_ga=GA1.2.1580628210.1648270848; _gid=GA1.2.887630064.1648270848; apple_state_key=ff876a66acc111ecb16c2a644eab852a; token_session=efe81d9e7bbef6b7c36e6a89d6bc9100b549d5fdb479b633cc3544f5cd0c372b910fd334c10b28af4d4d8e745f9d5504",
"Accept": "application/json, text/plain, */*",
"Content-Type": "application/json",
"Access-Token": access_token,
"Content-Length": "31",
"Origin": "https://reward.ff.garena.com",
"Referer": "https://reward.ff.garena.com/",

}


url_google_login = "https://prod-api.reward.ff.garena.com/redemption/api/game/ff/multiple/redeem/"
google = requests.post(url_google_login, headers=paylod)
soup = (google.text)


print (soup)