import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
)
print(response.text)
if response.usage_metadata:
    metadata = response.usage_metadata
    print('Prompt tokens: ' + str(metadata.prompt_token_count))
    print('Response tokens: ' + str(metadata.candidates_token_count))
else:
    print('No usage metadata in response')
