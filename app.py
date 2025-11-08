from http import HTTPStatus

from schemas import Message, UserSchema, UserPublic, UserDB, UserList
from fastapi import FastAPI, HTTPException

app = FastAPI(title='FastAPI do zero')

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def root():
    return {'message': 'Olá mundo!'}

# |------------------------------------------------------------------------------------------|
# Criando metodos para inserir usuarios com (POST)
# |------------------------------------------------------------------------------------------|
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema): # anotação de tipo, determinado pelo schema (entrada dos dados)
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1) # criando um desempacotamento dos dados users
    database.append(user_with_id)

    return user_with_id

# |------------------------------------------------------------------------------------------|
# Criado metodo para ler todos os usuarios criados (GET)
# |------------------------------------------------------------------------------------------|
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(): 
    
    return {'users': database}


# |------------------------------------------------------------------------------------------|
# Criado metodo para ler usuário pelo ID (GET)
# |------------------------------------------------------------------------------------------|
@app.get('/users/{user_id}', response_model=UserPublic)
def read_user__exercicio(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    return database[user_id - 1]


# |------------------------------------------------------------------------------------------|
# Criando metodo para atualizar dados do banco (PUT)
# |------------------------------------------------------------------------------------------|
@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    # Criando lógica para verificar quando nao há usuario
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found!'
        )
    database[user_id - 1] = user_with_id

    return user_with_id


# |------------------------------------------------------------------------------------------|
# Criado metodo para deletar users no banco de dados (DELETE)
# |------------------------------------------------------------------------------------------|
@app.delete('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def delete_user(user_id: int):
    # criado logica para deletar users
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found!'
        )
    return database.pop(user_id - 1) 



if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
