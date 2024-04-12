
import textwrap

import google.generativeai as genai
import markdown as md
from IPython.display import Markdown


def to_HTML(text):
  text = text.replace('•', '  *')
  my_data = Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  return md.markdown(my_data.data)



GOOGLE_API_KEY="AIzaSyCmB8EIudC3M7Jejpa8gCK00MEoyO9Ndbw"

genai.configure(api_key=GOOGLE_API_KEY)
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(to_HTML(response.text))
