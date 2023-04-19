import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"demoServiceAccount.json"

# Instantiates a client
client = texttospeech_v1.TextToSpeechClient()

text = '''Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices,
available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible.
As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices.
'''

synthesis_input = texttospeech_v1.SynthesisInput(text=text)

voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code="en-in", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

voice2 = texttospeech_v1.VoiceSelectionParams(
    name = 'vi-VN-Wavenet-D',
    language_code="vi-VN",
    
)

audio_config = texttospeech_v1.AudioConfig(
     audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

response1 = client.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)

response2 = client.synthesize_speech(
    input=synthesis_input,
    voice=voice2,
    audio_config=audio_config
)

with open('audio file1.mp3', 'wb') as output1:
    output1.write(response1.audio_content )
with open('audio file2.mp3', 'wb') as output1:
    output1.write(response2.audio_content )
