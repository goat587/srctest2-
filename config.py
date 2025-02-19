from os import getenv


API_ID = int(getenv("API_ID", "22696222"))
API_HASH = getenv("API_HASH", "1b4cdb255f37262200981dbbf87a1fa0")
BOT_TOKEN = getenv("BOT_TOKEN", "7972456737:AAEOwSiwQ3ck4E2MsY6arf62DCwCIX-F4dc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7413628447").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://xatibem660:7MWX7Ck6OomoNiWB@cluster0.wrfmk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002313809839"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002313809839"))


