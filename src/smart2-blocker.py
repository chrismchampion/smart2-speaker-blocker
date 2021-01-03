import speech_recognition as sr
import pyaudio
import wave
import re
import os
import time
from pydub import AudioSegment


class Smart2Blocker:

    privacy_on: bool = False

    def play_wav_file(self, filename: str):
        chunk = 1024
        f = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        data = f.readframes(chunk)

        while data:
            stream.write(data)
            data = f.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def gtts(self, text: str):

        os.system('bash' + ' ' + 'simple-google-tts/./simple_google_tts -p en ' + '"' + text + '"')

    def get_loudness(self):
        sound = AudioSegment.from_file('audio_file_1.wav')
        return sound.dBFS

    def privacy_mode(self, p_key):
        if p_key == "activate":
            if self.privacy_on:
                self.play_wav_file('privacy_mode_already_on.wav')
            else:
                self.privacy_on = True
                self.play_wav_file('privacy_mode_on.wav')
        elif p_key == "deactivate":
            if self.privacy_on:
                self.privacy_on = False
                self.play_wav_file('privacy_mode_off.wav')
            else:
                self.play_wav_file('privacy_mode_already_off.wav')

    def keyword_mode(self, p_key):
        new_val: str = ""
        new_val = new_val.split(p_key, 1)[0]
        print("You said = {}".format(new_val) + " " + "[redacted]")

    def set_timer(self):
        self.gtts("Activating privacy mode for 5 minutes")
        for t in range(300):
            #minutes = t / 60
            #seconds = t % 60
            #print("%d:%2d" % (minutes, seconds))
            time.sleep(1.0)

    def handle_voice_input(self, pvalue: str):

        # ARGUMENT MODE
        if Smart2Blocker.get_loudness(self) > -5.0 and not self.privacy_on:
            Smart2Blocker.gtts(self, "It sounds like you might be having an argument. Activating privacy mode.")
            self.privacy_on = True
            return True

        # PRIVACY MODE EVALUATION
        if re.search(r'(.*) privacy', pvalue, re.M | re.I):
            search_obj = re.search(r'(.*) privacy', pvalue, re.M | re.I)
            self.privacy_mode(search_obj.group(1).lower())
            return True

        # INSTRUCT USER TO DEACTIVATE PRIVACY MODE IF THEY WISH TO RESUME NORMAL OPERATION
        if self.privacy_on:
            self.gtts("Please deactivate privacy mode to relay commands.")
            return True

        # NORMAL OPERATION: KEYWORD EVALUATION
        if re.search(r'affair|bank|girlfriend|account|password|pin', pvalue, re.M | re.I):
            search_obj = re.search(r'affair|bank|girlfriend|account|password|pin', pvalue, re.M | re.I)
            self.keyword_mode(search_obj.group())
            return True

        # TIME-BASED KEYWORD
        if re.search(r'finance', pvalue, re.M | re.I):
            self.set_timer()
            return True


class Tester:

    r = sr.Recognizer()
    m = sr.Microphone()
    echo = Smart2Blocker()

    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            echo.gtts("Go ahead, I am listening.")
            with m as source:
                audio = r.listen(source)
                audioWavData = audio.get_wav_data()
            print("Got it! Now to recognize it...")

            try:
                # recognize speech using CMU Sphinx pocketsphinx
                value = r.recognize_sphinx(audio, language="en-US")
                # print unicode characters to standard output
                print("You said {}".format(value))

                # st    ore recorded phrase in audio_file_1 wav file
                f = open('audio_file_1.wav', 'w+b')
                f.write(audioWavData)
                f.close()

                if echo.handle_voice_input(value):
                    print("-------------------------")
                else:
                    # play recorded phrase
                    echo.play_wav_file('audio_file_1.wav')
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from pocketsphinx;{0}".format(e))
    except KeyboardInterrupt:
        pass
