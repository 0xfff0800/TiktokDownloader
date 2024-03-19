import time
import requests
from load import *
from core import Core

api = "https://api.telegram.org/bot" + TokenBot 
update_id = 0

def main():
    try:
        print("[+] Bot is active!")
        print("[+] Press Ctrl + C to exit!")
        res = requests.get(f"{api}/getme")
        bot_name = res.json().get('result', {}).get('first_name', 'Unknown Bot')
        print(f"[+] Bot name: {bot_name}")
        print('~' * 40)
        
        while True:
            try:
                req = requests.get(f"{api}/getupdates", params={"offset": update_id}).json()
                if not req.get('ok', False):
                    print("[-] Error in getting updates.")
                    continue
                
                results = req.get('result', [])
                if len(results) == 0:
                    continue

                update = results[0]
                Core(update)
                update_id = update.get('update_id', 0) + 1
                print("~" * 40)
                
            except ConnectionError:
                print('- Connection error! Retrying in 5 seconds...')
                time.sleep(5)
                continue
                
    except KeyboardInterrupt:
        print("\n[+] Exiting...")
        exit()

if __name__ == "__main__":
    main()
