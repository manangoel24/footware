from PyPDF2 import PdfReader
import tempfile
import os

# Extract content from uploaded file for context injection
def get_review_snippets(file):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        text = ""
        # PDF handling
        if file.name.lower().endswith(".pdf"):
            reader = PdfReader(tmp_path)
            text = "\n".join(
                page.extract_text() or "" for page in reader.pages
            )
        else:
            with open(tmp_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

        os.remove(tmp_path)

        # Summarize or trim for injection
        snippet = text[:1000] if len(text) > 1000 else text
        return f"Here are some notes or references from the user's upload:\n\n{snippet}"

    except Exception as e:
        print("Failed to extract context:", e)
        return None
