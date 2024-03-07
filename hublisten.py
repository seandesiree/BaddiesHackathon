from openai import OpenAI
import os 
from dotenv import load_dotenv

#connect to script.JS


load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


#input for creating chatbot personality
messages = []
system_msg = input("What type of assistant are you looking to create today? Don't be afraid to give it some personality and a profession. Example: A sassy healthcare professional. To end your chat session, type quit.\n")
messages.append({"role": "system", "content": system_msg})
print("Your new asistant is ready!")

#input for human questions
while input != "quit()":
    message = input("")
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
