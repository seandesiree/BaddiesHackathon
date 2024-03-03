import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.5)

#Defining the AI's Job
system_template = "You are a compassion coach, helping people achieve their goals step by step. You give them the most up to date and accurate information."
system_message_prompt = SystemMessagePromptTemplate(system_template)

# Human prompt template
human_template = "{input_text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
