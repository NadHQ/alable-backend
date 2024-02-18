from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/hallo")
async def get_user():
    return {"message": "Hallo"}
