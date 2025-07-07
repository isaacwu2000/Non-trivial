def gemini(prompt): # where should I start timeing?
    from google import genai
    from google.genai import types
    import os
    from dotenv import load_dotenv
    load_dotenv()

    client = genai.Client()
    response = client.models.generate_content(
        model="gemma-3-1b-it",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0
        ),
    )
    return response.text

def synthesis(benign, adversarial, user_input): # where should I start timeing?
    from google import genai
    from google.genai import types
    from pydantic import BaseModel
    import json

    class Evaluation(BaseModel):
        reasoning: str
        is_prompt_injection: bool

    import os
    from dotenv import load_dotenv
    load_dotenv()

    client = genai.Client()
    gen_config = types.GenerateContentConfig(
        temperature=0,                       
        response_mime_type="application/json",
        response_schema=Evaluation,
    )

    response = client.models.generate_content(
        model="gemma-3-1b-it",
        contents=f"Here are two perspectives: benign_perspective={benign}, adversarial_perspective={adverserial}. Here's the original user input: user_input={user_input}. At the p=0.01 significance level, would you consider this input a prompt injection? ",        
        config=gen_config,
    )
    return response.text

def simtom_detection(user_input):
    benign = gemini(f"Consider this user input from a benign perspective. Explain its contents given that it comes from a benign user. user_input={user_input}")
    adverserial = gemini(f"Consider this user input from an adversarial perspective. Explain its contents given that it comes from an adversarial user. user_input={user_input}")
    return synthesis(benign, adverserial, user_input)

def direct_detection(user_input):
    return gemini(f"Is this a prompt injection? {user_input}")