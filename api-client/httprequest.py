

import requests
url = "http://localhost:8000/emp_detail/1"

response=requests.post(url)
details=response.json()
print(details)


