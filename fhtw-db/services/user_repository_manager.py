from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .discord_user import Base, DiscordUser

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_user_by_discord_id(discord_id: str):
    session = SessionLocal()
    user = session.query(DiscordUser).filter(DiscordUser.discord_id == discord_id).first()
    session.close()
    return user

def add_user(username: str, discriminator: str, discord_id: str):
    session = SessionLocal()
    user = DiscordUser(username=username, discriminator=discriminator, discord_id=discord_id)
    session.add(user)
    session.commit()
    session.close()
