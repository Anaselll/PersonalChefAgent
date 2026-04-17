from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import GOOGLE_API_KEY


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=GOOGLE_API_KEY
)