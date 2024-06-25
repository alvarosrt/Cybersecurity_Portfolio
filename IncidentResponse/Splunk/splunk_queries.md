# Splunk Queries and Analysis

This document provides sample Splunk queries and analysis techniques for incident response and security monitoring.

## Authentication Logs
Query to analyze authentication attempts:

```splunk
index=main sourcetype=auth (source=sshd OR source=login) failed OR success
| stats count by user, action
| sort -count
```

## Network Traffic Analysis
Query to monitor incoming and outgoing network traffic:

```splunk
index=main sourcetype=network_traffic src_ip=192.168.1.100 OR dest_ip=192.168.1.100
| stats sum(bytes) as TotalBytes by src_ip, dest_ip
| sort -TotalBytes
```

## Malware Detection
Query to detect potential malware infections:

```splunk
index=main sourcetype=malware_logs virus_detected=true
| table _time, host, signature, severity
```

## Incident Response Actions

### Alert Triggering
Create alerts based on query results to notify security teams:

```splunk
index=main sourcetype=web_logs status=500
| stats count by host, uri_path
| where count > 10
| eval message="Potential web server issue detected"
| sendalert "Web_Server_Alert"
```

### Investigation and Reporting
Generate detailed reports and dashboards for incident analysis:

```splunk
index=main sourcetype=incident_reports status=active
| stats count by category, severity
| sort -count
| dedup 10 category
| outputlookup active_incidents.csv
```

## Resources
- [Splunk Documentation](https://docs.splunk.com/)
- [Splunk Query Language](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/SearchReference)
