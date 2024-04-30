import requests

free5gc_address = "30.0.0.1"
webconsole_port = 5000

subscribers_list: list = requests.get(
    url=f"http://{free5gc_address}:{webconsole_port}/api/subscriber",
    headers={"Token": "admin"},
).json()

for subscriber in subscribers_list:
    supi = subscriber.get("ueId")
    subscriber["details"] = requests.get(
        url=f"http://{free5gc_address}:{webconsole_port}/api/registered-ue-context/{supi}",
        headers={"Token": "admin"},
    ).json()

print(subscribers_list)