from config import settings
from sqlalchemy import URL, create_engine

url = URL.create(
    drivername=settings.DB.DRIVER,
    username=settings.DB.USER,
    password=settings.DB.PASSWORD,
    host=settings.DB.HOST,
    port=settings.DB.PORT,
    database=settings.DB.NAME,
    # query={
    #     "some": "x",
    #     "somey": "y"
    # }
)

engine = create_engine(url)