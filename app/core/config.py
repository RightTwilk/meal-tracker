from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

load_dotenv()

DEBUG: bool = False
BASE_DIR: Path = Path(__file__).parent.parent
LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(message)s"


class DBConfig(BaseModel):
    db_user: str = ""
    db_password: str = ""
    db_name: str = ""
    echo: bool = True if DEBUG else False

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@localhost:5432/{self.db_name}"


class LogConfig(BaseModel):
    level: str = "INFO"
    format: str = LOG_FORMAT
    datefmt: str = "%Y-%m-%d %H:%M:%S"


class Config(BaseSettings):
    log: LogConfig = LogConfig()
    db: DBConfig = DBConfig()


config = Config()

print(config.db.db_url)
