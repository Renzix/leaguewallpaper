#!/usr/bin/python

import platform, os, sys, subprocess

#set up

OsName=sys.platform();
if(OsName=="linux"):
    if os.environ.get('KDE_FULL_SESSION') == 'true':
        print("KDE is not yet supported")
    elif os.environ.get("GNOME_DESKTOP_SESSION_ID"):
        print("Gnome not yet supported");
    else:
        #assuming we can use feh
        import pwd;
        username=pwd.getpwduid(os.getuid())[0];
        print("Username:"+username);
        bashCommand="feh--bg-scale /home/"+username+"/.leaguewallpaper/"+ChampName+".jpg";
        process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE);)

elif OsName in ["win32","cygwin"]:
    print("Windows is not yet suppored");
elif(OsName=="darwin"):
    print("Mac is not yet supported")
else:
    print(OsName+" is not yet supported");
