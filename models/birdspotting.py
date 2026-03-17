from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from models.birds import Bird

class BirdspottingBase(SQLModel):
    bird_id: int = Field(foreign_key="birds.id")
    spotted_at: datetime
    location: str
    observer_name: str
    notes: Optional[str] = None

class Birdspotting(BirdspottingBase, table=True):
    __tablename__ = "birdspotting"
    id: Optional[int] = Field(default=None, primary_key=True)
    bird: Optional[Bird] = Relationship()

class BirdspottingCreate(BirdspottingBase):
    pass

class BirdspottingRead(BirdspottingBase):
    id: int
    bird: Optional[Bird] = None
