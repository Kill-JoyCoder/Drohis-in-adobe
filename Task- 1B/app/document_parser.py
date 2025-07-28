import fitz  
import re
 
SECTION_HEADING_KEYWORDS = [
    'abstract', 'introduction', 'background', 'method', 'methods', 'results',
    'discussion', 'conclusion', 'summary', 'references', 'acknowledgement',
    'experiments', 'datasets', 'benchmark', 'evaluation', 'analysis',
    'materials', 'overview', 'related work', 'future work', 'implementation',
    'findings', 'approach', 'technique', 'algorithm', 'data', 'validation',
    'comparison', 'experiment', 'application', 'framework',
]

def is_heading(text: str, spans) -> bool:
    text_lower = text.strip().lower()

    
    if any(text_lower.startswith(k) for k in SECTION_HEADING_KEYWORDS):
        return True

    
    if any(span["size"] >= 13 for span in spans):
        return True
    if any('bold' in span["font"].lower() for span in spans):
        return True

    
    if len(text) < 60 and text.isupper():
        return True

    return False

def is_uninformative_section(text: str) -> bool:
    text = text.strip()
    # Remove numeric-only section titles
    if re.fullmatch(r'\d+\.?', text):
        return True
    # Common citation and author-name patterns 
    if re.match(r'^[A-Z][a-z]+ [A-Z]\.?', text):
        return True
    if re.search(r'Nucleic Acids Res|Brief Bioinform|Adv Neural Inf Process|Bioinformatics', text, re.I):
        return True
    return False

def parse_documents(pdf_files):
    sections = []
    for pdf in pdf_files:
        doc = fitz.open(pdf)
        for i, page in enumerate(doc):
            blocks = page.get_text("dict")["blocks"]
            page_text = []
            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        line_text = " ".join(span["text"] for span in line["spans"]).strip()
                        if not line_text:
                            continue

                        if is_heading(line_text, line["spans"]):
                            page_text.append({"type": "heading", "text": line_text})
                        else:
                            page_text.append({"type": "body", "text": line_text})

            for idx, chunk in enumerate(page_text):
                if chunk["type"] == "heading" and not is_uninformative_section(chunk["text"]):
                    body_lines = []
                    
                    for nxt in page_text[idx + 1: idx + 11]:
                        if nxt["type"] == "body":
                            body_lines.append(nxt["text"])
                        else:
                            break
                    if body_lines:
                        sections.append({
                            "document": pdf,
                            "page_number": i + 1,
                            "section_title": chunk["text"],
                            "sec_text": " ".join(body_lines)
                        })
        doc.close()
    return sections
