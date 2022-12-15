import os
import openai
import webbrowser
from input import input

def file(text):
    fname='template 1/kj3.html'
    f=open(fname, 'w')
    f.write(text)
    f.close()
    webbrowser.open(os.path.realpath(fname))


initialPromt = input()

openai.api_key = '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'
a=openai.Completion.create(
  model="text-davinci-003",
  prompt=initialPromt,
  max_tokens=2380,
  temperature=0.9
)

file(a['choices'][0]['text'])