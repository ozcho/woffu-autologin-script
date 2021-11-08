# woffu-autologin-script
This is a small script that auto checks you into your Woffu organization.

The point is to schedule this script so that it runs every day at the times you check in and out of work (i.e, 9 and 17)

I don't use it myself at the moment, and I only built it as a fun proof of concept - there are definitely a lot of 
improvements that could be made, rather easily too. However, it does work.

## Why?
A new law in my country is forcing people to check in and out of their jobs, every day at the same hours. Sounds to me
like a boring, useless chore that could be automated, and what is programming if not automating tasks to make our lifes easier.

## How to use
You need to configure WOFFU_USER and WOFFU_PASS as environment variables.

You need Python 3.6+ (f-strings rock!), and [the requests library](https://pypi.org/project/requests/).

You'll be prompted to enter your user and password the first time it starts, and that's it, you don't have to do anything else
but to execute the script whenever you want to log in or out.

## How to integrate in AWS Lambda
Open this link and find the region that your function is using:
https://github.com/keithrozario/Klayers/tree/master/deployments/python3.8/arns

Open the .csv related to your region and search for the requests row.
This is the ARN related to requests library:
arn:aws:lambda:us-east-1:770693421928:layer:Klayers-python38-requests:6

So now in your lambda function, add a layer using the ARN found.

Also need to add WOFFU_USER and WOFFU_PASS variables in configuration.
## Caveats
### Passwords
This forks substitutes the JSON credentials file in favor of environment variables.

Woffu [does have an API](https://www.woffu.com/wp-content/uploads/2019/07/Woffu-API-Document-Guide-en.pdf) your organization 
can probably use to log you in, or enable so that your user can have an API Key or something. The organization I used to test
this script doesn't so this script is the only way to do it, to my knowledge. If you want to use this script and you want it
to be compatible with your API Key instead of using your password (you should want to!), open an issue and I'll probably do it,
it should be really easy.

### Timezones
The timezone is hardcoded, and I've set it up to UTC+1. If you live in a different timezone, change 
the 'StartDate', 'EndDate' and 'TimezoneOffset' values in the signIn() function. 

### Telegram integration
If setted TELEGRAM_TOKEN and TELEGRAM_CHATID it will notify via telegram.
TELEGRAM_TOKEN is the telegram bot token
TELEGRAM_CHATID is the telegram chat id
You can set up your bot chatting with @BotFather and get your token.
Then you have to start a chat with your bot and send a /start command to it.
To get the chat id you can query (maybe via postman) this url https://api.telegram.org/bot{token}/getUpdates
