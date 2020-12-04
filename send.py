import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MDA0MTU3LCJqdGkiOiIzNDY3MThmZTcyMGE0ZjM1ODJlYzkzNWViMmFiNTViNyIsInVzZXJfaWQiOjF9._rwy1GzVwlGSgAW7_8NZnIFROmNINfnge-juzaK0vVQ'

r = requests.get("http://localhost:8000/api/profiles/", headers=headers)

print(r.text)