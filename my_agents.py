from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import os

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=provider,
)

# web developer agent
web_developer = Agent(
    name="Web Developer",
    instructions="A web developer who can build websites and web applications",
    model=model,
    handoff_description= "handsoff to web developer if the task is related to web development"
)

# app developer agent

app_developer = Agent(
    name = "App Developer",
    instructions="Develop cross-platform mobile apps for ios and Andorid",
    model= model,
    handoff_description ="handsoff to mobile app developer if te task is realted to app developer"
)

# Marketing agent

marketing = Agent(
    name = "Marketing Agent",
    instructions="create and executes marketing strategies for product launchies",
    model = model,
    handoff_description= "hadsoff to marketing agent if the task  is related to marketing"
)

async def myAgent(user_input):
    # manager agent
    manager = Agent(
        name = "manager",
        instructions= """You are a helpful assistant that can only help with 3 specific things:

1. Web Development - Building websites and web applications
2. Mobile App Development - Creating cross-platform mobile apps for iOS and Android  
3. Marketing - Creating and executing marketing strategies for product launches

If the user asks for anything related to these 3 topics, help them appropriately.

If the user asks for anything else (like cooking, sports, movies, general chat, etc.), simply respond with:
 "Sorry, I can only help with web development, mobile app development, and marketing. Please ask me about one of these topics."
""",
        model= model,
        handoff_description = ["web developer", "app developer", "marketing agent"]
        )
    response = await Runner.run(
        manager,
        input = user_input,
        )

    return response.final_output





