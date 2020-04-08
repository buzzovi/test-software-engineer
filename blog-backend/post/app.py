import json
import boto3
import json
import decimal
from decimal import Decimal
from boto3.dynamodb.conditions import Key, Attr
import os
import requests
import datetime
# import pytz

def utcnow():
    # return Decimal(datetime.datetime.now(tz=pytz.utc).timestamp())
    return Decimal(datetime.datetime.now().timestamp())

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
    """ List Post
    """

    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    table = dynamodb.Table('Blog')

    response = table.scan()


    return {
        "statusCode": 200,
        "body": json.dumps(response, indent=4, cls=DecimalEncoder),
    }

def post_create(event, context):

    user_name = event['queryStringParameters']['user_name']
    post_content = event['queryStringParameters']['post_content']
    image = "null"
    if event['queryStringParameters'].get('image'):
        image = event['queryStringParameters']['image']
    now_timestamp = utcnow()


    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    table = dynamodb.Table('Blog')
    table.put_item(
        Item={
            "id": f"{now_timestamp}-{user_name}",
            "content": post_content,
            "username": user_name,
            "comments": [],
            "image": image,
            "timestamp": now_timestamp
        }
    )
    response = table.get_item(
        Key={
            'id': f"{now_timestamp}-{user_name}"
        }
    )
    item = response['Item']

    return {
        "statusCode": 200,
        "body": json.dumps(item, indent=4, cls=DecimalEncoder),
    }

def post_delete(event, context):
    post_id = event['id']


    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('Blog')
    table.delete_item(
        Key={
            'id': post_id
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps(f"Deleted id: {post_id}", indent=4, cls=DecimalEncoder),
    }

def comment_create(event, context):
    post_id = event['id']
    user_name = event['user_name']
    comment = event['user_name']
    now_timestamp = datetime.datetime.now()

    comment_item = dict()
    comment_item["comment"] = comment
    comment_item["liked"] = "false"
    comment_item["timestamp"] = now_timestamp
    comment_item["username"] = user_name


    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('Blog')
    response = table.get_item(
        Key={
            'id': f"{now_timestamp}-{user_name}"
        }
    )
    item = response['Item']

    item['comments'].append(comment_item)

    table.update_item(
        Key={
            'id': f"{now_timestamp}-{user_name}"
        },
        UpdateExpression='SET comments = :val1',
        ExpressionAttributeValues={
            ':val1': item['comments']
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response, indent=4, cls=DecimalEncoder),
    }

def comment_delete(event, context):
    response = dict()
    return {
        "statusCode": 200,
        "body": json.dumps(response, indent=4, cls=DecimalEncoder),
    }