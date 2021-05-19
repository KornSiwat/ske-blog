# SKE Blog

This project is a final project for software security course

## Members

| name                     | id         |
| ------------------------ | ---------- |
| Arisa Pangpeng           | 6110545678 |
| Nattapol Boonyapornpong  | 6110545503 |
| Pawaris Wongsalung       | 6110545562 |
| Patteera Likitmanuayporn | 6110545597 |
| Siwat Ponpued            | 6110546640 |

## OWASP Top 10 Solutions

- Injection: Use ORM provided by Django

- Broken authentication: Require long password and must not common, Use authentication system provided by Django

- Sensitive data exposure: Use HTTPS

- XML External Entities (XXE): Does not fetch from any 3rd party

- Broken access control: Strictly Configured Access Control

- Security misconfiguration: Do code review

- XSS: follows framework and security best practices

- Insecure deserialization: Uses popular and reliable library

- Using components with known vulnerabilities: Always check for update and subscribe to news on vulnerabilities of the components used

- Insufficient logging and monitoring: Implement logging and activity tracking (history app)

## Prerequisite

- `Python (ver.3.9 or above)` [download site](https://www.python.org/downloads/)
- `Python modules listed in` [requirement file](requirements.txt)

## Installation

1.  clone the project

```
git clone https://github.com/kornsiwat/ske-blog
```

2.  Install dependencies

```
pip install -r requirements.txt
```

3.  Make Migration

```
python manage.py makemigrations
python manage.py migrate
```

## How to run

```
python manage.py runserver
```
