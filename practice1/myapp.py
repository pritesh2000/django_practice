import requests

URL = "http://localhost:8000/user/student_detail/"

r = requests.get(url = URL)

data = r.json()

print(data)