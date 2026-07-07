def create_html_report(devices):
    with open("reports/entra__device_report.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <body>
        <h1>Entra Device Report</h1>
        <p>Total devices: {len(devices)}</p>
        """)
        
        
        if len(devices) == 0:
            f.write("""
                    <p> No Entra devices found.</p>
                    """)
            
            f.write("""
                    </body>
                    </html>
                    """)
        