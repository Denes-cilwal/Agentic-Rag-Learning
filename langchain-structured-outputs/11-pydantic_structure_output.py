from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class Review(BaseModel):
    keythemes: list[str] = Field(..., description="Main themes discussed in the review")
    summary: str = Field(..., description="A brief summary of the review")
    sentiment: Literal["positive", "negative", "mixed"] = Field(
        ..., description="Overall sentiment"
    )

structured_output = model.with_structured_output(Review, method="function_calling")

result = structured_output.invoke(
    "The hardware specifications of the new iPhone are impressive. "
    "There are too many installed apps that I cannot remove. "
    "Also the UI looks cluttered. Hoping for a better experience next time."
)

print(result)                 # Review(...)
print(result.summary)         # ✅
print(result.sentiment)       # ✅
print(result.keythemes)       # ✅

as_dict = result.model_dump() # ✅ convert to dict (pydantic v2)
print(as_dict["summary"])
