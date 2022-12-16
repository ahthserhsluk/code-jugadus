def recog():
    import requests
    url = "https://whisper.lablab.ai/asr"
    payload={}
    files=[
    ('audio_file',('test1.mp3',open('recording0.mp3','rb'),'audio/mpeg'))
    ]
    response = requests.request("POST", url, data=payload, files=files)
    return response.text

def voice(sec=10):
    import sounddevice as sd
    from scipy.io.wavfile import write
    freq = 44100
    duration = sec
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write("recording0.mp3", freq, recording)
    return recog()
