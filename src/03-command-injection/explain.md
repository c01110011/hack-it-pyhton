# Command Injection


## What Is It
Command injection occurs when the user input is passed unsanitized to the system shell commands.

## How the Attack Works
Let's have this code below as an example
```python
import os
os.system("ping -c 1 " + user_input)
```

if the user_input is `google.com; cat /etc/passwd`, user is able to execute cat /etc/passwd using the system shell command.

Shell metacharacters attackers use:

- ; — run next command regardless
- && — run next command if first succeeds
- || — run next command if first fails
- | — pipe output to next command
- $() — command substitution, output injected inline
- backticks — same as $()

## Risks
- reverse shell
- data deletion
- read environment variables, steal API keys, read database credentials from config files
- establish persistence (create backdoor files)

## Mitigations
Use subprocess.run() with shell=False (the default) and pass arguments as a list, never a string:
subprocess.run(["ping", "-c", "1", user_input])

With shell=False, the OS passes arguments directly to the binary — no shell, no metacharacter interpretation. The attacker's ; is just a literal string passed to ping, which rejects it.

## CVEs
- CVE-2014-6271 (Shellshock) — Bash. Any CGI script (including Python CGI) that passed HTTP headers as environment variables to Bash triggered command injection. An attacker sent a crafted User-Agent header: () { :; }; /bin/bash -c "cat /etc/passwd". Mass exploitation within hours of disclosure. Affected millions of servers.
- CVE-2022-24439 — gitpython (Python library). Command injection via crafted repository URL passed to clone_from(). The library constructed a git clone shell command using unsanitized user input. Affected any Python application using gitpython to clone user-supplied URLs.
 