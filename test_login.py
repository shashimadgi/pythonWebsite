from pydoc import html

import pytest
import requests


@pytest.mark.loginFlow(html)
def test_send_otp_validation():
    payload = {
        "phone": "+917243464979",
        "isSignup": True,
        "deviceInfo": {
            "APP_TYPE": "android",
            "DeviceData": {
                "deviceUID": {
                    "_h": 0,
                    "_i": 3,
                    "_j": {
                        "_h": 0,
                        "_i": 1,
                        "_j": "36e27f877d1a7c24",
                        "_k": None
                    },
                    "_k": None
                },
                "installReferrer": {
                    "_h": 0,
                    "_i": 1,
                    "_j": "utm_source=google-play&utm_medium=organic",
                    "_k": None
                },
                "carrier": {
                    "_h": 0,
                    "_i": 1,
                    "_j": "",
                    "_k": None
                },
                "manufacturer": {
                    "_h": 0,
                    "_i": 1,
                    "_j": "realme",
                    "_k": None
                },
                "ipAddress": {
                    "_h": 0,
                    "_i": 1,
                    "_j": "192.168.57.66",
                    "_k": None
                },
                "model": "RMX3501",
                "firstInstallTime": {
                    "_h": 0,
                    "_i": 1,
                    "_j": 1689061417338,
                    "_k": None
                },
                "androidVersion": {
                    "_h": 0,
                    "_i": 1,
                    "_j": 31,
                    "_k": None
                },
                "width": 360,
                "height": 724,
                "hasNotch": False
            }
        }
    }
    header = {
        'gameid': 'bgmi',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    }
    base_url = 'https://stage-api.getstan.app'
    response = requests.post(url=base_url + '/api/v1/auth/otp/send', headers=header, json=payload)

    data = response.json()

    if response.status_code == 200:
        assert response.status_code == 200
        print(data)
    else:

        assert response.status_code == 401
        print(response.text)
        assert response.status_code == 500
        print(response.text)
        assert response.status_code == 201
        print(response.text)


@pytest.mark.loginFlow(html)
def test_verify_otp_validation():
    payload = {
        "phone": "+919999999999",
        "otp": "5555",
        "deviceInfo": {
            "APP_TYPE": "android",
            "DeviceData": {
                "deviceUID": "36e27f877d1a7c25"
            }
        },
        "utmPayload": {},
        "campaignUrl": "",
        "sessionId": None,
        "referralCode": None,
        "provider": ""
    }
    header = {
        'gameid': 'bgmi',
        'Content-Type': 'application/json'
    }
    base_url = 'https://stage-api.getstan.app'
    response = requests.post(url=base_url + '/api/v4/verify/otp', headers=header, json=payload)

    data = response.json()

    if response.status_code == 200:
        assert response.status_code == 200
        print(data)
    else:

        assert response.status_code == 401
        print(response.text)
        assert response.status_code == 500
        print(response.text)
        assert response.status_code == 201
        print(response.text)


@pytest.mark.loginFlow(html)
def test_select_game_validation():
    payload = {
        "gameId": "freefire",
        "referralCode": "SHHDJDDJD"
    }
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'GameId': 'freefire',
        'AppVersion': '94',
        'Platform': 'android',
        'SID': '1689061440422-74140',
        'TS': 'undefined',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIwNjAyNTAsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzcxLCJpYXQiOjE3MDE5NzM4NTAsImlkIjoiNzIxNiJ9.GrUMQF-Lv-jjLN4D04hLjEUcePLphSiWCxseRstPoLw'
    }
    base_url = 'https://stage-api.getstan.app'
    response = requests.post(url=base_url + '/api/v4/select/game', headers=header, json=payload)

    data = response.json()

    if response.status_code == 200:
        assert response.status_code == 200
        print(data)
    else:

        assert response.status_code == 401
        print(response.text)
        assert response.status_code == 500
        print(response.text)
        assert response.status_code == 201
        print(response.text)
