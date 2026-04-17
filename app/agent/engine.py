from langchain.agents import create_agent


from app.tools.web_search import web_search
from langchain.messages import HumanMessage
# from app.model.groq import model
from langgraph.checkpoint.memory import InMemorySaver
from app.model.gemini import model


agent=create_agent(
    model=model,
    tools=[web_search],
    system_prompt="you are a personal chef that cook the best food based on ingredients",
    checkpointer=InMemorySaver()
)
config={"configurable":{"thread_id":"1"}}

def engine(input_type="text",input=None):
    user_message = HumanMessage(content=input if input_type == "text" else [{
        "type": "image",
        "base64": input,
        "mime_type": "image/png"
    }])
   
    response=agent.invoke({
            "messages":[user_message],

        },  config)


    return response