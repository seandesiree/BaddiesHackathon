from openai import OpenAI

client = OpenAI(api_key="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")


completion = client.chat.completions.create(model="gpt-3.5-turbo-0125", messages=[{"role": "user", "content": "How do I fix this error in Visual Studio Code: DEPRECATION: textract 1.6.5 has a non-standard dependency specifier extract-msg<=0.29.*. pip 24.1 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of textract or contact the author to suggest that they release a version with a conforming dependency specifiers.'?"}])
print(completion.choices[0].message.content)
