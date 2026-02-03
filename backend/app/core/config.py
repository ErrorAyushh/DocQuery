import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")


settings = Settings()
