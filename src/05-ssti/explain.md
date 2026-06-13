# Server-Side Template Injection


## What Is It
Web-servers are using template engines to generate the HTML content. Template engines are using placeholders to fill in user input.
```python
template = "Hello, {{ name }}!"
# renders to: "Hello, alice!"
```


## How the Attack Works
If the user input is filled in directly into the template string, unsanitized, the template engine processes the user input as code, not data
```python
# vulnerable
template_str = "Hello, " + user_input + "!"
render_template_string(template_str)
# renders Hello, 49!
```


## Risks
Jinja2 gives access to Python internals, so an attacker can chain object traversal to reach os.system and execute arbitrary code.


## Mitigations
Never concatenate user input into a template string. Pass user input as a variable to a fixed template:
```python
# safe
render_template_string("Hello, {{ name }}!", name=user_input)
```

The engine treats name as data, never as template syntax.


## CVEs
- CVE-2019-8341 - Jinja2. from_string() with unsanitized user input allowed SSTI leading to RCE. Affected any Flask/Jinja2 application passing user-controlled strings directly to template rendering.
- CVE-2016-4977 - Spring Security OAuth (Java, not Python). Included here because it's the canonical SSTI CVE that put the vulnerability class on the map - error message templates were rendered with user-supplied scope parameter, leading to RCE. Widely referenced in SSTI writeups regardless of language.
- Werkzeug debugger PIN bypass (2019) - not a CVE but a well-documented attack where SSTI was used to leak server internals and calculate the debugger PIN, turning SSTI into interactive RCE. Directly relevant to Flask.