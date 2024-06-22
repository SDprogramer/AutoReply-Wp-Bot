# DEMO

'''
from openai import OpenAI


client = OpenAI(
    api_key="OPEN_API_KEY"
)


completion = client.chat.completions.create(
    model="OPENAI_MODEL",
    messages=[
        {"role": "system", "content": "You are a person named Soumyadeep who speaks hindi english and bengali all 3 languages. "
         "He is from India and he is a coder. You analyze chat history and respond like soumyadeep"},
        {"role": "user", "Content": "generate"}
    ]
)

response = completion.choices[0].message.content
'''