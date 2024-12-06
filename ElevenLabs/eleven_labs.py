# """ElevenLabs speech module"""
# import os

# import requests
# from playsound import playsound


# PLACEHOLDERS = {"your-voice-id"}


# class ElevenLabsSpeech():
#     """ElevenLabs speech class"""

#     def setup(self) -> None:
#         """Set up the voices, API key, etc.

#         Returns:
#             None: None
#         """

#         default_voices = ["21m00Tcm4TlvDq8ikWAM", "MF3mGyEYCl7XYWbV9V6O"]
#         voice_options = {
#             "Rachel": "21m00Tcm4TlvDq8ikWAM",
#             "Domi": "AZnzlk1XvdvUeBnXmlld",
#             "Bella": "EXAVITQu4vr4xnSDxMaL",
#             "Antoni": "ErXwobaYiN019PkySvjV",
#             "Elli": "MF3mGyEYCl7XYWbV9V6O",
#             "Josh": "TxGEqnHWrfWFTfGW9XjX",
#             "Arnold": "VR6AewLTigWG4xSOukaG",
#             "Adam": "pNInz6obpgDQGcFmaJgB",
#             "Sam": "yoZ06aMxZJJ28mfd3POQ",
#             "Xina": "bruh"
#         }
#         self._headers = {
#             "Content-Type": "application/json",
#             "xi-api-key": 'sk_18e2295579d6d5d05064ebea06bbeff7f6e9b5c62cc5599d',
#         }
#         self._voices = default_voices.copy()
#         # self.use_custom_voice(elevenlabs_voice_1_id, 0)
#         # self.use_custom_voice(elevenlabs_voice_2_id, 1)

#     def use_custom_voice(self, voice, voice_index) -> None:
    
#         if voice and voice not in PLACEHOLDERS:
#             self._voices[voice_index] = voice

#     def speech(self, text: str, voice_index: int = 0, only_return: bool = False):
    
#         tts_url = (
#             f"https://api.elevenlabs.io/v1/text-to-speech/{self._voices[voice_index]}/stream"
#         )
#         response = requests.post(tts_url, headers=self._headers, json={"text": text,
#                                                                        "voice_settings":{
#                                                                             "stability": .6,
#                                                                             "similarity_boost": .8, 
#                                                                         }
#                                                                        })

#         if response.status_code == 200:
#             with open("speech.mpeg", "wb") as f:
#                 f.write(response.content)
#                 if only_return:
#                     return True    
#             playsound("speech.mpeg", True)
#             os.remove("speech.mpeg")
#             return True
#         else:
#             print("Request failed with status code:", response.status_code)
#             # print("Response content:", response.content)
#             return False
        
# def play_audio(input_text):
#     tts = ElevenLabsSpeech()
#     tts.setup()
#     saved = tts.speech(input_text, 0)
#     return saved

        
# if __name__ == "__main__":
#     audio = play_audio("What are you doing tanmay and ayush")
#     print(audio)


    # tts = ElevenLabsSpeech()
    # tts.setup()
    # tts.speech("30 SECONDS LEFT....... 10 SECONDS LEFT! SPIKE PLANTED!  ACE!!", 0)


# import os
# import uuid
# from elevenlabs import VoiceSettings
# from elevenlabs.client import ElevenLabs


# client = ElevenLabs(
#     api_key='sk_18e2295579d6d5d05064ebea06bbeff7f6e9b5c62cc5599d',
# )


# def text_to_speech_file(text: str) -> str:
#     # Calling the text_to_speech conversion API with detailed parameters
#     response = client.text_to_speech.convert(
#         voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
#         output_format="mp3_22050_32",
#         text=text,
#         model_id="eleven_turbo_v2_5", # use the turbo model for low latency
#         voice_settings=VoiceSettings(
#             stability=0.0,
#             similarity_boost=1.0,
#             style=0.0,
#             use_speaker_boost=True,
#         ),
#     )

   
#     # play(response)

#     save_file_path = f"{uuid.uuid4()}.mp3"

#     # Writing the audio to a file
#     with open(save_file_path, "wb") as f:
#         for chunk in response:
#             if chunk:
#                 f.write(chunk)

#     print(f"{save_file_path}: A new audio file was saved successfully!")

#     # Return the path of the saved audio file
#     return save_file_path



# text_to_speech_file("my name is ayush gakre from dsce")

# import pyttsx3
# def play_audio(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     audio = play_audio("What are you doing tanmay and ayush")
#     print(audio)

import gtts
import playsound

def play_audio(text):
    sound = gtts.gTTS(text, lang="en",tld="co.in")
    sound.save("ayush.mp3")
    playsound.playsound("ayush.mp3")

if __name__ == "__main__":
    audio = play_audio("What are you doing tanmay and ayush")
    print(audio)
