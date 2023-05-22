import subprocess
import requests
import json

# Функция сканера хостов
def ping_sweep(network):
    """Ping sweep a network to determine available hosts"""
    ip_list = []
    for i in range(1, 255):
        ip = network + "." + str(i)
        # Run the ping command with a timeout of 1 second
        ping_output = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Check the output for successful ping response
        if "1 received" in str(ping_output.stdout):
            ip_list.append(ip)
    return ip_list

network = "192.168.1"
ip_list = ping_sweep(network)
print(ip_list)

# Функция запросов
def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()

    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )

post_request_payload = None
request_target = str(input("Target:"))
request_method = str(input("Method (GET|POST):"))
request_headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
if request_method == "POST":
    post_request_payload = str(input("Payload:"))

sent_http_request(request_target, request_method, request_headers, post_request_payload)
