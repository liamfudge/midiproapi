import time
from threading import Thread
from pydub import AudioSegment
from fastapi.responses import FileResponse
import uuid
import os
from utils.config import Instruments, OUTPUTS_FOLDER, BARS
import json


def random_audio_file_name():
    """
        Function to generate a random audio file name
    """
    return str(uuid.uuid4()) + '.mp3'


def delete_audio_file(audio_file_name):
    """
        Threaded Function to delete the audio file after few minutes
    """
    time.sleep(10)
    os.remove(OUTPUTS_FOLDER + audio_file_name)


def generate_audio(midi, vels, durs, data):
    """
        Function to generate the audio file
    """

    data = json.loads(data);
    midi = json.loads(midi)
    vels = json.loads(vels)
    durs = json.loads(durs)

    # 16th note length in ms
    note_val = int(((120 / data['tempo']) * 1000) / 8)
    overlayPart = AudioSegment.silent(duration=note_val*data['bars'])

    for index, i in enumerate(midi):
        if midi[i] is not None:
            if len(midi[i]) > 0:
                for j in range(len(midi[i])):
                    velocity = -(10 - round(vels[i][j]*10))
                    inst_note = Instruments[data['instID']][str(midi[i][j])] + velocity
                    sound = inst_note[:note_val*durs[i][j]]
                    fadedSound = sound.fade_out(note_val)
                    overlayPart = overlayPart.overlay(
                        fadedSound, position=index*note_val)

    file_name = random_audio_file_name()

    file_handle = overlayPart.export(OUTPUTS_FOLDER + file_name, format='mp3')

    Thread(target=delete_audio_file, args=(file_name,)).start()

    return FileResponse(path=OUTPUTS_FOLDER + file_name, filename=file_name)
