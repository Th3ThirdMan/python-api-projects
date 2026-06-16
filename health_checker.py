import requests
import time
import csv
from datetime import datetime


with open("urls.txt", "r") as file:
    urls = file.read().splitlines()

print(urls)

results = []
csv_rows = []
up_count = 0
error_count = 0

for line in urls:
    name, url = line.split(",")
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()
        response_time = round(end_time - start_time, 2)
        
        if response.status_code == 200:
            print(url, "- UP")
            results.append(f"{name} - UP - {response_time}s")
            csv_rows.append([name, "UP", response_time])
            up_count += 1
        else:
            print(url, "-DOWN")
            results.append(f"{name} - DOWN")
            csv_rows.append([name, "DOWN", ""])
            
    except Exception:
        print(url, "-ERROR")
        results.append(f"{name} - ERROR")
        csv_rows.append([name, "ERROR", ""])
        error_count += 1
        
timestamp = datetime.now() 
report_name = f"health_report_{timestamp.strftime('%Y%m%d_%H%M%S')}.txt"      
with open(report_name, "w") as file:
    csv_name = f"health_report_{timestamp.strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(csv_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Service", "Status", "Response Time"])
        for row in csv_rows:
            writer.writerow(row)
        
        file.write(f"Health Check Report\n")
        file.write(f"Generated: {timestamp}\n\n")
    
    for result in results:
        file.write(result + "\n")
        
    file.write("\n*** Summary ***\n")
    file.write(f"UP: {up_count}\n")
    file.write(f"ERROR: {error_count}\n")
    