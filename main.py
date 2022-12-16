import os
import openai
import webbrowser
from input import voice_input

def file(text):
    fname='template 1/kj3.html'
    f=open(fname, 'w')
    f.write(text)
    f.close()
    webbrowser.open(os.path.realpath(fname))


initialPromt = voice_input()


print("lets make your website")
openai.api_key = ''
a=openai.Completion.create(
  model="text-davinci-003",
  prompt=initialPromt,
  max_tokens=2380,
  temperature=0.9
)
file(a['choices'][0]['text'])


