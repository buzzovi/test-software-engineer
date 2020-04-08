import json
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

import os

# import requests

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def post_list(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)
    #     raise e

    # Create an S3 client
    # s3 = boto3.client('s3')
    # bucket_name = os.environ['blog-app-bz'] # Supplied by Function service-discovery wire

    # def handler(message, context):

    # # Add a file to your Object Store
    # response = s3.put_object(
    #     Bucket=bucket_name,
    #     Key='blog',
    #     Body='{}',
    #     ACL='public-read'
    # )
    # return response


    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    table = dynamodb.Table('blog')

    response = table.scan()


    return {
        "statusCode": 200,
        "body": json.dumps(response, indent=4, cls=DecimalEncoder),
    }

    # title = "The Big New Movie"
    # year = 2015

    # response = table.update_item(
    #     Key={
    #         'year': year,
    #         'title': title
    #     },
    #     UpdateExpression="set info.rating = :r, info.plot=:p, info.actors=:a",
    #     ExpressionAttributeValues={
    #         ':r': decimal.Decimal(5.5),
    #         ':p': "Everything happens all at once.",
    #         ':a': ["Larry", "Moe", "Curly"]
    #     },
    #     ReturnValues="UPDATED_NEW"
    # )

    # print("UpdateItem succeeded:")
    # print(json.dumps(response, indent=4, cls=DecimalEncoder))

def post_new(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    table = dynamodb.Table('blog')
    table.put_item(
        Item={
            "post-id": "1586341039-bz",
            "content": "First Post",
            "comments": [],
            "username": "bz",
            "image": "''",
            "timestamp": 1586341039
        }
    )
    response = table.scan()

    return {
        "statusCode": 200,
        "body": json.dumps(response, indent=4, cls=DecimalEncoder),
    }