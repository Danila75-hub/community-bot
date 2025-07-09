from utils.faqloader import load_faq, FAQItem
from typing import List
from pathlib import Path


def validate_faq_items(items: List[FAQItem]):
    for idx, item in enumerate(items):
        if not item.question or not item.answers:
            print(f"❌ Entry {idx} is incomplete: {item.dict()}")
        elif isinstance(item.answers, list) and not all(isinstance(a, str) for a in item.answers):
            print(f"⚠️  Entry {idx} has non-string answers: {item.answers}")
        elif isinstance(item.answers, str) and not item.answers.strip():
            print(f"⚠️  Entry {idx} has an empty string answer.")
    print(f"\n✅ Checked {len(items)} entries.")


if __name__ == "__main__":
    path = Path("faq.json")
    try:
        items = load_faq(path)
        validate_faq_items(items)
    except Exception as e:
        print(f"❌ Error: {e}")
