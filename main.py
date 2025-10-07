import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import SYS_PROMPT as system_prompt, MAX_ITERS as max_iterations
from call_function import call_function, available_functions


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    count = 0
    while count < max_iterations:
        count+= 1
        try:
            output = generate_content(client, messages, verbose)
            if output:
                print("Final Response:")
                print(output)
                break
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Maximum iterations ({max_iterations}) reached.")

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.function_calls:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            function_call_response = function_call_result.parts[0].function_response.response
            if not function_call_response:
                raise Exception("empty function call result")
            elif verbose:
                print(f"-> {function_call_response}")
            messages.append(types.Content(role="user", parts=function_call_result.parts))
    else:
        return response.text


if __name__ == "__main__":
    main()