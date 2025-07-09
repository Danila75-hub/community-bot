import json
from typing import List
from pydantic import BaseModel


class FAQItem(BaseModel):
    question: str
    answers: List[str]


def load_faq_from_json(file_path: str) -> List[FAQItem]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [FAQItem(**item) for item in data if isinstance(item, dict)]
