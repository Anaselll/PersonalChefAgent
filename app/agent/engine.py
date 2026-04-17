from langchain.agents import create_agent


from app.tools.web_search import web_search
from langchain.messages import HumanMessage
from app.model.groq import model
from langgraph.checkpoint.memory import InMemorySaver



agent=create_agent(
    model=model,
    tools=[web_search],
    system_prompt="you are a personal chef that cook the best food based on ingredients",
    checkpointer=InMemorySaver()
)

config={"configurable":{"thread_id":"1"}}

response=agent.invoke({
    "messages":[HumanMessage(content="i have tomato pasta and chicken")],
  
},  config)

response=agent.invoke({
    "messages":[HumanMessage(content="detail this recipe")],
  
},  config)



print(response["messages"])