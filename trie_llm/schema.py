from pydantic import BaseModel
from typing import List

#Schema for the ThemedWordList
class ThemedWordList(BaseModel):
    # Pydantic Word validation for the list 
    words = List[str]