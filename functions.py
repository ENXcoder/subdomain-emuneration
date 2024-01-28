import requests
def request(url):
        try:
            result=requests.get("https://"+url)
            if(result):
                print(f"[+]Subdomain discovered------->{url}")
        except:
            print(f"[+]{url} NOT FOUND")
            pass

def main():
            target_url=input("[+]Enter target url\n[+]example:google.com\n[+]----->")
            with open("subdmainwordlist.txt","r") as wordlist:
                    for line in wordlist:
                        word=line.strip()
                        test_url=word+"."+target_url
                        request(test_url)