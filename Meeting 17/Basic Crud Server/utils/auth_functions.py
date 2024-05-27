import time
import jwt
from decouple import config
import bcrypt
from utils.database_functions import read_data
from main import filepath

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(entered_password, hashed_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8'))


def authenticate_new_user(id, password):
    pass
