import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMIN_ID"),
]

host = os.getenv("DB_HOST")
db_name = str(os.getenv("DB_NAME"))
db_pass = str(os.getenv("DB_PASS"))
db_user = str(os.getenv("DB_USER"))
db_port = os.getenv("DB_PORT")
db_uri = f"postgresql://{db_user}:{db_pass}@{host}/{db_name}"