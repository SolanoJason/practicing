from pydantic import BaseModel, computed_field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseModel):
    DRIVER: str = "postgresql+psycopg"
    HOST: str = "localhost"
    USER: str = "postgres"
    PORT: int = 5432
    PASSWORD: str
    NAME: str


    @computed_field
    @property
    def URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=self.DRIVER,
            host=self.HOST,
            password=self.PASSWORD,
            username=self.USER,
            port=self.PORT,
            path=self.NAME
        )

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid",
        frozen=True,
        case_sensitive=True,
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        env_nested_delimiter="__",
    )

    DEBUG: bool

    DB: DatabaseSettings

settings = Settings() # type: ignore