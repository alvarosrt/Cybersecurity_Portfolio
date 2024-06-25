# Firewall Rules Configuration - pfSense

## Overview
pfSense is an open-source firewall and router platform based on FreeBSD that provides various features for secure network communication.

### Example Rule
```plaintext
Action: Pass
Interface: WAN
Protocol: TCP/UDP
Source: Any
Destination: 192.168.1.0/24
Port: 80, 443
Description: Allow HTTP(S) traffic to LAN network
```

### Types of Firewall Rules
1. **Floating Rules**: These rules apply to traffic passing through the firewall regardless of interface-specific rules.
2. **Interface Rules**: These rules apply to specific interfaces and govern traffic entering or leaving those interfaces.

### Common Rule Actions
- **Pass**: Allows traffic matching the rule.
- **Block**: Blocks traffic matching the rule.
- **Reject**: Blocks traffic and sends an error message to the sender.


