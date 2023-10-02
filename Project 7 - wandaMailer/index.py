import smtplib

HOST = "smtp.mydomain.com"
SUBJECT = "Test email from python"
TO = "mikekanyungo95@gmail.com"
FROM = "python@mydomain.com"
TEXT = "blah blah blah"
BODY = "\r\n".join((
    f"From:" {FROM},
    f"To:" {TO},
    f"Subject:" {SUBJECT},
    "",
    text)
)

server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()