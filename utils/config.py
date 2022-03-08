from pydantic import BaseModel
from pydub import AudioSegment
from typing import List, Optional

OUTPUTS_FOLDER = 'outputs/'
BARS = 16

TITLE = "Audio Generator API"
DESC = "Generate audio files from MIDI"
VERSION = "0.1"
HOST = "127.0.0.1"
PORT = 5000

DELETE_FILE_INTERVAL = 10  # in seconds

piano = {
    '28': AudioSegment.from_file('audio/piano_notes/28.mp3', format='mp3'),
    '29': AudioSegment.from_file('audio/piano_notes/29.mp3', format='mp3'),
    '30': AudioSegment.from_file('audio/piano_notes/30.mp3', format='mp3'),
    '31': AudioSegment.from_file('audio/piano_notes/31.mp3', format='mp3'),
    '32': AudioSegment.from_file('audio/piano_notes/32.mp3', format='mp3'),
    '33': AudioSegment.from_file('audio/piano_notes/33.mp3', format='mp3'),
    '34': AudioSegment.from_file('audio/piano_notes/34.mp3', format='mp3'),
    '35': AudioSegment.from_file('audio/piano_notes/35.mp3', format='mp3'),
    '36': AudioSegment.from_file('audio/piano_notes/36.mp3', format='mp3'),
    '37': AudioSegment.from_file('audio/piano_notes/37.mp3', format='mp3'),
    '38': AudioSegment.from_file('audio/piano_notes/38.mp3', format='mp3'),
    '39': AudioSegment.from_file('audio/piano_notes/39.mp3', format='mp3'),
    '40': AudioSegment.from_file('audio/piano_notes/40.mp3', format='mp3'),
    '41': AudioSegment.from_file('audio/piano_notes/41.mp3', format='mp3'),
    '42': AudioSegment.from_file('audio/piano_notes/42.mp3', format='mp3'),
    '43': AudioSegment.from_file('audio/piano_notes/43.mp3', format='mp3'),
    '44': AudioSegment.from_file('audio/piano_notes/44.mp3', format='mp3'),
    '45': AudioSegment.from_file('audio/piano_notes/45.mp3', format='mp3'),
    '46': AudioSegment.from_file('audio/piano_notes/46.mp3', format='mp3'),
    '47': AudioSegment.from_file('audio/piano_notes/47.mp3', format='mp3'),
    '48': AudioSegment.from_file('audio/piano_notes/48.mp3', format='mp3'),
    '49': AudioSegment.from_file('audio/piano_notes/49.mp3', format='mp3'),
    '50': AudioSegment.from_file('audio/piano_notes/50.mp3', format='mp3'),
    '51': AudioSegment.from_file('audio/piano_notes/51.mp3', format='mp3'),
    '52': AudioSegment.from_file('audio/piano_notes/52.mp3', format='mp3'),
    '53': AudioSegment.from_file('audio/piano_notes/53.mp3', format='mp3'),
    '54': AudioSegment.from_file('audio/piano_notes/54.mp3', format='mp3'),
    '55': AudioSegment.from_file('audio/piano_notes/55.mp3', format='mp3'),
    '56': AudioSegment.from_file('audio/piano_notes/56.mp3', format='mp3'),
    '57': AudioSegment.from_file('audio/piano_notes/57.mp3', format='mp3'),
    '58': AudioSegment.from_file('audio/piano_notes/58.mp3', format='mp3'),
    '59': AudioSegment.from_file('audio/piano_notes/59.mp3', format='mp3'),
    '60': AudioSegment.from_file('audio/piano_notes/60.mp3', format='mp3'),
    '61': AudioSegment.from_file('audio/piano_notes/61.mp3', format='mp3'),
    '62': AudioSegment.from_file('audio/piano_notes/62.mp3', format='mp3'),
    '63': AudioSegment.from_file('audio/piano_notes/63.mp3', format='mp3'),
    '64': AudioSegment.from_file('audio/piano_notes/64.mp3', format='mp3'),
    '65': AudioSegment.from_file('audio/piano_notes/65.mp3', format='mp3'),
    '66': AudioSegment.from_file('audio/piano_notes/66.mp3', format='mp3'),
    '67': AudioSegment.from_file('audio/piano_notes/67.mp3', format='mp3'),
    '68': AudioSegment.from_file('audio/piano_notes/68.mp3', format='mp3'),
    '69': AudioSegment.from_file('audio/piano_notes/69.mp3', format='mp3'),
    '70': AudioSegment.from_file('audio/piano_notes/70.mp3', format='mp3'),
    '71': AudioSegment.from_file('audio/piano_notes/71.mp3', format='mp3'),
    '72': AudioSegment.from_file('audio/piano_notes/72.mp3', format='mp3'),
    '73': AudioSegment.from_file('audio/piano_notes/73.mp3', format='mp3'),
    '74': AudioSegment.from_file('audio/piano_notes/74.mp3', format='mp3'),
    '75': AudioSegment.from_file('audio/piano_notes/75.mp3', format='mp3'),
    '76': AudioSegment.from_file('audio/piano_notes/76.mp3', format='mp3'),
    '77': AudioSegment.from_file('audio/piano_notes/77.mp3', format='mp3'),
    '78': AudioSegment.from_file('audio/piano_notes/78.mp3', format='mp3'),
    '79': AudioSegment.from_file('audio/piano_notes/79.mp3', format='mp3'),
    '80': AudioSegment.from_file('audio/piano_notes/80.mp3', format='mp3'),
    '81': AudioSegment.from_file('audio/piano_notes/81.mp3', format='mp3'),
    '82': AudioSegment.from_file('audio/piano_notes/82.mp3', format='mp3'),
    '83': AudioSegment.from_file('audio/piano_notes/83.mp3', format='mp3'),
    '84': AudioSegment.from_file('audio/piano_notes/84.mp3', format='mp3'),
    '85': AudioSegment.from_file('audio/piano_notes/85.mp3', format='mp3'),
    '86': AudioSegment.from_file('audio/piano_notes/86.mp3', format='mp3'),
    '87': AudioSegment.from_file('audio/piano_notes/87.mp3', format='mp3'),
    '88': AudioSegment.from_file('audio/piano_notes/88.mp3', format='mp3'),
    '89': AudioSegment.from_file('audio/piano_notes/89.mp3', format='mp3'),
    '90': AudioSegment.from_file('audio/piano_notes/90.mp3', format='mp3'),
    '91': AudioSegment.from_file('audio/piano_notes/91.mp3', format='mp3'),
    '92': AudioSegment.from_file('audio/piano_notes/92.mp3', format='mp3'),
    '93': AudioSegment.from_file('audio/piano_notes/93.mp3', format='mp3'),
    '94': AudioSegment.from_file('audio/piano_notes/94.mp3', format='mp3'),
    '95': AudioSegment.from_file('audio/piano_notes/95.mp3', format='mp3'),
    '96': AudioSegment.from_file('audio/piano_notes/96.mp3', format='mp3'),
    '97': AudioSegment.from_file('audio/piano_notes/97.mp3', format='mp3'),
}


