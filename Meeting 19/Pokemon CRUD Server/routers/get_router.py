from fastapi import APIRouter, HTTPException
from database_connection.database import session_local
from database_connection.models import Pokemon, Trainer, Type, TypePokemon, TrainerPokemon

router = APIRouter()


@router.get('/pokemon-details-by-id/{pokemon_id}')
async def get_pokemon_details_by_id(pokemon_id: int):
    session = session_local()
    db_pokemon = session.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    if db_pokemon is None:
        session.close()
        raise HTTPException(status_code=404, detail='Pokemon not found')

    session.close()

    return db_pokemon


@router.get('/pokemon-details-by-name/{pokemon_name}')
async def get_pokemon_details_by_name(pokemon_name: str):
    session = session_local()
    db_pokemon = session.query(Pokemon).filter(Pokemon.name == pokemon_name).first()

    if db_pokemon is None:
        session.close()
        raise HTTPException(status_code=404, detail='Pokemon not found')

    session.close()

    return db_pokemon


@router.get('/pokemons-by-type/{pokemon_type}')
async def get_pokemons_by_type(pokemon_type: str):
    session = session_local()
    db_type = session.query(Type).filter(Type.type == pokemon_type).first()

    if db_type is None:
        session.close()
        raise HTTPException(status_code=404, detail='Type not found')

    db_pokemons = session.query(TypePokemon).filter(TypePokemon.type_id == db_type.id).all()
    pokemons = []
    for item in db_pokemons:
        db_pokemon = session.query(Pokemon).filter(Pokemon.id == item.pokemon.id).first()
        pokemons.append(db_pokemon.name)

    session.close()

    return pokemons


@router.get('/pokemon-trainers/{pokemon_name}')
async def get_pokemon_trainers(pokemon_name: str):
    session = session_local()
    db_pokemon = session.query(Pokemon).filter(Pokemon.name == pokemon_name).first()

    if db_pokemon is None:
        session.close()
        raise HTTPException(status_code=404, detail='Pokemon not found')

    db_trainers = session.query(TrainerPokemon).filter(TrainerPokemon.pokemon_id == db_pokemon.id).all()
    trainers = []
    for item in db_trainers:
        db_trainer = session.query(Trainer).filter(Trainer.id == item.trainer.id).first()
        trainers.append(db_trainer.name)

    session.close()

    return trainers


@router.get('/pokemons-by-trainer/{trainer_name}')
async def get_pokemons_by_trainer(trainer_name: str):
    session = session_local()
    db_trainer = session.query(Trainer).filter(Trainer.name == trainer_name).first()

    if db_trainer is None:
        session.close()
        raise HTTPException(status_code=404, detail='Trainer not found')

    db_pokemons = session.query(TrainerPokemon).filter(TrainerPokemon.trainer_id == db_trainer.id).all()
    pokemons = []
    for item in db_pokemons:
        db_pokemon = session.query(Pokemon).filter(Pokemon.id == item.pokemon.id).first()
        pokemons.append(db_pokemon.name)

    session.close()

    return pokemons
