from passlib.context import CryptContext

context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=50000,
)


def create_hash(password):
    return context.hash(password)


def compare_hash(password, hashed_password):
    return context.verify(password, hashed_password)
