#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25134698"))
API_HASH = environ.get("API_HASH", "6b66c879f765a0662a3ad030f8ae45f7")
BOT_TOKEN = environ.get("BOT_TOKEN", "8676600538:AAHT7JW6HU7RqRMbwdVt4W0daTCWf4ltUx0")

OWNER = int(environ.get("OWNER", "8749565729"))
CREDIT = environ.get("CREDIT", "vj")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8749565729').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8749565729').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



