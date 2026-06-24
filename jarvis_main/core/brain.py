from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def think(command):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, an intelligent personal assistant."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message.content
    except:
        return "AI connection failed."