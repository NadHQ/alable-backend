import uvicorn
from fastapi import FastAPI

from src.api.routes.category import book_router
from src.api.routes.user import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(book_router)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
