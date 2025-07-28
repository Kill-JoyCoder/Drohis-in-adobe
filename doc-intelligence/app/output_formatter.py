import time
import re

def extract_key_sentences(text: str, max_sentences=10, window=100, min_length=300, max_length=1500) -> str:
    keywords = [
        'important', 'significant', 'key', 'main', 'notable', 'critical',
        'major', 'best', 'useful', 'relevant', 'core', 'primary', 'essential',
        'conclusion', 'summary', 'overview', 'findings', 'results', 'implication',
        'performance', 'effect', 'measure', 'benchmark', 'analysis', 'study',
        'discussed', 'highlighted', 'demonstrates', 'suggests', 'indicates',
        'determines', 'examined', 'reported', 'observed', 'proposed', 'approach',
        'method', 'technique', 'algorithm', 'data', 'evaluation', 'validation',
        'comparison', 'experiment', 'accuracy', 'resulting', 'impact', 'advantage',
        'limitations', 'application', 'framework'
    ]

    sentences = re.split(r'(?<=[.!?])\s+', text)
    if not sentences:
        return text.strip()

    def sentence_score(s):
        s_lower = s.lower()
        return sum(s_lower.count(k) for k in keywords)

    scored = [(sentence_score(s), s, idx) for idx, s in enumerate(sentences)]
    scored.sort(key=lambda x: (-x[0], x[2]))

    selected = []
    for score, sent, idx in scored:
        if score == 0:
            continue
        selected.append((idx, sent))
        if len(selected) >= max_sentences:
            break

    if len(selected) < max_sentences:
        existing = {idx for idx, _ in selected}
        for idx, s in enumerate(sentences):
            if idx not in existing:
                selected.append((idx, s))
            if len(selected) >= max_sentences:
                break

    selected.sort(key=lambda x: x[0])
    summary = ' '.join(s for _, s in selected).strip()

    if len(summary) < min_length and len(text) > len(summary):
        first_sent = selected[0][1] if selected else sentences[0]
        start_idx = text.find(first_sent)
        if start_idx == -1:
            start_idx = 0
        start_window = max(0, start_idx - window)
        end_window = min(len(text), start_idx + max_length)
        summary = text[start_window:end_window].strip()
        if end_window < len(text):
            summary += "..."

    if len(summary) < min_length:
        summary = text[:max_length].strip()
        if len(text) > max_length:
            summary += "..."

    return summary

def format_output(pdf_files, persona, job, ranked_sections):
    metadata = {
        "input_documents": [{"filename": f, "title": None} for f in pdf_files],
        "persona": persona,
        "job_to_be_done": job,
        "processing_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z")
    }
    extracted_sections = [
        {
            "document": s["document"],
            "page_number": s["page_number"],
            "section_title": s["section_title"],
            "importance_rank": s["importance_rank"]
        } for s in ranked_sections
    ]
    subsection_analysis = [
        {
            "document": s["document"],
            "page_number": s["page_number"],
            "section_title": s["section_title"],
            "refined_text": extract_key_sentences(s["sec_text"])
        } for s in ranked_sections
    ]
    return {
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
