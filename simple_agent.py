from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()],
    markdown=True #display output
)

#after this can use streamlit framework
#here we are using already available ones
agent.print_response("Who won the India vs Newzeland finals in CT 2025")