class Midi(BaseModel):
    one: List[int]
    two: List[int]
    three: List[int]
    four: List[int]
    five: List[int]
    six: List[int]
    seven: List[int]
    eight: List[int]


class Vels(BaseModel):
    one: List[float]
    two: List[float]
    three: List[float]
    four: List[float]
    five: List[float]
    six: List[float]
    seven: List[float]
    eight: List[float]


class Durs(BaseModel):
    one: List[int]
    two: List[int]
    three: List[int]
    four: List[int]
    five: List[int]
    six: List[int]
    seven: List[int]
    eight: List[int]


# These are examples of the parameters that will be with the request
# midi = {
#     "one": [36, 48, 60, 72, 76],
#     "two": [36],
#     "three": [48],
#     "four": [36, 72, 79],
#     "five": [36],
#     "six": [48],
#     "seven": [36],
#     "eight": [48, 76, 79],
# }
# vels = {
#     "one": [0.59, 0.76, 0.88, 0.65, 0.66],
#     "two": [0.14],
#     "three": [0.44],
#     "four": [0.53, 0.89, 0.91],
#     "five": [0.21],
#     "six": [0.59],
#     "seven": [0.6],
#     "eight": [0.474, 0.6793333333333332, 0.685833333333333],
# }
# durs = {
#     "one": [16, 16, 16, 16, 16],
#     "two": [14],
#     "three": [12],
#     "four": [10, 10, 10],
#     "five": [8],
#     "six": [6],
#     "seven": [4],
#     "eight": [2, 2, 2],
# }
