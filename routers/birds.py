from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models.birds import Bird, BirdCreate
from repositories.birds import BirdsRepository

router = APIRouter(prefix="/birds", tags=['Bird'])

def get_birds_repository(
    session: Annotated[Session, Depends(get_session)],
) -> BirdsRepository:
    return BirdsRepository(session)

@router.get("/", response_model=List[Bird])
async def get_birds(repo: Annotated[BirdsRepository, Depends(get_birds_repository)]):
    return repo.get_all()

@router.post("/", response_model=Bird)
async def add_bird(
    bird: BirdCreate,
    repo: Annotated[BirdsRepository, Depends(get_birds_repository)]
):
    return repo.insert(bird)
