from fastapi import APIRouter
from api.routes.v1 import routes_veiculo


router = APIRouter(prefix='/veiculos')

router.include_router(routes_veiculo.router)
