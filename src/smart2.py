import re
import smart2utils
import speech_recognition as sr
import time


class Smart2:

    def __init__(self):
        # self.privacy_on: bool = False
        self.privacy_on = False
        self.current_ms_time = int(round(time.time() * 1000))

    def privacy_mode(self, p_key):
        if p_key == "activate":
            if self.privacy_on:
                smart2utils.gtts("Privacy mode is already on.")
            else:
                self.privacy_on = True
                smart2utils.gtts("Privacy mode activated.")
        elif p_key == "deactivate":
            if self.privacy_on:
                self.privacy_on = False
                smart2utils.gtts("Privacy mode is off.")
            else:
                smart2utils.gtts("Privacy mode is already off.")

    def capture_audio(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        try:
            # get current time for runtime output
            self.current_ms_time = int(round(time.time() * 1000))
            print("A moment of silence, please...")
            with m as source:
                r.adjust_for_ambient_noise(source)
            print("Setting minimum energy threshold to {}".format(r.energy_threshold))
            # while True:
            print("Say something")
            # echo.gtts("Go ahead, I am listening.")

            with m as source:
                # smart2utils.gtts("how is the weather today")
                # smart2utils.gtts("what is ten times 3")
                # smart2utils.play_wav_from_file("bank account password.wav")
                audio = r.listen(source)
                audio_wav_data = audio.get_wav_data()

            print("Processing...")
            # self.current_ms_time = int(round(time.time() * 1000))

            try:
                # recognize speech using CMU Sphinx pocketsphinx
                value = r.recognize_sphinx(audio, language="en-US")
                # print unicode characters to standard output
                print("You said: {}".format(value))

                # store recorded phrase in audio_file_1 wav file
                f = open('audio_file_1.wav', 'w+b')
                f.write(audio_wav_data)
                f.close()
                return value
            except sr.UnknownValueError:
                print("SpeechRecognition: unknown value")
            except sr.RequestError as e:
                print("Couldn't request results from pocketsphinx;{0}".format(e))
        except KeyboardInterrupt:
            pass

    def analyze_audio(self, p_audio_val):
        if self.handle_voice_input(p_audio_val):
            current_ms_time = int(round(time.time() * 1000)) - self.current_ms_time
            rec_length = int(round(smart2utils.get_audio_segment_length()))
            print("RUNTIME = " + str(current_ms_time))
            print("CLIP LENGTH = " + str(rec_length))
            smart2utils.write_runtime("runtime_output.txt", f"{current_ms_time-rec_length}\tBLOCK\t{p_audio_val}\n")
            print("-------------------------")
        else:
            current_ms_time = int(round(time.time() * 1000)) - self.current_ms_time
            rec_length = int(round(smart2utils.get_audio_segment_length()))
            print("RUNTIME = " + str(current_ms_time))
            print("CLIP LENGTH = " + str(rec_length))
            smart2utils.write_runtime("runtime_output.txt", f"{current_ms_time-rec_length}\tFWD\t{p_audio_val}\n")
            # play wake word "Alexa"
            smart2utils.gtts('Alexa')
            # play recorded phrase
            smart2utils.play_wav_file()
            # time.sleep(3)
            print("-------------------------")

    def handle_voice_input(self, p_value: str):
        # ARGUMENT MODE
        if smart2utils.get_loudness() > -5.0 and not self.privacy_on:
            smart2utils.gtts("It sounds like you might be having an argument. Activating privacy mode.")
            self.privacy_on = True
            return True

        # PRIVACY MODE EVALUATION
        if re.search(r'(.*) privacy', p_value, re.M | re.I):
            search_obj = re.search(r'(.*) privacy', p_value, re.M | re.I)
            self.privacy_mode(search_obj.group(1).lower())
            return True

        # INSTRUCT USER TO DEACTIVATE PRIVACY MODE IF THEY WISH TO RESUME NORMAL OPERATION
        if self.privacy_on:
            smart2utils.gtts("Please deactivate privacy mode to relay commands.")
            return True

        # NORMAL OPERATION: KEYWORD EVALUATION
        if re.search(r'affair|bank|girlfriend|account|password|pin', p_value, re.M | re.I):
            search_obj = re.search(r'affair|bank|girlfriend|account|password|pin', p_value, re.M | re.I)
            smart2utils.print_redaction(search_obj.group())
            return True

        # TIME-BASED KEYWORD
        if re.search(r'finance', p_value, re.M | re.I):
            smart2utils.set_timer()
            return True
