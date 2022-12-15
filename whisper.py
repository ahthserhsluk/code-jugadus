def recog():
    import requests
    url = "https://whisper.lablab.ai/asr"
    payload={}
    files=[
    ('audio_file',('test1.mp3',open('recording0.mp3','rb'),'audio/mpeg'))
    ]
    response = requests.request("POST", url, data=payload, files=files)
    return response.text

def voice():
    import sounddevice as sd
    from scipy.io.wavfile import write
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write("recording0.mp3", freq, recording)
    return recog()
