# Risk Assessment Matrix

## 1. Assets, Vulnerabilities, and Consequences
1. **Asset 1: Student Records Server**
   - **Vulnerability:** Unrestricted guest network access to the server.
   - **Consequence:** Unauthorized internal users or guests can access, alter, or exfiltrate sensitive student data, causing data breaches and regulatory non-compliance.

2. **Asset 2: Transferred Student Files / Sensitive Data in Transit**
   - **Vulnerability:** Unencrypted network file transfers between campuses.
   - **Consequence:** Eavesdropping or Man-in-the-Middle (MitM) attacks allowing adversaries to intercept, view, or tamper with data during transit.

3. **Asset 3: System / Staff User Accounts**
   - **Vulnerability:** Weak staff passwords and outdated system software.
   - **Consequence:** Easy compromise via brute-force or dictionary attacks, leading to unauthorized administrative access and vulnerability exploitation by external attackers.

---

## 2. Risk Ranking (Likelihood and Impact)

| Risk Ref | Asset | Likelihood | Impact | Overall Rank | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R1** | Student Records Server (Guest Access) | **High** | **High** | **1 (Critical)** | Guest network access is currently active and easily accessible without external barriers, exposing core records directly. |
| **R2** | Transferred Files (Unencrypted Transfers) | **High** | **Medium** | **2 (High)** | Files are actively transferred between campuses; lack of encryption makes eavesdropping highly probable during routine operations. |
| **R3** | Staff Accounts & Software | **Medium** | **High** | **3 (Medium-High)** | System exploitation or password cracking requires targeted effort, but successful compromise grants extensive privilege. |

---

## 3. Recommended Controls

1. **Control for Risk 1 (Guest Access):** Implement network segmentation using Firewall / Access Control Lists (ACLs) to block all guest subnet traffic from reaching the records server.
2. **Control for Risk 2 (Unencrypted File Transfers):** Mandate secure transport protocols (e.g., SFTP, SCP, or HTTPS with TLS) and apply symmetric encryption (e.g., AES-256) to sensitive data before transmission.
3. **Control for Risk 3 (Weak Passwords & Outdated Software):** Enforce a strong Password Policy (MFA, minimum length/complexity) and establish a regular Patch Management process to update system software.
