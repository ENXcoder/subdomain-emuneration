import requests
import functions
print("T̴̛̹̮͔͓͗͛͆̇ͅD̴͍̜̺̤̀̿̊͊͘͜R̶̡̠̝̝̥̾̊̒͋͝ ̷͕̩̙̣̜̐̒̐̚͠S̶̲̙̤̪͇͒̌͗̇͆U̸̲̹̼̘͓͊̍̍̽̊B̴̧̧̟̞̼̽͑̈́̊͝D̷̙͙̟̫͎͒̋̅͗͝Ỏ̸̡̢̦̝̩̑͊̀́M̶̡̫̼̺̦͛̑͆̉̆Ä̸͚͉̤͕̠͆̈̒̾I̶̢͕͙̩̋̀͆͛̒͜Ǹ̷̯̻͉̼͇͌͘̕̚ ̷̼̺̼̩͇̈̾̇̇͘Ȇ̴̡̱̩̝̈́̑̌̆͜Ṋ̷̢̖̞͙̊́͗̓̀Ű̷̲̫̜̝̑̅̾̿ͅM̵͕̮͎͔͓̒̓̀́̚E̸̜̪̫̗͖͐̈́̓̈̇Ŗ̷̩̭̼͉̈́̿̀̅̕Ą̶̨̤̙̳̃̈̆̂̉T̴͙̹̺̹̞͗̊̐́̏Î̴̢̠̞̘̘̓̾̚͘O̸̜̤͉͙̮̐̉͛̈́̚N̶̠̮͔̻̤̈́͗͊͠ \n   DEVELOPER:ARNOLD")
y=input("[+]START OR STOP\n[+]YES\n[+]NO\n[+]>>")
opt=y.lower()
if opt=="yes" or "y":
    s=input("[+]+Do you want to start with default subdomain list??\n>>[YES]\n>>[NO]\n>>")
    opt2=s.lower()
    if opt2=="yes" or opt2=="y":
        functions.main()
    else:
        target=input("[+]Enter target url\n[+]example:google.com\n[+]----->")
        file=input("[+]Enter the subdomain list file\n[+]>>")
        try:
            with open(file,"r") as sublist:
                for line in sublist:
                    word=line.strip()
                    testurl=word+"."+target
                    functions.request(testurl)
        except FileNotFoundError:
            print(f"File '{file}' not found.")

else:
     print("[+]Program Ended")