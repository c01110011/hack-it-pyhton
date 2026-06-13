# Timing attacks


## What Is It
A timing attack exploits the fact that code takes measurably different amounts of time to execute depending on the input. 
An attacker can infer secret information, like a password or token, by measuring how long the server takes to respond.


## How the Attack Works
The classic example — string comparison:

Python's == operator compares strings character by character and stops as soon as it finds a mismatch:

```python
"secret123" == "sXXXXXXXX"  # stops at position 1 — fast
"secret123" == "secret124"  # stops at position 8 — slower
```


## Risks
If you're comparing a user-supplied token against a secret token, an attacker can send thousands of guesses and measure response times. 
Guesses that match more characters take slightly longer, leaking how many characters are correct. 
Repeat until the full secret is recovered.

Any == comparison of secrets is vulnerable:
  - API token validation
  - Password reset token comparison
  - HMAC verification done manually
  - Cookie signature checks


## Mitigations
Use hmac.compare_digest() — a constant-time comparison function that always takes the same amount of time regardless of where the strings differ:

```python
import hmac
hmac.compare_digest(user_token, secret_token)
```

No early exit. No timing signal. The attacker learns nothing from response times.

## CVEs
- CVE-2015-2157 - PuTTY. Timing attack on private key comparison. Classic example of the class in a widely-used tool.
- Django security release (2012, no CVE) - Django's check_password() used == to compare hashes. Fixed by introducing constant_time_compare(). Documented in Django's security changelog. Direct Python precedent for this entry.
- Python hmac module - Python's own hmac.compare_digest() was added in Python 2.7.7 / 3.3 specifically because the language lacked a constant-time comparison primitive. The addition is documented in the Python changelog as a security fix.