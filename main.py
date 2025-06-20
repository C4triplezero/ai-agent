import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
try:
    prompt = sys.argv[1]
except:
    print("Error: Invalid prompt")
    sys.exit(1)

messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

response = client.models.generate_content(model="gemini-2.0-flash-001", contents = messages)
print(response.text)

if sys.argv.__contains__("--verbose"):
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")