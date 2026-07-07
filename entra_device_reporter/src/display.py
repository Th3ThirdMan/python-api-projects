def print_device_summary(devices):
    print()
    print("====================")
    print("Entra Device Report")
    print("====================")

    print()
    print(f"Total devices: {len(devices)}")

    if len(devices) == 0:
        print("No Entra devices found.")