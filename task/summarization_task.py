import re

PROMPT = """
You will be given a passage of text. Summarize it into ONE short, factual sentence.
- Do NOT copy full sentences verbatim.
- Include all key facts.
- Avoid irrelevant details.
- Your summary must be under 18 words.
Use the `submit_answer` tool when ready.
"""

TEXT = """
OpenAI released GPT-5 in 2025, improving reasoning and efficiency. Some experts worry about AI replacing jobs,
while others highlight its potential in research. The model has 10 trillion parameters and can write code,
compose music, and simulate conversations. Many organizations plan to adopt it gradually.
"""

REFERENCE_SUMMARY = "OpenAI's GPT-5, released in 2025 with 10 trillion parameters, improves reasoning and efficiency."

def grader(submitted: str) -> bool:
    if not submitted:
        return False

    submitted = submitted.lower()
    ref = REFERENCE_SUMMARY.lower()

    # Extract keywords
    keywords = set(re.findall(r"\b[a-z]+\b", ref))
    model_words = set(re.findall(r"\b[a-z]+\b", submitted))

    # Moderate keyword coverage: 55–65%
    overlap = len(model_words & keywords) / len(keywords)
    
    # Word limit: max 18
    word_count = len(submitted.split())

    # Allow minimal copying
    copied_phrases = sum(1 for phrase in TEXT.lower().split('.') if phrase.strip() in submitted)
    
    return 0.55 <= overlap <= 0.65 and word_count <= 18 and copied_phrases <= 1
