from fastapi import HTTPException
from database_connection.models import TrainerPokemon, TypePokemon


def delete_pokemon(session, db_pokemon):
    if db_pokemon is None:
        session.close()
        raise HTTPException(status_code=404, detail='Pokemon not found')

    db_types = session.query(TypePokemon).filter(TypePokemon.pokemon_id == db_pokemon.id).all()
    for db_type in db_types:
        session.delete(db_type)

    db_trainers = session.query(TrainerPokemon).filter(TrainerPokemon.pokemon_id == db_pokemon.id).all()
    for db_trainer in db_trainers:
        session.delete(db_trainer)

    session.delete(db_pokemon)
    session.commit()
    session.close()


def delete_trainer(session, db_trainer):
    if db_trainer is None:
        session.close()
        raise HTTPException(status_code=404, detail='Trainer not found')

    db_pokemons = session.query(TrainerPokemon).filter(TrainerPokemon.trainer_id == db_trainer.id).all()
    for db_pokemon in db_pokemons:
        session.delete(db_pokemon)

    session.delete(db_trainer)
    session.commit()
    session.close()

