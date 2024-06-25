## Suricata
###  Intrusion Detection System (IDS)

**Project Description:**

Suricata is an open-source intrusion detection system (IDS), intrusion prevention system (IPS), and network security monitoring tool. It monitors network traffic, detects suspicious activities, and generates alerts for potential intrusions.

**Technologies Used:**
```
    - Suricata
    - IDS/IPS rules (e.g., custom.rules)
    - Packet capture files (e.g., sample.pcap)
    - Event log analysis tools (e.g., `jq` for `eve.json`)
```

**Project Highlights:**

- **IDS Mode:**
  - Monitors network traffic and alerts on suspicious activities based on predefined rules.
  
- **IPS Mode:**
  - Not only detects but also actively blocks malicious traffic based on configured rules.

- **Network Security Monitoring (NSM):**
  - Provides comprehensive network telemetry through detailed event logs like `eve.json`.

- **Signature-based Detection:**
  - Uses signature analysis to detect specific patterns in network traffic.
  - Components of a signature include action, header (network traffic details), and rule options.



**Screenshots and Diagrams:**
*working*

**Configuration and Usage:**

1. **Setup:**
   - Install Suricata on your system (e.g., `sudo apt install suricata`).
   - Configure Suricata to monitor network interfaces (`suricata -c /etc/suricata/suricata.yaml -i eth0`).

2. **Custom Rules:**
   - Create custom rules in `custom.rules` file to define specific behaviors and alerts.
   - Example rule:
     ```
     alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; http_method; sid:12345; rev:3;)
     ```

3. **Testing Rules:**
   - Use packet capture files (`sample.pcap`) to simulate network traffic.
   - Run Suricata with custom rules (`sudo suricata -r sample.pcap -S custom.rules -k none`).
   - Monitor output in `fast.log` for quick alerts and `eve.json` for detailed event logs.

4. **Analyzing Alerts:**
   - View alerts generated in `fast.log` for immediate actions.
   - Analyze detailed event logs in `eve.json` using tools like `jq` for specific event details.

5. **Custom Script (`ids_analysis.py`):**
   - Use Python script `ids_analysis.py` for further analysis and automation of IDS alerts.
   - Example functionality includes parsing `fast.log` and `eve.json` for specific alerts or patterns.

**Conclusion:**
Suricata provides robust capabilities for network intrusion detection and prevention, essential for maintaining network security and responding to potential threats effectively.