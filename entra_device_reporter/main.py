from src.auth import get_token
from src.devices import get_devices

token = get_token()
devices = get_devices(token)

print(devices)

print(f"Retrieved {len(devices)} devices")