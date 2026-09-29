
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
```
## Test Execution and Results
-**Test 1: Permitted Connection (Staff Network -> SSH)**

- Source IP: 10.0.10.15 (Staff Workstation)

- Command Executed:
nc -zv -w 3 192.168.1.100 22

- Expected Outcome: Connection succeeds (open).

- Actual Result: Connection to 192.168.1.100 22 port [tcp/ssh] succeeded!

**Test 2: Blocked Connection 1 (Guest Network -> SSH)**

- Source IP: 10.0.20.45 (Guest Workstation)

- Command Executed:

nc -zv -w 3 192.168.1.100 22

- Expected Outcome: Connection times out or is refused.

- Actual Result: nc: connect to 192.168.1.100 port 22 (tcp) timed out

**Test 3: Blocked Connection 2 (Unfamiliar External Network -> SSH)**

- Source IP: 172.16.0.88 (External Network)

- Command Executed:
nc -zv -w 3 192.168.1.100 22

- Expected Outcome: Connection times out or is blocked.

- Actual Result: nc: connect to 192.168.1.100 port 22 (tcp) timed out
