import os
from woffu import Woffu
class Main:
    def run():
        print("Woffu Autologin Script\n")
        
        username=os.getenv('WOFFU_USER')
        password=os.getenv('WOFFU_PASS')

        client = Woffu(username, password)
        if(client.is_working_day_for_me()):
            if (client.sign_in()):
                return ("Success!")
            else:
                return ("Something went wrong when trying to log you in/out.")

if __name__ == "__main__":
    print(Main.run())