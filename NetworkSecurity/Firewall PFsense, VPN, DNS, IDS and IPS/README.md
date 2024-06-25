# PFSense

**Project Description:**

pfSense is an open-source firewall and router software distribution based on FreeBSD. It is commonly deployed as a perimeter firewall, router, DHCP server, DNS server, and VPN endpoint. This project demonstrates the configuration and deployment of pfSense in a network environment to enhance security and network management capabilities.

**Technologies Used:**
``` 
- pfSense
- FreeBSD
- OpenVPN
- Snort
- pfBlockerNG
```

**Project Highlights:**

- **Firewall Configuration:**
  - Configured firewall rules to control traffic flow between different network segments.
  - Implemented NAT (Network Address Translation) to allow internal devices to access the internet securely.

- **VPN Setup:**
  - Established a secure VPN (Virtual Private Network) using OpenVPN for remote access.
  - Configured VPN clients to connect securely to the internal network from remote locations.

- **DHCP and DNS Services:**
  - Configured DHCP (Dynamic Host Configuration Protocol) to dynamically assign IP addresses to devices on the network.
  - Set up DNS (Domain Name System) to resolve domain names to IP addresses within the network.

- **Traffic Monitoring and Logging:**
  - Utilized pfSense's built-in monitoring tools to track network traffic and identify potential security threats.
  - Configured logging to record firewall events and traffic statistics for analysis.

- **Security Enhancements:**
  - Implemented IDS (Intrusion Detection System) and IPS (Intrusion Prevention System) using Snort to detect and block malicious activities.
  - Configured pfBlockerNG to block known malicious IP addresses and domains.

- **Explanation of Files**
    **firewall_rules.md**

    This file provides an overview of firewall rules configuration in pfSense:
    - Describes different types of rules and common actions.
    - Includes examples of rules and recommended practices for configuring and optimizing custom rules.
    - Provides links to additional resources for more detailed configuration.

- **pfsense_config.txt**

    This file details the basic configuration of pfSense, covering:
    - Network configuration, firewall rules, services, and VPN setup.
    - Offers an overview of system configuration and maintenance.
    - Provides troubleshooting tips and additional assistance through community and online resources.

**Screenshots and Diagrams:**
*Working.*

**Installation and Configuration Steps:**

1. **Download pfSense:**
   - Download the latest version of pfSense from the [official website](https://www.pfsense.org/download/).

2. **Install pfSense:**
   - Create a bootable USB drive with the pfSense ISO image.
   - Boot the target device from the USB drive and follow the installation instructions.

3. **Initial Setup:**
   - Access the pfSense web interface via a web browser.
   - Complete the initial setup wizard to configure basic settings such as the LAN IP address and admin credentials.

4. **Configure Firewall Rules:**
   - Navigate to the Firewall > Rules section to define rules for allowing or blocking traffic.

5. **Set Up VPN:**
   - Go to VPN > OpenVPN to configure the VPN server and client settings.

6. **Enable DHCP and DNS Services:**
   - Configure DHCP settings under Services > DHCP Server.
   - Set up DNS resolver under Services > DNS Resolver.

7. **Enable Traffic Monitoring:**
   - Access Status > Traffic Graph to monitor real-time network traffic.

8. **Configure IDS/IPS:**
   - Install Snort from the Package Manager and configure it under Services > Snort.

9. **Set Up pfBlockerNG:**
   - Install pfBlockerNG from the Package Manager and configure it under Firewall > pfBlockerNG.

**Conclusion:**

This project showcases the essential steps and configurations needed to deploy pfSense effectively. Implementing pfSense provides robust network security and management capabilities, making it an excellent choice for both small and large-scale network environments. 
