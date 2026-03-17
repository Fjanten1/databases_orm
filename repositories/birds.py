from sqlmodel import Session, select
from models.birds import Bird, BirdCreate
from models.species import Species 

class BirdsRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Bird]:
        statement = select(Bird)
        items = self.session.exec(statement).all()
        return items

    def insert(self, payload: BirdCreate) -> Bird:
        try:
            species = self.session.get(Species, payload.species_id)
            if not species:
                raise ValueError(f"Species with id {payload.species_id} does not exist")

            item = Bird.model_validate(payload)
            self.session.add(item)
            self.session.commit()
            self.session.refresh(item)
            return item
        except Exception as e:
            self.session.rollback()
            raise e
