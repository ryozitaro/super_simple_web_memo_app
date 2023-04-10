import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

import router_memo


app = FastAPI(debug=True)
app.include_router(router_memo.router)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
