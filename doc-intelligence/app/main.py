#initialize docker desktop
#(powershell) docker run --rm -it -v ${PWD}\pdfs:/app/pdfs -v ${PWD}\outputs:/app/outputs docintelligence:latest
#/app/pdfs/chemkine.pdf , /app/pdf/chemkine2.pdf
#venv\Scripts\activate
#python app/main.py
import sys
import json
import os
import time
import re

from document_parser import parse_documents
from embedder import get_embeddings, get_task_embedding
from ranker import rank_sections
from output_formatter import format_output

def sanitize_filename(s):
    s = s.lower()
    s = re.sub(r'\s+', '_', s)
    s = re.sub(r'[^\w\-]', '', s)
    return s[:30]

def is_uninformative_title(text):
    text = text.strip()
    if re.fullmatch(r'\d+\.?', text):
        return True
    if re.match(r'^[A-Z][a-z]+ [A-Z]\.?', text):
        return True
    if re.search(r'Nucleic Acids Res|Brief Bioinform|Adv Neural Inf Process|Bioinformatics', text, re.I):
        return True
    return False

def main():
    if len(sys.argv) < 4:
        persona = input("Enter Persona (role description): ").strip()
        job = input("Enter Job to be Done (task description): ").strip()
        pdf_input = input("Enter PDF file paths, separated by commas: ").strip()
        pdf_files = [p.strip() for p in pdf_input.split(",") if p.strip()]
    else:
        persona = sys.argv[1]
        job = sys.argv[2]
        pdf_files = sys.argv[3:]

    print("Extracting sections from PDFs...")
    parsed_sections = parse_documents(pdf_files)
    print(f"Total sections found: {len(parsed_sections)}")
    if len(parsed_sections) == 0:
        print("Warning: No sections found in the given PDFs.")
        sys.exit(1)

    section_embeddings = get_embeddings([s["sec_text"] for s in parsed_sections])
    task_embedding = get_task_embedding(persona, job)
    ranked_sections = rank_sections(parsed_sections, section_embeddings, task_embedding)

    filtered_sections = [s for s in ranked_sections if not is_uninformative_title(s["section_title"])]

    output_json = format_output(pdf_files, persona, job, filtered_sections)

    persona_safe = sanitize_filename(persona)
    job_safe = sanitize_filename(job)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    os.makedirs("outputs", exist_ok=True)
    out_path = f"outputs/extracted_{persona_safe}_{job_safe}_{timestamp}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2, ensure_ascii=False)

    print(f"Results written to {out_path}")

if __name__ == "__main__":
    main()


