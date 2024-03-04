from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


completion = client.chat.completions.create(model="gpt-3.5-turbo-0125", messages=[{"role": "user", "content": "For a Hackathon I worked with a team of 5 people to create a custom chatbot. I built the backend using python and Open AI. How do I write this in a cover letter?"}])
print(completion.choices[0].message.content)
