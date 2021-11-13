import json
from main import Main

def lambda_handler(event, context):
    client=Main()
    message = client.run()

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
