from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import GOOGLE_API_KEY
from pydantic import BaseModel

class Recipe(BaseModel):
    ingredients: list[str]
    recipe: str
    steps: list[str]
    tips: str

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
   
    
)