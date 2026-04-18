from sqlalchemy import URL, create_engine, make_url
from core.settings import settings
from sqlalchemy.orm import sessionmaker

url = make_url(settings.DB.URI.unicode_string())

engine = create_engine(
    url,
    echo=True,
    echo_pool=True,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_timeout=15,
    isolation_level=settings.DB.ISOLATION_LEVEL
)

SessionFactory = sessionmaker(engine)