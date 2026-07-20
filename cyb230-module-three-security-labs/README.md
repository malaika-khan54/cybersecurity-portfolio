# CYB 230 Module Three Security Labs

## Project Overview

This project documents the hands-on labs I completed for CYB 230: Operating System Security at Southern New Hampshire University.

The Module Three labs focused on basic network configuration, Windows and Linux firewall security, security policies, failed logon auditing, and system hardening.

## Labs Completed

### 1. Basic Network Configuration

I manually configured a CentOS network interface using both NetworkManager and the traditional network service.

During this lab, I worked with:

- IP addresses
- Subnet masks
- Default gateways
- DNS servers
- Hostnames
- Fully qualified domain names
- The `/etc/hosts` file
- The `/etc/resolv.conf` file

I also used commands such as:

- `ifconfig`
- `route`
- `ping`
- `host`
- `dig`

This lab helped me understand how systems are configured to communicate on a network and how DNS and hostname resolution work.

### 2. Network Security and Firewalls

I worked with Windows Firewall and Windows Firewall with Advanced Security.

I enabled the File and Printer Sharing Echo Request rule for ICMPv4 traffic. Before enabling the rule, one Windows server could not successfully ping the other. After enabling the correct inbound rule, all four packets were received with zero packet loss.

I also practiced using Linux firewall rules to control network traffic and block insecure Telnet connections.

### 3. Implementing Security Policies

I created a customized Windows logon warning and enabled auditing for failed login attempts.

I intentionally entered an incorrect password and then located the resulting Audit Failure event in Windows Event Viewer.

I also used Zenmap to examine open ports on a Linux system and practiced applying firewall rules to restrict incoming traffic while still allowing web traffic through port 80.

## Challenge and Solution

I made one small mistake during the network configuration lab. I took one of my screenshots too early, before the complete configuration output was displayed.

Since I needed to include the screenshot in my Module Three worksheet, I returned to the terminal, ran the correct command, and made sure the IP address, gateway, and DNS settings were visible before retaking the screenshot.

This reminded me that technical work is not only about making configuration changes. It is also important to verify the results and document them clearly.

## Skills Practiced

- CentOS network configuration
- Windows and Linux administration
- DNS and hostname resolution
- Windows Firewall management
- Linux firewall configuration
- ICMP connectivity testing
- Failed login auditing
- Windows Event Viewer
- Group Policy configuration
- Port scanning with Zenmap
- System hardening
- Technical troubleshooting
- Security documentation

## Screenshots

### CentOS Network Configuration

![CentOS Network Configuration](centos-network-configuration.png)

### Successful Windows Firewall Test

![Successful Windows Firewall Test](windows-firewall-ping.png)

### Customized Windows Logon Warning

![Customized Windows Logon Warning](windows-logon-warning.png)

### Failed Logon Audit Event

![Failed Logon Audit Event](audit-failure-event.png)

## Ethical Use Statement

This project was completed in an authorized academic lab environment for educational purposes. No testing was performed against systems without permission.
