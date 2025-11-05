import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv()
except FileNotFoundError:
    print(".env tai .env.test ei löytynyt")

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME")
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)