from fastapi import APIRouter, HTTPException
from utils.api_operations import get_pokemon_details
from database_connection.database import session_local
from database_connection.models import Pokemon, Type, TypePokemon

router = APIRouter()


@router.post('/new-pokemon/{pokemon_name}')
async def add_new_pokemon(pokemon_name: str):
    session = session_local()
    db_pokemon = session.query(Pokemon).filter(Pokemon.name == pokemon_name).first()

    if db_pokemon:
        session.close()
        raise HTTPException(status_code=404, detail='Pokemon already exists')

    types, height, weight = get_pokemon_details(pokemon_name=pokemon_name)

    if types is None or height is None or weight is None:
        session.close()
        raise HTTPException(status_code=404, detail='Failed to get pokemon details. No pokemon with the provided name exists.')

    db_pokemon = Pokemon(name=pokemon_name, height=height, weight=weight)
    session.add(db_pokemon)
    session.flush()

    for type in types:
        db_type = session.query(Type).filter(Type.type == type).first()
        if db_type is None:
            db_type = Type(type=type)
            session.add(db_type)
            session.flush()

        db_type_pokemon = TypePokemon(type_id=db_type.id, pokemon_id=db_pokemon.id)
        session.add(db_type_pokemon)
        session.flush()

    session.commit()
    session.close()

    return {'name': pokemon_name, 'height': height, 'weight': weight, 'types': types}
