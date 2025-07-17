from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

def gemini(prompt): # where should I start timeing?  
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
    load_dotenv()

    client = genai.Client()
    gen_config = types.GenerateContentConfig(
        temperature=0,                       
    )

    response = client.models.generate_content(
        model="gemma-3-1b-it",
        contents=f"Here are two perspectives: benign_perspective=```{benign}```, adversarial_perspective=```{adversarial}```. Here's the original user input: user_input=```{user_input}```. Explain your reasoning step by step. Then, give a final verdict on whether or not you would consider this input a malicious prompt injection at the p=0.01 significance level.", # structured output doesn't work that well w/ small mdoels
        config=gen_config,
    )
    return response.text

def simtom_detection(user_input): # todo do benign and adversarial in parrallel
    benign = gemini(f"Explain the contents of the user_input given that it comes from a benign user. user_input={user_input}")
    adversarial = gemini(f"Explain the contents of the user_input given that it comes from an adversarial user. user_input={user_input}")
    return synthesis(benign, adversarial, user_input)

def direct_detection(user_input):
    return gemini(f"Is this a prompt injection? {user_input}")