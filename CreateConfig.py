#!/usr/bin/python
f=open("config.txt", "w");
f.write("LeagueName:"+input("Enter your Username: ")+"\n");
f.write("CurrentChamp:Veigar\n");
f.write("Region:");
Region=input("Enter Region:");
if(Region=="North America"||Region=="NA"):
    f.write("NA1");
elif(Region=="Europe West"||Region=="EUW"):
    f.write("EUW1");
elif(Region=="Europe North East"||Region=="EUNE"):
    f.write("EUN1");
elif(Region=="Brazil"||Region=="BR"):
    f.write("BR1");
elif(Region=="Japan"||Region=="JP"):
    f.write("JP1");
elif(Region=="Korea"||Region=="KR"):
    f.write("KR");
elif(Region=="Latin America North"||Region=="LAN"):
    f.write("LA1");
elif(Region=="Latin America South"||Region=="LAS"):
    f.write("LA2");
elif(Region=="Oceania"||Region=="OCE"):
    f.write("OC1");
elif(Region=="Turkey"||Region=="TR"):
    f.write("TR1");
elif(Region=="Russia"||Region=="RU"):
    f.write("RU");
elif(Region=="Public Beta Environment"||Region=="PBE"):
    f.write("PBE1");
else
    print("Error finding region please Enter the initals of your region in capital letters ie NA or EUW");
f.close();
