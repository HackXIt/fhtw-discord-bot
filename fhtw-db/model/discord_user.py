from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DiscordUser(Base):
    __tablename__ = 'discord_users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    discriminator = Column(String, nullable=False)
    discord_id = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<DiscordUser(id={self.id}, username={self.username}, discord_id={self.discord_id})>'
