# Cybersecurity Advisory - E-Commerce Platform

## Overview
Assessed security posture of a global e-commerce platform focusing on:
- Web applications
- APIs
- Cloud infrastructure

## Key Threats Identified
- SQL Injection on login forms
- API abuse due to missing rate limiting
- Misconfigured S3 buckets exposing sensitive data

## Recommendations
- Implement secure coding practices (OWASP)
- Add Web Application Firewall (WAF)
- Enforce IAM least privilege and MFA
- Regular vulnerability scanning & penetration testing

## Threat Modeling
- Used NIST CSF and MITRE ATT&CK to prioritize risks
- Calculated risk scores for key systems
- Diagrammed data flows & sensitive data handling

## Tools Used
Python, OWASP ZAP, Burp Suite, Wireshark, NIST CSF
