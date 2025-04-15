import os

API_ID = os.environ.get("API_ID", "13460015")

API_HASH = os.environ.get("API_HASH", "bd452af645d2a569f654f70b366ce577")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7689689379:AAHdBKGoDZ9z6_ZhVNIZ2pcnGRDHYSq31jA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5431970720))

LOG = -1002244425961,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[5431970720]
    for x in (os.environ.get("ADMINS", "5431970720").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
