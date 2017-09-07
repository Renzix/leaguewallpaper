#!/usr/bin/python

import os, sys, platform, subprocess

try:
    f=open("config.txt","r");
    config=f.readlines();
    f.close();
except FileNotFoundError:
    print("Config file not found")
    sys.exit(1);

#search config file for champ
for line in config:
    if(line[0:13]=="CurrentChamp:"):
        ChampName=line.replace("CurrentChamp:","").replace("\n","");


#set up

OsName=platform.system();
if(OsName=="Linux"):
    if os.environ.get('KDE_FULL_SESSION') == 'true':
        print("KDE is not yet supported")
    elif os.environ.get("GNOME_DESKTOP_SESSION_ID"):
        print("Gnome not yet supported");
    else:
        #assuming we can use feh
        import pwd;
        username=pwd.getpwuid(os.getuid())[0];
        bashCommand="feh --bg-scale /home/"+username+"/.leaguewallpaper/"+ChampName+".jpg";
        process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE);

elif OsName in ["Windows","cygwin"]:
    print("Windows is not yet suppored");
elif(OsName=="darwin"):
    print("Mac is not yet supported");
else:
    print(OsName+" is not yet supported");
