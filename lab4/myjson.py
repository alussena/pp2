import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-" * 80)


for item in data['imdata']:
    dn = item['l1PhysIf']['attributes']['dn']
    speed = item['l1PhysIf']['attributes']['speed']
    mtu = item['l1PhysIf']['attributes']['mtu']
    

    print(f"{dn:<50} {speed:<20} {mtu:<10}")
