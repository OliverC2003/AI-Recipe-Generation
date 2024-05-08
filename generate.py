import os
from openai import OpenAI
from dotenv import load_dotenv
import Preprocessing as prep


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

def generate_stream(Prompt: str):
    stream = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": """You are a helpful assistant being used for creating creative recipes using items people have left over. 
Always output your answer using this format:
Name Of dish:
### Ingredients:
- Ingredient 1
- Ingredient 2

### Instructions:
1. **Instruction 1:**
   - Explain instruction 1

2. **Instruction 2:**
   - Explain instruction 2

3. **Instruction 3:**
   - Explain instruction 3

You can include as many steps and ingredients as you choose, just make sure it follows this structure  """},
        {"role": "user", "content": Prompt}
        ],
    stream=True,
    )
    return stream

def generate_message(Prompt: str):
    stream = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": """You are a helpful assistant being used for creating creative recipes using items people have left over. 
Always output your answer using this format:
Name Of dish:
### Ingredients:
- Ingredient 1
- Ingredient 2

### Instructions:
1. **Instruction 1:**
   - Explain instruction 1

2. **Instruction 2:**
   - Explain instruction 2

3. **Instruction 3:**
   - Explain instruction 3

You can include as many steps and ingredients as you choose, just make sure it follows this structure  """},
        {"role": "user", "content": Prompt}
        ],
    )
    return stream.choices[0].message.content
    
def display_stream(stream: str):
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

def generate_image(Prompt: str):
    response = client.images.generate(
    model="dall-e-3",
    prompt= Prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
    return response.data[0].url

def print_recipe_with_images(preprocessed_recipe):
    item_of_food, ingredients, instructions = preprocessed_recipe
    print(item_of_food)
    print(generate_image(item_of_food))

    print(str(ingredients))
    print(generate_image(str(ingredients)))

    for instruction in instructions:
        print(instruction)
        print(generate_image(instruction))


