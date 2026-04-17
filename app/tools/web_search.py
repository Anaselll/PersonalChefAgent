from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from app.core.config import TAVILY_API_KEY
tavily_client = TavilyClient()

@tool 
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)

web_search.invoke("Who is the current mayor of San Francisco?")