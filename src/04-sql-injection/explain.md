# SQL Injection


## What Is It
SQL injection occurs when application accepts user input, unsanitized to build SQL queries.

## How the Attack Works
Let's take this SQL query for example: 
```python
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
```
if user_input is `c01110011` the SQL query is a valid one, searching for the username. However, if the user can manipulate
the user_input and change it to `c01110011' OR '1'='1` the SQL query becomes

```python
query = "SELECT * FROM users WHERE username = 'c01110011' OR '1'='1'"
```
In this scenario `'1'='1'` is always true, returning every row from the table, bypassing the authentication

## Risks
- bypass authentication
- data deletion
- dump entire tables — usernames, passwords, emails, payment data
- in some databases (SQL Server, some MySQL configs) SQLi can reach the OS via functions like xp_cmdshell

## Mitigations
Use parametrized queries. The database driver takes care of escaping keeping the data separated from code  
```python
cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
```
The ? is a placeholder. The value is passed separately and never interpreted as SQL.

## CVEs
- CVE-2019-14234 — Django's JSONField and HStoreField had insufficient sanitization of key names in QuerySet.filter() calls. An attacker who controlled the lookup key (not just the value) could inject arbitrary SQL. Affected Django 1.11–2.2.
- Sophos XG CVE-2020-12271 — SQLi as initial access in a real attack chain (not Python but the attack pattern is canonical and well-documented)