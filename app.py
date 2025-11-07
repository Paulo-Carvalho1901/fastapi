from http import HTTPStatus

from schemas import Message, UserSchema, UserPuplic, UserDB
from fastapi import FastAPI

app = FastAPI(title='FastAPI do zero')

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def root():
    return {'message': 'Olá mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPuplic)
def create_user(user: UserSchema): # anotação de tipo, determinado pelo schema
    user_with_id = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(database) + 1
    )

    database.append(user_with_id)

    return user_with_id





if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
