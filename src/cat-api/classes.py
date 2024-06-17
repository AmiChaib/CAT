
from typing import Annotated, List
from pydantic import BaseModel, StringConstraints, Field

# Request-Body Model
    # Validation through pydantic
pattern = r"^[\s\S]{30,3000}$"
ChecksumInputString = Annotated[str, StringConstraints(pattern=pattern)]

class UserInput(BaseModel):
    input_text: ChecksumInputString
    input_categories: Annotated[List[str], Field(min_items=1)]

class Section(BaseModel):
    section: str = Field(description="text section relevant for identification as sub_category")
    category: str = Field(description="category that best describes the section")
    sub_category: str = Field(description="specifies a subtype or aspect within the category")
    explanation: str = Field(description="brief explanation why this section is identified")