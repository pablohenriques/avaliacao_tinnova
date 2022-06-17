from fastapi import FastAPI
from uvicorn import run
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from api.routes import routes
from api.models import models_veiculos
from api.database.basedados import engine


models_veiculos.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(routes.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/', tags=['Documentação'])
async def index():
    return RedirectResponse("/docs")


if __name__ == '__main__':
    run('main:app', host='0.0.0.0', port=8000, reload=True)
