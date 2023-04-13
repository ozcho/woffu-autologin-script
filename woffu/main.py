import os
from woffu import Woffu
from random import randint
from time import sleep

class Main:
    
    def __init__(self):
        self.sendMessage=True
        self.token=False


    def shouldSendMessage(self):
        if(not self.token):
            return False
        if(os.getenv("WOFFU_DEBUG")):
            return True
        return self.sendMessage
        
    def run(self):
        print("Woffu Autologin Script\n")
        randomTime=randint(1,120)
        sleep(randomTime)
        username=os.getenv('WOFFU_USER')
        password=os.getenv('WOFFU_PASS')
        self.token=os.getenv('TELEGRAM_TOKEN')

        client = Woffu(username, password)
        message="empty message"
        if(client.is_working_day_for_me()):
            
            try:
                client.sign_in()
                message="✅Correctly signed in/out.✅"
            except Error:
                message="❌Something went wrong when trying to log you in/out.❌"
        else:
            message="🎉🎊No working day for you!🎊🎉"
            self.sendMessage=False
        if(self.shouldSendMessage()):
            chatId=os.getenv('TELEGRAM_CHATID')
            message=f'''{message}
                    🕰️Wait {randomTime} seconds🕰️'''
            client.sendTelegram(self.token, chatId, message)
           
            
        return message

if __name__ == "__main__":
    c=Main()
    print(c.run())
