
from openai import OpenAI
import os
#print("Initializing OpenAI client")
apikey=""


client = OpenAI(
  api_key=apikey,
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a musical assistant, skilled in suggesting songs related to various themes."},
    {"role": "user", "content": "Compose a song on nature"}
  ]
)


# print(completion.choices[0].message)
print(completion)
response=completion
# Print the assistant's message content specifically
tokens=response.usage.total_tokens
print("total tokens:", tokens)
