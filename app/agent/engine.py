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
        You are a personal chef.

        You MUST ALWAYS respond ONLY in valid JSON.

        No explanation. No markdown. No text outside JSON.

        Format:
        {
        "ingredients": [],
        "recipe": "",
        "steps": [],
        "tips": ""
        }
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

    response = agent.invoke(
        {"messages": [message]},
        config
    )

    response["messages"][-1].content[0]["text"]
    output= response["messages"][-1].content[0]["text"]
    cleaned = re.sub(r"```json|```", "", output).strip()
    try:
        parsed = json.loads(cleaned)
    except Exception:
        parsed = {
            "error": "Invalid JSON from model",
            "raw_output": cleaned
        }

    return parsed