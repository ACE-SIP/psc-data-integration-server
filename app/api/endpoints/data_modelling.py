from fastapi import Depends, APIRouter
from app.api.models import User
from app.api.models.User import get_current_active_user

router = APIRouter(responses={404: {"description": "Not found"}})


@router.get('/test')
def test_modelling():
    return {"code": 200, "message": "test api for modelling"}


@router.get('/condition/{product_id}')
def product_condition_modelling(product_id, current_user: User = Depends(get_current_active_user)):
    return {"code": 200, "current_user": current_user, "message": "test api for product tracking"}
