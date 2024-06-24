# # DEMO

# from openai import OpenAI


# # pip install openai
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#    api_key="Your Api Key"
# )


# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a person named Soumyadeep and you speak Hindi Bengali aand English as well. He is from India and is a coder. You analyse chat history and respond like Soumyadeep"},
#     {"role": "user", "content": ""}
#   ]
# )

# print(completion.choices[0].message.content)