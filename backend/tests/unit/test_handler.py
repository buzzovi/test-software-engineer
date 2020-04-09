import json

import pytest

from backend.hello_world import app
from backend.post import app as blog


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


def test_lambda_handler(apigw_event):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
    # assert "location" in data.dict_keys()


@pytest.fixture()
def post_create_event():
    """ Generates API GW Event"""

    return {'resource': '/postcreate', 'path': '/postcreate', 'httpMethod': 'POST', 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,en-US;q=0.9,hu;q=0.8', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'GB', 'content-type': 'text/plain;charset=UTF-8', 'Host': 'bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com', 'origin': 'http://localhost:3000', 'Referer': 'http://localhost:3000/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36', 'Via': '2.0 8759b407cd243e2e2c573d5db804d721.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'kuqLbzEHh1GkRuINUnxDGryOdFCmY6hnjCQ9GIWls1a0B0xfEaZMEw==', 'X-Amzn-Trace-Id': 'Root=1-5e8f59dd-596d37aaf8075b4e22b0c67c', 'X-Forwarded-For': '86.161.235.22, 70.132.46.140', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'], 'Accept-Language': ['en,en-US;q=0.9,hu;q=0.8'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['GB'], 'content-type': ['text/plain;charset=UTF-8'], 'Host': ['bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com'], 'origin': ['http://localhost:3000'], 'Referer': ['http://localhost:3000/'], 'sec-fetch-dest': ['empty'], 'sec-fetch-mode': ['cors'], 'sec-fetch-site': ['cross-site'], 'User-Agent': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'], 'Via': ['2.0 8759b407cd243e2e2c573d5db804d721.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['kuqLbzEHh1GkRuINUnxDGryOdFCmY6hnjCQ9GIWls1a0B0xfEaZMEw=='], 'X-Amzn-Trace-Id': ['Root=1-5e8f59dd-596d37aaf8075b4e22b0c67c'], 'X-Forwarded-For': ['86.161.235.22, 70.132.46.140'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'quxt3o', 'resourcePath': '/postcreate', 'httpMethod': 'POST', 'extendedRequestId': 'Kur6nE8rDoEFv1Q=', 'requestTime': '09/Apr/2020:17:22:37 +0000', 'path': '/Prod/postcreate', 'accountId': '531958541780', 'protocol': 'HTTP/1.1', 'stage': 'Prod', 'domainPrefix': 'bmpi7pfcqk', 'requestTimeEpoch': 1586452957429, 'requestId': '04c99c6a-75cf-4a0f-be93-410c7b4175e6', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '86.161.235.22', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36', 'user': None}, 'domainName': 'bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com', 'apiId': 'bmpi7pfcqk'}, 'body': '{"username":"cc","content":"ccc"}', 'isBase64Encoded': False}

def test_lambda_post_create(post_create_event):

    ret = blog.post_create(post_create_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "content" in ret["body"]
    assert data["content"] == "First Post"

@pytest.fixture()
def post_delete_event():
    """ Generates API GW Event"""

    return {
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "queryStringParameters": {
            "id": "1586388479.53417110443115234375-BZ"
        },
        "stageVariables": {
            "baz": "qux"
        }
    }

def test_lambda_post_delete(post_delete_event):

    ret = blog.post_delete(post_delete_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "Deleted id" in ret["body"]

@pytest.fixture()
def comment_create_event():
    """ Generates API GW Event"""

    return {
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "queryStringParameters": {
            "id": "1586388562.792418956756591796875-BZ",
            "user_name": "B",
            "comment": "Comment!!!2"
        },
        "stageVariables": {
            "baz": "qux"
        }
    }

def test_lambda_comment_create(comment_create_event):

    ret = blog.comment_create(comment_create_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "comment" in ret["body"]

@pytest.fixture()
def comment_delete_event():
    """ Generates API GW Event"""

    return {
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "queryStringParameters": {
            "id": "1586388562.792418956756591796875-BZ",
            "user_name": "B",
            "timestamp": "1586392147.67799091339111328125"
        },
        "stageVariables": {
            "baz": "qux"
        }
    }

def test_lambda_comment_delete(comment_delete_event):

    ret = blog.comment_delete(comment_delete_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "comments" in ret["body"]