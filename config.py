import os

API_ID = os.environ.get("API_ID", "21705536")

API_HASH = os.environ.get("API_HASH", "c5bb241f6e3ecf33fe68a444e288de2d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7824200717:AAHoLvCPubl26T7_QHKW48xvi2a5EroRn-4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5957208798))

LOG = -1002244425961,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[5957208798]
    for x in (os.environ.get("ADMINS", "5957208798").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
