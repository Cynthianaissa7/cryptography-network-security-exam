# Cryptography and Network Security Exam Project

**Repository:** `cryptography-network-security-exam`  
**Institution:** ULK Polytechnic Institute  
**Module:** ETTCS801 Cryptography and Network Security  

---
## 1. Project Structure

cryptography-network-security-exam/

├── README.md                  # Project overview and execution instructions

├── risk_assessment.md         # Risk assessment matrix and recommendations

├── filter_tests.md            # Firewall configuration and traffic test logs

├── crypto_toolkit.py          # Python security script for encryption & hashing

├── report.tex                 # Technical report source code (LaTeX)

└── report.pdf                 # Compiled LaTeX report

> **Note:** The key file (`secret.key`) is generated and stored in the parent directory (`../secret.key`) to keep sensitive keys out of public version control.

---

## 2. Environment Setup & Requirements
- **Python Version:** Python 3.8+
- **Dependencies:** `cryptography`

Install required libraries:
```bash
pip install cryptography
python3 crypto_toolkit.py
nc -zv -w 3 <SERVER_IP> 22

