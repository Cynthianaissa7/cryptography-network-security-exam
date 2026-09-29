# Set default policies
iptables -F
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow loopback and established connections
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 3a & 3b. Block Guest network and permit Staff network to SSH (Port 22)
iptables -A INPUT -p tcp -s 10.0.20.0/24 --dport 22 -j DROP
iptables -A INPUT -p tcp -s 10.0.10.0/24 --dport 22 -j ACCEPT

# 3c. Explicitly block all other inbound traffic to Port 22
iptables -A INPUT -p tcp --dport 22 -j DROP
# Network Traffic Filtering Test Report

## Network Environment Parameters
- **Target Server IP:** `192.168.1.100`
- **Target Service:** SSH (`tcp/22`)
- **Staff Subnet:** `10.0.10.0/24`
- **Guest Subnet:** `10.0.20.0/24`
- **External Subnet:** `172.16.0.0/24`

---

## Firewall Rules Applied
```bash
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp -s 10.0.20.0/24 --dport 22 -j DROP
iptables -A INPUT -p tcp -s 10.0.10.0/24 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP
