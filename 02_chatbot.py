from openai import OpenAI


#pip install openai
#If you saved the key under a different envirionment variable name, you can do something like:

client = OpenAI(
    api_key="<YOUR API KEY HERE>",
)

command='''

'''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named om who speaks hindi, english and marathi. He is from India and an engineer. You analyze chat history and respond like om."},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)