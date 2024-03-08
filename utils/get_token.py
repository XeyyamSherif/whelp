from fastapi import HTTPException


def get_token(authorization):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    try:
        token_type, token = authorization.split()
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")

    if token_type.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid token type. Bearer token expected")
    return token