#!/usr/bin/python

import requests, sys, subprocess, platform
#Riot API key
API="RGAPI-795e8bce-90c0-494d-ad67-96098278e832"
#Turn Summoner name into Account ID
def findID(name):
    url="https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name+"?api_key="+API
    r=requests.get(url)
    print(name);
    if "accountId" in r.json():
        print(r.json()["accountId"]);
        return r.json()["accountId"];
    else:
        return -1;
    
#Turn Champ ID into Champ name
def findChamp(ID):
    patch="7.17.2"
    url="http://ddragon.leagueoflegends.com/cdn/"+patch+"/data/en_US/champion.json" 
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
    print("OS:Linux");
    import pwd
    import os
    username=pwd.getpwuid( os.getuid() )[ 0 ];
    print("Username:"+username);
    bashCommand="feh --bg-scale /home/"+username+"/.leaguewallpaper/"+ChampName+".jpg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

#for Windows 
if(platform.system()=="Windows"):
    print("OS:Windows")
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
    print("OS:Mac")
    print("Mac is not supported yet give me a minute");

#Exit without error
sys.exit(0)
