# Experiment 12: Conversational AI chatbot using NVIDIA API
# Install first: pip install openai
from openai import OpenAI
from getpass import getpass

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=getpass("NVIDIA API Key: ")
)

messages = [
    {"role": "system",
     "content": "You are a helpful AI and ML chatbot. Answer simply and accurately."}
]

while True:
    user = input("You: ")
    if user.lower().strip() == "bye":
        print("Bot: Goodbye!")
        break

    messages.append({"role": "user", "content": user})
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )
        reply = response.choices[0].message.content
        print("Bot:", reply)
        messages.append({"role": "assistant", "content": reply})
    except Exception as error:
        print("API error:", error)
        messages.pop()
