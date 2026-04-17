from langchain.agents import create_agent


from app.tools.web_search import web_search
from langchain.messages import HumanMessage
from app.model.groq import model




agent=create_agent(
    model=model,
    tools=[web_search],
    system_prompt="you are a personal chef that cook the best food based on ingredients"
)



response=agent.invoke({
    "messages":[HumanMessage("i have tomato pasta and chicken")]
})


print(response["messages"][-1].content)