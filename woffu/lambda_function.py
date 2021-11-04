import json
from main import Main

def lambda_handler(event, context):
    message = Main.run()
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
