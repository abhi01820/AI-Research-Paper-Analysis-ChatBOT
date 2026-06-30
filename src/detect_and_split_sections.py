import json
from typing import List, Dict


def refine_sections(input_list: str, llm) -> List[Dict]:
    prompt = f"""
You are a precise data processor.

I will give you a JSON list of sections from a research paper. Each item may have:
- "section" (string)
- optional "subsection" (string)
- "start" (integer)

Some entries are unnecessary and must be **removed completely**:
1. Figure or Table captions (any "section" starting with "Figure" or "Table").
2. Incomplete, meaningless, or fragment sections (e.g., "making", "length nis smaller...").
3. Any other irrelevant entries that are not proper sections or subsections.

Your task is to **refine this list**:

- Keep only meaningful main sections and their subsections.
- Main sections should be in the format: 
  {{"section": "Section Name", "start": number}}
- Subsections should be in the format: 
  {{"section": "Parent Section", "subsection": "Subsection Name", "start": number}}
- The output must be **strictly a JSON array of dictionaries**.
- Do **not** include any explanations, notes, extra text, or commentary.
- If a section is unnecessary (e.g., figure, table, fragment), **exclude it completely**.

Here is the input JSON:

{input_list}

Always return list of dictionaries only, no preamble.
"""


    try:
        assistant_text = llm.invoke(prompt).content.strip()
        sections = json.loads(assistant_text)
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print("Warning: LLM output not valid JSON. Returning empty list.")
        print("Error:", e)
        sections = []

    return sections

