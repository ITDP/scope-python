import os
import signal
import sys
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src.api.brt_scope_api import brt_scope_api

app = FastAPI(title="itdpApi")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


brt_scope_api(app)

def exit_gracefully():
    time.sleep(0.2)
    sys.exit(0)


signal.signal(signal.SIGTERM, exit_gracefully)

handler = Mangum(app)
