import random
from difflib import get_close_matches
from utils.faqloader import FAQItem


def find_answer(faq_data: list[FAQItem], question: str) -> str:
    normalized_question = question.strip().lower()
    questions_list = [item.question.strip().lower() for item in faq_data]
    matches = get_close_matches(
        normalized_question, questions_list, n=1, cutoff=0.6)

    if matches:
        matched_question = matches[0]
        for item in faq_data:
            if item.question.strip().lower() == matched_question:
                if item.answers:
                    return random.choice(item.answers)
    return "Sorry, I don't have an answer for that yet."


def is_personal_question(question: str) -> bool:
    personal_keywords = ['my', 'me', 'personal',
                         'account', 'profile', 'delete']
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in personal_keywords)
