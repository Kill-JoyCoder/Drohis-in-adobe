# main.py
import fitz
import json
import os
from glob import glob


with open("Task-1A/schema/output_schema.json", "r", encoding="utf-8") as f:
    OUTPUT_SCHEMA = json.load(f)

def extract_outline(pdf_path, max_pages=50):
    doc = fitz.open(pdf_path)
    metadata_title = doc.metadata.get("title", "").strip()
    title = metadata_title or ""

    if not title and len(doc) >= 1:
        spans = [
            span
            for block in doc[0].get_text("dict")["blocks"]
            if "lines" in block
            for line in block["lines"]
            for span in line["spans"]
        ]
        if spans:
            largest = max(spans, key=lambda s: s["size"])
            title = largest["text"].strip()

    outline = []
    for page_idx in range(min(len(doc), max_pages)):
        page = doc[page_idx]
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]
                    if len(text) < 2:
                        continue

                    if size >= 16:
                        level = "H1"
                    elif 13 <= size < 16:
                        level = "H2"
                    elif 11 <= size < 13:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_idx + 1
                    })

    # dedupe + preserve order
    seen = set()
    deduped = []
    for item in outline:
        key = (item["level"], item["text"], item["page"])
        if key not in seen:
            seen.add(key)
            deduped.append(item)

    return {
        "title": title or "Untitled Document",
        "outline": deduped
    }

def validate_against_schema(data, schema):
    #min recursive validation
    def _validate(obj, sch, path=""):
        if "type" in sch:
            t = sch["type"]
            if t == "object":
                if not isinstance(obj, dict):
                    return False, f"Expected object at {path}"
                for prop, prop_sch in sch.get("properties", {}).items():
                    if prop in obj:
                        ok, msg = _validate(obj[prop], prop_sch, path + f".{prop}")
                        if not ok:
                            return False, msg
                    elif prop in sch.get("required", []):
                        return False, f"Missing required {path}.{prop}"
                return True, ""
            elif t == "array":
                if not isinstance(obj, list):
                    return False, f"Expected array at {path}"
                item_sch = sch["items"]
                for idx, itm in enumerate(obj):
                    ok, msg = _validate(itm, item_sch, path + f"[{idx}]")
                    if not ok:
                        return False, msg
                return True, ""
            elif t == "string":
                if not isinstance(obj, str):
                    return False, f"Expected string at {path}"
                return True, ""
            elif t == "integer":
                if not isinstance(obj, int):
                    return False, f"Expected integer at {path}"
                return True, ""
        return True, ""
    return _validate(data, schema)

def main():
    IN_DIR = os.path.join("Task-1A/input")
    OUT_DIR = os.path.join("Task-1A/output")
    os.makedirs(OUT_DIR, exist_ok=True)

    pdfs = glob(os.path.join(IN_DIR, "*.pdf"))
    if not pdfs:
        print("No PDFs found in input/")
        return

    for pdf_path in pdfs:
        base = os.path.basename(pdf_path)
        name, _ = os.path.splitext(base)
        out_path = os.path.join(OUT_DIR, f"{name}.json")

        print(f"➡️ Processing {base} ...")
        data = extract_outline(pdf_path)

        ok, err = validate_against_schema(data, OUTPUT_SCHEMA)
        if not ok:
            print(f"Schema validation failed for {base}: {err}")
            continue

        with open(out_path, "w", encoding="utf-8") as fout:
            json.dump(data, fout, indent=2, ensure_ascii=False)
        print(f"Output written to output/{name}.json")

if __name__ == "__main__":
    main()