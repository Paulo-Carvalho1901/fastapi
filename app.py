from http import HTTPStatus

from schemas import Message, UserSchema, UserPuplic, UserDB, UserList
from fastapi import FastAPI

app = FastAPI(title='FastAPI do zero')

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def root():
    return {'message': 'Olá mundo!'}


# Criando metodos para inserir usuarios com (POST)
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPuplic)
def create_user(user: UserSchema): # anotação de tipo, determinado pelo schema (entrada dos dados)
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1) # criando um desempacotamento dos dados users

    database.append(user_with_id)

    return user_with_id


# Criado metodo para ler todos os usuarios criados (GET)
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(): 
    
    return {'users': database}


# Criando metodo para atualizar dados do banco (PUT)
@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPuplic)
def update_user(user_id: int, user: UserSchema):
    ...



if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
