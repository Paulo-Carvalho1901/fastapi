from http import HTTPStatus

from schemas import Message, UserSchema
from fastapi import FastAPI

app = FastAPI(title='FastAPI do zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def root():
    return {'message': 'Olá mundo!'}


@app.post('/users/')
def create_user(user: UserSchema): # anotação de tipo, determinado pelo schema
    return user

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
