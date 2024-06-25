import splunklib.client as client
import splunklib.results as results
import datetime

# Splunk server configuration
SPLUNK_HOST = 'https://splunk.example.com'
SPLUNK_USERNAME = 'your_username'
SPLUNK_PASSWORD = 'your_password'

# Example query parameters
QUERY = 'index=main sourcetype=syslog earliest=-24h'
ALERT_THRESHOLD = 10

def fetch_alerts():
    try:
        service = client.connect(host=SPLUNK_HOST, username=SPLUNK_USERNAME, password=SPLUNK_PASSWORD)
        job = service.jobs.create(QUERY)
        while not job.is_ready():
            pass
        job_results = results.ResultsReader(job.results())
        alerts = [result for result in job_results if int(result.get('count', 0)) >= ALERT_THRESHOLD]
        return alerts
    except Exception as e:
        print(f"Error fetching alerts from Splunk: {str(e)}")
        return []

def process_alerts(alerts):
    for alert in alerts:
        timestamp = alert.get('_time', 'Unknown')
        source = alert.get('host', 'Unknown')
        severity = alert.get('severity', 'Unknown')
        message = alert.get('_raw', 'No message')
        print(f"Alert: {timestamp} - {source} - Severity: {severity} - Message: {message}")

if __name__ == "__main__":
    alerts = fetch_alerts()
    if alerts:
        print(f"Fetched {len(alerts)} alerts from Splunk.")
        process_alerts(alerts)
    else:
        print("No alerts fetched from Splunk.")