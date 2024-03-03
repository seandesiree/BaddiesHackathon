from dotenv import load_dotenv
import os
import time
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

ASSISTANT_ID = "asst_LARLDLzD9HaY0QBokjoZrJ2Q"

# Make sure your API key is set as an environment variable.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Create a thread with a message.

message = input("")
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            # Update this with the query you want to use.
            "content": message,
        }
    ]
)

# Submit the thread to the assistant.
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID, model="gpt-3.5-turbo")
print(f"👉 Run Created: {run.id}")

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"🏃 Run Status: {run.status}")
    time.sleep(1)
else:
    print(f"🏁 Run Completed!")

# Get the latest message from the thread.
message_response = client.beta.threads.messages.list(thread_id=thread.id)
messages = message_response.data

# Print the latest message.
latest_message = messages[0]
print(f"💬 Response: {latest_message.content[0].text.value}")