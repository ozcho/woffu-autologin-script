import os
from woffu import Woffu
from random import randint
from time import sleep

class Main:
        
    def run():
        print("Woffu Autologin Script\n")
        randomTime=randint(1,100)
        sleep(randomTime)
        username=os.getenv('WOFFU_USER')
        password=os.getenv('WOFFU_PASS')
        token=os.getenv('TELEGRAM_TOKEN')

        client = Woffu(username, password)
        if(client.is_working_day_for_me()):
            message="empty message"
            if (client.sign_in()):
                message=f"Correctly signed in/out. Waited {randomTime}"
                    
            else:
                message="Something went wrong when trying to log you in/out"
            
            if(token):
                chatId=os.getenv('TELEGRAM_CHATID')
                client.sendTelegram(token, chatId, message)
                
            return message

if __name__ == "__main__":
    print(Main.run())