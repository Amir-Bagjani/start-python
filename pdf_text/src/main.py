from pathlib import Path

from constants import RESUME_SCHEME_PROMPT
from llm_interface import ask_ai
from PyPDF2 import PdfReader


def extract_pdf_text(file_path: str | Path) -> str:

    reader = PdfReader(Path(file_path))

    resume_text = ""
    for page_text in reader.pages:
        resume_text += page_text.extract_text()

    return resume_text


print("Loading...")
prompt = f"{RESUME_SCHEME_PROMPT}\n\n{extract_pdf_text('resume.pdf')}"
print(ask_ai(prompt))
