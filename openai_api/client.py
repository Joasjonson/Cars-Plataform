from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key="OPENAI_API_KEY")
                



def get_car_ai_description(name, brand, model_year):
    message="""
    Generate a sales description for car model {} from {} in {} with a maximum of 200 characters, include technical specifications.
    """

    message = message.format(name, brand, model_year)
    response = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": message}
        ],
        model="gpt-3.5-turbo",
        max_tokens=100,
    )
    return response.data.choices[0].message['content']
   