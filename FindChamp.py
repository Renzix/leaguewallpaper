#!/usr/bin/python
print("Finding Champion...")

import requests, sys
#Riot API key will be encrypted using .ini file when/if I get a real one
API="RGAPI-82dff4b7-821a-4eac-bf66-19673c6ab364"

#Gets some variables from config
try:
    f=open("config.txt","r");
    config=f.readlines();
    f.seek(0);
    for line in config:
        if(line[0:11]=="LeagueName:"):
            leaguename=line.replace("LeagueName:","").replace("\n","");
        elif(line[0:7]=="Region:"):
            Region=line.replace("Region:","").replace("\n","").lower();
    f.close();
except FileNotFoundError:
    print("Config file not found")
    sys.exit(1);

#Turn Summoner name into Account ID
def findAccID(name):
    url="https://"+Region+".api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name+"?api_key="+API
    r=requests.get(url)
    if "accountId" in r.json():
        return r.json()["accountId"];
    else:
        return -1;
    
def findSumID(name):
    url="https://"+Region+".api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name+"?api_key="+API
    r=requests.get(url)
    if "id" in r.json():
        return r.json()["id"];
    else:
        return -1;

def CurrentGame(SumID):
    url="https://"+Region+".api.riotgames.com/lol/spectator/v3/active-games/by-summoner/"+str(SumID)+"?api_key="+API
    r=requests.get(url);
    try:
        r.json()["status"]["status_code"];
        return r.json()["status"]["status_code"]*-1;
    except KeyError:
        for person in r.json()["participants"]:
            if(person["summonerId"]==SumID):
                print("Currently in game")
                return person["championId"];
    return -1;

#Turn Champ ID into Champ name
def findChamp(ID):
    patch="7.17.2" #Make it find regions latest patch...
    url="http://ddragon.leagueoflegends.com/cdn/"+patch+"/data/en_US/champion.json" 
    r=requests.get(url)
    for key in r.json()["data"].items():
        if(ID==int(key[1]["key"])):
            return key[1]["name"];

#find SummonerID
SumID=findSumID(leaguename)
#if SumID doesnt exist exit with error
if(SumID==-1):
    print("Invalid name...");
    sys.exit(1);
print("Summoner ID:"+ str(SumID));

#find Account ID
AccID=findAccID(leaguename);
print("Account ID:"+str(AccID));

#if in current game return current champ
ChampName=findChamp(CurrentGame(SumID));
if(not ChampName):
    #get past 20 matches
    url="https://"+Region+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(AccID)+"/recent?api_key="+API
    r=requests.get(url);
    dic=r.json();
    ChampName=findChamp(dic["matches"][0]["champion"]);

#get rid of white space
ChampName=ChampName.replace(" ", "");
ChampName=ChampName.replace("'","");
#print out last played champ
print("Last played champ:"+ChampName)

#Reads and Writes to config file to find last played champion
try:
    f = open("config.txt","r+")
    config = f.readlines()
    f.seek(0)
    for line in config:
        if "CurrentChamp:" not in line:
            f.write(line);
        else:
            f.write("CurrentChamp:"+ChampName+"\n");
    f.truncate()
    f.close()
except FileNotFoundError:
    print("Config file not found. Run CreateConfig to write it.")
    sys.exit(1)


"""
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
"""

#Exit without error
print("Exiting...\n")
sys.exit(0)
