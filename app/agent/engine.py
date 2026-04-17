from langchain_core.messages import HumanMessage
import re
from app.model.gemini import model
from langchain.agents import create_agent
from app.tools.web_search import web_search
from langgraph.checkpoint.memory import InMemorySaver
import json
checkpointer = InMemorySaver()
config = {
        "configurable": {
            "thread_id": "1"
        }
    }



agent = create_agent(
    model=model,
    tools=[web_search],
  system_prompt = """
        You are a personal chef assistant.

        You search the web and create the best possible recipe based on ingredients.

        Always respond in this exact format:

        Ingredients:
        - item 1
        - item 2

        Recipe:
        (short title)

        Steps:
        1. step one
        2. step two
        3. step three

        Tips:
        - useful cooking tips
        """,
    checkpointer=checkpointer
)
def engine(input_type: str, data: str):

    if input_type == "text":
        message = HumanMessage(content=data)

    elif input_type == "image":
        message = HumanMessage(content=[
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{data}"
                }
            }
        ])

    else:
        raise ValueError("Invalid input type")

    response = agent.invoke({"messages": [message]}, config)

    output = response["messages"][-1].content

    
    return output