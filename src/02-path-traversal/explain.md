# Path Traversal

## What Is It
Let's work on this scenario. A webserver is serving files from disk based on the filename in the request. 
Path traversal means that an attacker can manipulate the path of filename in the request, using ../ sequence in order to get access on the server filesystem outside the intended directory.

## How the Attack Works
Let's imagine we are serving report.pdf from /var/www/resources/. If the attacker can manipulate the path for report.pdf,
potentially he will gain access to sensitive information.
Example: 
- if the requested file is ../.env, the resulted path will be /var/www/resources/../.env, which allows attacker to get access to environment variables holding secrets
- if the requested file is ../../../etc/passwd, the resulted path will be /var/www/resources/../../../etc/passwd, which allows attacker to get access to user credentials for entire server
## Risks
- /etc/passwd — user accounts
- /etc/shadow — hashed passwords (if running as root)
- ~/.ssh/id_rsa — private SSH keys
- .env files — API keys, database credentials
- Application source code - to find more vulnerabilities

## Mitigations
Get the absolute path of the requested file and match against the base directory
- Resolve the full absolute path after joining the path of the requested file with the base directory
- Verify that resulting path still starts with the base directory path
- use pathlib to mitigate the issue.

## CVEs
- CVE-2021-41773 — Apache HTTP Server 2.4.49. Path traversal + RCE. Actively exploited in the wild within 24 hours of disclosure. Patched, then bypassed again in 2.4.50 (CVE-2021-42013).
- CVE-2024-23334 — aiohttp (Python async web framework). Path traversal in static file serving. Disclosed 2024.
- Zip Slip (2018) — path traversal via archive extraction. Affected dozens of libraries across Java, Python, Go, JavaScript. Still appears in new codebases.
 