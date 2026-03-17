from typing import List, Annotated, Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models.birdspotting import BirdspottingCreate, BirdspottingRead
from repositories.birdspotting import BirdspottingRepository

router = APIRouter(prefix="/birdspotting", tags=['Birdspotting'])

def get_birdspotting_repository(
    session: Annotated[Session, Depends(get_session)],
) -> BirdspottingRepository:
    return BirdspottingRepository(session)

@router.get("/", response_model=List[BirdspottingRead])
async def get_birdspottings(
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    '''
    Get all birdspottings
    '''
    return repo.get_all()

@router.get("/{spotting_id}", response_model=Optional[BirdspottingRead])
async def get_birdspotting(
    spotting_id: int,
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    '''
    Get a birdspotting by id
    '''
    return repo.get_one(spotting_id)

@router.post("/", response_model=BirdspottingRead)
async def add_birdspotting(
    spotting: BirdspottingCreate,
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    '''
    Add a new birdspotting
    '''
    return repo.insert(spotting)
