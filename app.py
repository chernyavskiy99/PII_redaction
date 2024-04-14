from fastapi import FastAPI, Form
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

@app.post("/pii-redact")
async def pii_redact(text: str = Form(...)):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are an AI assistant that redacts personally identifiable information (PII) from text."},
            {"role": "user", "content": f"Please redact any PII from the following text:\n\n{text}"}
        ]
    )

    redacted_text = completion.choices[0].message.content
    return {"redacted_text": redacted_text}
