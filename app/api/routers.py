from fastapi import FastAPI
from app.api.endpoints import auth, data_modelling, data_visualisation, product_tracking, reporting


def execute():
    fastAPI = FastAPI()
    fastAPI.include_router(auth.router, prefix="/api")
    fastAPI.include_router(data_modelling.router, prefix="/api/modelling")
    fastAPI.include_router(data_visualisation.router, prefix="/api/visual")
    fastAPI.include_router(product_tracking.router, prefix="/api/tracking")
    fastAPI.include_router(reporting.router, prefix="/api/reporting")
    return fastAPI
