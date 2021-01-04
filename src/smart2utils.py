import os
import pyaudio
import wave
import time
from pydub import AudioSegment


# Simple Google TTS (offline)
def gtts(text: str):
    os.system('bash' + ' ' + 'simple-google-tts/./simple_google_tts -p en ' + '"' + text + '"')


def write_runtime(file, string):
    try:
        with open(file, 'a') as f_out:
            f_out.write(string)
    except IOError as io_err:
        print(io_err)


def set_timer():
    gtts("Activating privacy mode for 5 minutes")
    for t in range(300):
        time.sleep(1.0)


def get_loudness():
    sound = AudioSegment.from_file('audio_file_1.wav')
    return sound.dBFS


def get_audio_segment_length():
    sound = AudioSegment.from_file('audio_file_1.wav')
    # assert sound.duration_seconds == (len(sound) / 1000.0)
    return sound.duration_seconds * 1000


def print_redaction(p_key):
    new_val: str = ""
    new_val = new_val.split(p_key, 1)[0]
    print("You said: {}".format(new_val) + " " + "[redacted]")


def play_wav_file():
    chunk = 1024
    f = wave.open("audio_file_1.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(),
                    rate=f.getframerate(), output=True)
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()


def play_wav_from_file(wav_file):
    chunk = 1024
    f = wave.open(wav_file, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(),
                    rate=f.getframerate(), output=True)
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()