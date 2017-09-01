#!/usr/bin/python
__Main()__:
e
import requests, sys, subprocess, platform
#Riot API key
API="RGAPI-a63a35a1-baf0-4656-b68d-f3729490b356"

#Turn Summoner name into Account ID
def findID(name):
    url="https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name+"?api_key="+API
    r=requests.get(url)
    if "accountId" in r.json():
        return r.json()["accountId"]
    else:
        return -1;
    
#Turn Champ ID into Champ name
def findChamp(ID):
    url="http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json" 
    r=requests.get(url)
    for key in r.json()["data"].items():
        if(ID==int(key[1]["key"])):
            return key[1]["name"];


#finds league name from file or asks for it then puts it in a file
try:
    f=open("leaguename","r");
    leaguename=f.read().splitlines()[0];
except FileNotFoundError:
    leaguename=input("Please enter your username:");
    f=open("leaguename","w");
    f.write(leaguename);
    f.close;
print("League Name:"+leaguename)

#find Account ID
AccID=findID(leaguename);
#See if name is invalid
if(AccID==-1):
    print("Invalid name...");
    sys.exit(1);
print("Account ID:"+str(AccID));

#get past 20 matches
url="https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(AccID)+"/recent?api_key="+API
r=requests.get(url);
dic=r.json();
ChampName=findChamp(dic["matches"][0]["champion"]);
print("Last played champ:"+ChampName)

#Set wallpaper

#For i3 and other Basic window managers
if(platform.system()=="Linux"):
    bashCommand="feh --bg-scale /home/renzix/Wallpaper/"+ChampName+".jpg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

#for Windows 
if(platform.system()=="Windows"):
    import ctypes
    import os
    drive = "C:\\"
    folder = "Pictures\\LeagueWallpaper"
    image = ChampName+".jpg"
    image_path = os.path.join(drive, folder, image)
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)

#for Mac
if(platform.system()=="Mac"):
    print("Mac is not supported yet give me a minute");

#Exit without error
sys.exit(0)
