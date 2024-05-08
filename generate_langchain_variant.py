import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
import Preprocessing as prep
import pandas as pd

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

recipe_file = "dataset/full_dataset.csv"
recipes = pd.read_csv(recipe_file)

llm = ChatOpenAI(model="gpt-4-turbo")

agent = create_pandas_dataframe_agent(llm, recipes, agent_type="openai-tools")

def generate_message(prompt):
    message = agent.invoke(
        {
            f"""You are a helpful assistant being used for creating creative recipes using items people have left over. 
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

    You can include as many steps and ingredients as you choose, just make sure it follows this structure.
    Give me a recipe that involves {prompt}  """
        }
    )
    return message['output']
