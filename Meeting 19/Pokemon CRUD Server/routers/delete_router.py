from fastapi import APIRouter, HTTPException

from database_connection.database import session_local
from database_connection.models import Pokemon

router = APIRouter()


def delete_pokemon(session, db_pokemon):
    if db_pokemon is None:
        session.close()
        raise HTTPException(status_code=404, detail='Pokemon not found')

    session.delete(db_pokemon)
    session.commit()
    session.close()

    return f'Deleted pokemon {db_pokemon.name}'


@router.delete('/pokemon-by-id/{pokemon_id}')
async def delete_pokemon_by_id(pokemon_id: int):
    session = session_local()
    db_pokemon = session.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    delete_pokemon(session, db_pokemon)


@router.delete('/pokemon-by-name/{pokemon_name}')
async def delete_pokemon_by_name(pokemon_name: str):
    session = session_local()
    db_pokemon = session.query(Pokemon).filter(Pokemon.name == pokemon_name).first()
    delete_pokemon(session, db_pokemon)


@router.delete('/pokemon-of-trainer-by-id/{trainer_id}')
async def delete_pokemon_of_trainer_by_id(trainer_id: int):
    pass


@router.delete('/pokemon-of-trainer-by-name/{trainer_name}')
async def delete_pokemon_of_trainer_by_name(trainer_name: str):
    pass
