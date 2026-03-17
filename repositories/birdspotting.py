from typing import Optional
from sqlmodel import Session, select
from models.birdspotting import Birdspotting, BirdspottingCreate, BirdspottingRead
from models.birds import Bird

class BirdspottingRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[BirdspottingRead]:
        statement = select(Birdspotting)
        items = self.session.exec(statement).all()
        return items

    def get_one(self, spotting_id: int) -> Optional[BirdspottingRead]:
        statement = select(Birdspotting).where(Birdspotting.id == spotting_id)
        item = self.session.exec(statement).first()
        return item

    def insert(self, payload: BirdspottingCreate) -> BirdspottingRead:
        try:
            # Check if the bird exists
            bird = self.session.get(Bird, payload.bird_id)
            if not bird:
                raise ValueError(f"Bird with id {payload.bird_id} does not exist")

            item = Birdspotting.model_validate(payload)
            self.session.add(item)
            self.session.commit()
            self.session.refresh(item)
            return item
        except Exception as e:
            self.session.rollback()
            raise e
