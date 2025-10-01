from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI(title='FastAPI do zero')


@app.get('/', status_code=HTTPStatus.OK)
def root():
    return {'message': 'Olá mundo!'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
