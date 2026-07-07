import csv

def export_devices(devices):
    with open("reports/entra_devices.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Device Name",
            "Operating System",
            "OS Version",
            "Trust Type"
        ])

        for device in devices:
            writer.writerow([
                device.get("displayName"),
                device.get("operatingSystem"),
                device.get("operatingSystemVersion"),
                device.get("trustType")
            ])