# @pytest.mark.purchase(html)
# def test_getRequest_validation():
#     payload = ''
#     header = {
#         'Accept': 'application/json, text/plain, */*',
#         'GameId': 'freefire',
#         'AppVersion': '93',
#         'Platform': 'android',
#         'SID': '1700203652887-35153',
#         'TS': 'undefined',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo0NzAyLCJleHAiOjE3MDE5NzE2OTUsImZyZWVmaXJlUHJvZmlsZUlkIjo0NjY2LCJpYXQiOjE3MDE4ODUyOTUsImlkIjozMjY1fQ.pyjqAJGisL5V5JdazWs-XVeZn0BZTJfsk6-bUljzOhQ',
#     }
#     base_url = 'https://stage-api.getstan.app'
#     response = requests.get(url=base_url + '/api/v3/user/coins', headers=header, json=payload)
#
#     data = response.json()
#
#     if response.status_code == 200:
#         assert response.status_code == 200
#         print(data)
#     else:
#
#         assert response.status_code == 401
#         print(response.text)
#         assert response.status_code == 500
#         print(response.text)
#         assert response.status_code == 201
#         print(response.text)
#
#
# @pytest.mark.purchase(html)
# def test_postRequest_validation():
#     header = {
#         'Accept': 'application/json, text/plain, */*',
#         'Content-Type': 'application/json',
#         'GameId': 'freefire',
#         'gaid': '9af1c2ff-4a28-4032-ae0c-b256b9258fe8',
#         'AppVersion': '93',
#         'Platform': 'android',
#         'SID': '1700203652887-35153',
#         'TS': 'undefined',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo5MzMzLCJleHAiOjE3MDA4OTk5OTAsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzMwLCJpYXQiOjE3MDA4MTM1OTAsImlkIjo3MTE3fQ.c7qJHir63P6Ldldgkm3ZqEdsEFyM0_kIKuEbCUBljEE'
#     }
#     payload = {
#         "developerPayloadAndroid": "",
#         "packageNameAndroid": "com.getstan",
#         "purchaseStateAndroid": 1,
#         "obfuscatedProfileIdAndroid": "",
#         "autoRenewingAndroid": False,
#         "isAcknowledgedAndroid": False,
#         "signatureAndroid": "JSUv/y12FPyYruanuRtjtYJVGAu2agHHWhINP/vVGZB/g0ly0P4tgeY/TLhM1zXHKLIHIJ/GE25/mnlhb2UU6ECFOFH5ewf+6TVk3a+DF2NDKcZYChUOHhljlh7j6dnWD+ksWS+AbzioNEPUEplV5ew1ST6kmXTojigHb9kJ6LZzftjjhQz2+5rGacSZTG3HDmhWVc2W4DzSQ2U7x1HUl2ZEkew4y/0nVYXolaBnhoNJJQ5lIE7+zpNErR8O+/hccK+qBaa/BCvUTSJcUPhG/N1WEoFat39g2l+jQxC7oCPEKE0bOPjW5B7bxO3YXCznabh8Mi2kc6C/YW1aBh3omw==",
#         "dataAndroid": "{\"orderId\":\"GPA.3370-4777-4107-58866\",\"packageName\":\"com.getstan\",\"productId\":\"coins_500\",\"purchaseTime\":1700203704669,\"purchaseState\":0,\"purchaseToken\":\"kbgdljnmggdjnfnmnepidajp.AO-J1OzBLK47BTLWuiDuZDC5kvb5LzisZ7_Ebdf-VWnAVPDTqJppbF9GBsSONoFy3YG9BMIJ7VfH9EugMQX3ioTUTw8pYtIL3Q\",\"quantity\":1,\"acknowledged\":false}",
#         "obfuscatedAccountIdAndroid": "",
#         "productId": "coins_500",
#         "transactionReceipt": "{\"orderId\":\"GPA.3370-4777-4107-58866\",\"packageName\":\"com.getstan\",\"productId\":\"coins_500\",\"purchaseTime\":1700203704669,\"purchaseState\":0,\"purchaseToken\":\"kbgdljnmggdjnfnmnepidajp.AO-J1OzBLK47BTLWuiDuZDC5kvb5LzisZ7_Ebdf-VWnAVPDTqJppbF9GBsSONoFy3YG9BMIJ7VfH9EugMQX3ioTUTw8pYtIL3Q\",\"quantity\":1,\"acknowledged\":false}",
#         "transactionId": "GPA.3370-4777-4107-58866",
#         "transactionDate": 1700203704669,
#         "purchaseToken": "kbgdljnmggdjnfnmnepidajp.AO-J1OzBLK47BTLWuiDuZDC5kvb5LzisZ7_Ebdf-VWnAVPDTqJppbF9GBsSONoFy3YG9BMIJ7VfH9EugMQX3ioTUTw8pYtIL3Q",
#         "productIds": [
#             "coins_500"
#         ]
#     }
#
#     base_url = 'https://stage-api.getstan.app'
#     response = requests.post(url=base_url + '/api/v1/google-purchases/verify', headers=header, json=payload)
#
#     data = response.json()
#
#     if response.status_code == 201:
#         assert response.status_code == 201
#         print(data)
#     else:
#
#         assert response.status_code == 401
#         print(response.text)
#         assert response.status_code == 500
#         print(response.text)
#         assert response.status_code == 200
#         print(response.text)
#
#
# @pytest.mark.purchase(html)
# def test_checkRequest_validation():
#     payload = ''
#     header = {
#         'Accept': 'application/json, text/plain, */*',
#         'GameId': 'freefire',
#         'AppVersion': '93',
#         'Platform': 'android',
#         'SID': '1700203652887-35153',
#         'TS': 'undefined',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo5MzMzLCJleHAiOjE3MDA4OTk5OTAsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzMwLCJpYXQiOjE3MDA4MTM1OTAsImlkIjo3MTE3fQ.c7qJHir63P6Ldldgkm3ZqEdsEFyM0_kIKuEbCUBljEE'
#     }
#     base_url = 'https://stage-api.getstan.app'
#     response = requests.get(url=base_url + '/api/v3/user/coins', headers=header, json=payload)
#
#     data = response.json()
#
#     if response.status_code == 200:
#         assert response.status_code == 200
#         print(data)
#
#     else:
#
#         assert response.status_code == 401
#         print(response.text)
#         assert response.status_code == 500
#         print(response.text)
#
#         assert response.status_code == 201
#         print(response.text)
