from fastapi import FastAPI, Response
from fae.database import engine, Base
from fae.api.v1.app.routers import users


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(
    users.router,
    prefix="/v1"
)


@app.get("/")
async def index():
    return Response(status_code=204)