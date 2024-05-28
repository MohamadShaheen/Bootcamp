from fastapi import APIRouter, HTTPException
from utils.api_operations import get_pokemon_details
from database_connection.database import session_local
from database_connection.models import Pokemon, Type, TypePokemon

router = APIRouter()



