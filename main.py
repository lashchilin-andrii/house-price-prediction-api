from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import headers, main_router, methods, origins


app = FastAPI(title="House prices prediction API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

app.include_router(
    main_router,
)

