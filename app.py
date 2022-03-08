from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import FileResponse
import json
from fastapi.staticfiles import StaticFiles
from fastapi import Request

from utils.audioGenerator import generate_audio
from utils.config import TITLE, DESC, VERSION, HOST, PORT
from utils.config import Midi, Vels, Durs, Data
from fastapi.templating import Jinja2Templates

app = FastAPI(title=TITLE, description=DESC, version=VERSION)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/audio", response_class=FileResponse)
def generate_audio_file(midi: Midi, vels: Vels, durs: Durs, data: Data ):
    return generate_audio(midi.json(), vels.json(), durs.json(), data.json() )


if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT, log_level="info")
