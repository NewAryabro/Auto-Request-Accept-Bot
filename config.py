from os import environ

API_ID = int(environ.get("API_ID", "7515868"))
API_HASH = environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")
BOT_TOKEN = environ.get("BOT_TOKEN", "7619312091:AAEj7QujRHXw-HqCAVilUP7Nmqbe_-Ko9io")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002370043591"))
ADMINS = int(environ.get("ADMINS", "6081617163"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://animefrnd44:OEgLPjMjrAKR46kE@cluster0.arcfjym.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "joinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
