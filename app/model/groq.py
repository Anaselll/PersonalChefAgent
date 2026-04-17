from langchain_groq import ChatGroq
from app.core.config import GROQ_API_KEY
model = ChatGroq(
    model="qwen/qwen3-32b",
)