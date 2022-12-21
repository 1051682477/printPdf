import requests


def oil_login():
    url = 'http://192.168.0.157:9030/auth/gov/staff/editPwd'
    data = {"newPwd": 123456,
            "checkPass": 123456,
            "oldPwd": 123456
            }
    header = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqc29uIjoie1wic3RhZmZJZFwiOjE5NCxcInN5c3RlbVwiOlwiZ292XCJ9In0.dz3wz9qh-CpwokEQbXrEsoxasN78caVak2Ad3fscKeY",
              "sourceType": "2"
              }
    r = requests.post(url=url, data=data, headers=header)
    print(r.json())


if __name__ == '__main__':
    oil_login()
