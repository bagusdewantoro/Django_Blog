import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
EMAIL_USER = os.environ.get('EMAIL_USER')

print(db_user)
print(db_password)
print(EMAIL_USER)
