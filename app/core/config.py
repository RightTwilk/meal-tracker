from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    app_name: str = "MealTracker"
    debug: bool = False
    db_user: str = ""
    db_password: str = ""
    db_name: str = ""
    
    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@localhost:5432/{self.db_name}"

config = Config()